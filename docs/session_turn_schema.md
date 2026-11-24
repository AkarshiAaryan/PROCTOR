# GuardSLM: Session and Turn Data Schema
## Simplified Machine-Readable JSON Schema (Phase 1.2)

---

## 1. Schema Design Principles

The Phase 1.2 data schema provides a platform-independent specification for GuardSLM benchmark records:
1. **No Proprietary Database Concepts**: Fully decoupled from Moodle internals, table names, XMLDB files, and platform-specific capability strings.
2. **Strict Isolation of Gold Truth and Model Predictions**: Ground-truth human annotations (`gold_guard_decision`, `gold_auditor_label`) are strictly isolated from model evaluation outputs (`model_guard_prediction`, `model_auditor_prediction`).
3. **First-Class Browser Accessibility Snapshot**: Captures the raw Playwright accessibility tree (`browser_snapshot`) as an active runtime input at every turn.
4. **Disambiguated Help-Level Fields**: Distinguishes what the student asked for (`explicitly_requested_help_level`), what was inferred (`inferred_requested_help_level`), what policy permits (`permitted_help_ceiling`), and what was delivered (`actually_delivered_help_level`).
5. **Complete Empirical Provenance**: Tracks whether each session is a `real_source`, `adapted_synthetic`, or `original_synthetic` record.

---

## 2. Master JSON Schema (Draft 2020-12)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "GuardSLM_SessionRecord_v1_2",
  "description": "Canonical schema for complete multi-turn conversational sessions in the GuardSLM benchmark.",
  "type": "object",
  "required": [
    "session_id",
    "session_title",
    "synthetic_user_id",
    "authenticated_role",
    "user_profile",
    "course_id",
    "resource_id",
    "resource_type",
    "resource_scope",
    "resource_lifecycle_state",
    "applicable_policy_ids",
    "scenario_id",
    "source_provenance",
    "session_summary",
    "gold_auditor_label",
    "auditor_behaviour_tags",
    "dataset_split",
    "turns"
  ],
  "properties": {
    "session_id": {
      "type": "string",
      "pattern": "^sess_[a-z0-9_]+$",
      "description": "Unique session identifier (e.g., sess_priya_cs101_01)"
    },
    "session_title": {
      "type": "string",
      "description": "Descriptive title summarizing the educational scenario and interaction goal"
    },
    "synthetic_user_id": {
      "type": "string",
      "description": "Pseudonymous synthetic user identifier (e.g., syn_student_042)"
    },
    "authenticated_role": {
      "type": "string",
      "enum": ["Student", "Teaching Assistant", "Professor / Course Instructor", "Administrator"],
      "description": "Authoritative authenticated LMS role"
    },
    "user_profile": {
      "type": "object",
      "required": ["profile_id", "profile_name"],
      "properties": {
        "profile_id": { "type": "string", "example": "PROF_01" },
        "profile_name": { "type": "string", "example": "Autonomous Conceptualist" }
      }
    },
    "course_id": {
      "type": "string",
      "example": "CS101"
    },
    "resource_id": {
      "type": "string",
      "example": "RES_ASSIGNMENT_04"
    },
    "resource_type": {
      "type": "string",
      "example": "RES_ASSIGNMENT"
    },
    "resource_scope": {
      "type": "string",
      "enum": ["Personal", "Group", "Course", "Platform"]
    },
    "resource_lifecycle_state": {
      "type": "string",
      "enum": [
        "DRAFT",
        "PUBLISHED",
        "ACTIVE",
        "SUBMISSION_CLOSED",
        "GRADED",
        "RESULTS_RELEASED",
        "ARCHIVED"
      ]
    },
    "applicable_policy_ids": {
      "type": "array",
      "items": { "type": "string" },
      "example": ["POL_CEIL_005", "POL_SOL_007"]
    },
    "scenario_id": {
      "type": "string",
      "example": "SCEN_QUICKSORT_SLICING"
    },
    "source_provenance": {
      "type": "object",
      "required": ["provenance_category", "source_dataset", "transformation_type"],
      "properties": {
        "provenance_category": {
          "type": "string",
          "enum": ["real_source", "adapted_synthetic", "original_synthetic"]
        },
        "source_dataset": {
          "type": "string",
          "enum": ["StudyChat", "Eedi", "GeometryOfHarmfulness", "None"]
        },
        "source_record_id": {
          "type": ["string", "null"]
        },
        "source_label": {
          "type": ["string", "null"]
        },
        "transformation_type": {
          "type": "string",
          "example": "iterative_slicing_adaptation"
        },
        "adaptation_description": {
          "type": "string"
        }
      }
    },
    "session_summary": {
      "type": "string",
      "description": "Narrative summary of the multi-turn interaction trajectory"
    },
    "gold_auditor_label": {
      "type": "string",
      "enum": ["HARMLESS", "SUSPICIOUS", "POLICY-VIOLATING"],
      "description": "Ground-truth session trajectory evaluation"
    },
    "auditor_behaviour_tags": {
      "type": "array",
      "items": { "type": "string" },
      "example": ["iterative_slicing", "gradual_escalation"]
    },
    "dataset_split": {
      "type": "string",
      "enum": ["train", "validation", "test"]
    },
    "model_auditor_evaluation": {
      "type": ["object", "null"],
      "description": "Isolated container for model predictions; never overwrites gold fields",
      "properties": {
        "model_id": { "type": "string" },
        "model_auditor_prediction": {
          "type": "string",
          "enum": ["HARMLESS", "SUSPICIOUS", "POLICY-VIOLATING"]
        },
        "model_auditor_prediction_reason": { "type": "string" },
        "evaluation_timestamp": { "type": "string", "format": "date-time" }
      }
    },
    "turns": {
      "type": "array",
      "minItems": 1,
      "items": { "$ref": "#/$defs/TurnRecord" }
    }
  },
  "$defs": {
    "TurnRecord": {
      "type": "object",
      "required": [
        "turn_id",
        "turn_index",
        "user_request",
        "explicitly_requested_help_level",
        "inferred_requested_help_level",
        "permitted_help_ceiling",
        "current_resource_state",
        "applicable_policy_ids",
        "lms_permission_context",
        "browser_snapshot",
        "gold_guard_decision",
        "gold_guard_reason_codes",
        "reference_assistant_response",
        "actually_delivered_help_level"
      ],
      "properties": {
        "turn_id": { "type": "string", "pattern": "^turn_[0-9]+$" },
        "turn_index": { "type": "integer", "minimum": 1 },
        "user_request": { "type": "string" },
        "explicitly_requested_help_level": {
          "type": ["integer", "null"],
          "minimum": 0,
          "maximum": 6,
          "description": "Explicit level stated by user in prompt; null if unstated"
        },
        "inferred_requested_help_level": {
          "type": "integer",
          "minimum": 0,
          "maximum": 6,
          "description": "Level inferred by annotator from request semantics"
        },
        "permitted_help_ceiling": {
          "type": "integer",
          "minimum": 0,
          "maximum": 6,
          "description": "Maximum assistance level allowed by active policy"
        },
        "current_resource_state": {
          "type": "string",
          "enum": [
            "DRAFT",
            "PUBLISHED",
            "ACTIVE",
            "SUBMISSION_CLOSED",
            "GRADED",
            "RESULTS_RELEASED",
            "ARCHIVED"
          ]
        },
        "applicable_policy_ids": {
          "type": "array",
          "items": { "type": "string" }
        },
        "lms_permission_context": {
          "type": "object",
          "required": ["granted_permissions", "access_check_passed"],
          "properties": {
            "granted_permissions": {
              "type": "array",
              "items": { "type": "string" },
              "example": ["VIEW", "SUBMIT"]
            },
            "access_check_passed": { "type": "boolean" },
            "time_remaining_seconds": { "type": ["integer", "null"] }
          }
        },
        "browser_snapshot": {
          "type": "object",
          "required": [
            "snapshot_id",
            "capture_timestamp",
            "page_url",
            "capture_status",
            "raw_accessibility_tree"
          ],
          "properties": {
            "snapshot_id": { "type": "string" },
            "capture_timestamp": { "type": "string", "format": "date-time" },
            "page_url": { "type": "string" },
            "capture_status": { "type": "string", "enum": ["success", "truncated", "failed"] },
            "raw_accessibility_tree": {
              "type": "string",
              "description": "Serialized Playwright accessibility tree"
            },
            "viewport_dimensions": { "type": "string", "example": "1280x800" },
            "truncation_metadata": { "type": ["string", "null"] }
          }
        },
        "gold_guard_decision": {
          "type": "string",
          "enum": ["ALLOW", "LIMIT", "BLOCK", "ESCALATE"],
          "description": "Ground-truth Turn Guard decision"
        },
        "gold_guard_reason_codes": {
          "type": "array",
          "items": { "type": "string" },
          "example": ["LIMIT_SOCRATIC_HINT"]
        },
        "reference_assistant_response": {
          "type": "string",
          "description": "Gold benchmark response conforming to decision and permitted ceiling"
        },
        "actually_delivered_help_level": {
          "type": "integer",
          "minimum": 0,
          "maximum": 6,
          "description": "Exact help level embodied in the reference response"
        },
        "model_guard_evaluation": {
          "type": ["object", "null"],
          "description": "Isolated container for model predictions during benchmark evaluation",
          "properties": {
            "model_id": { "type": "string" },
            "model_guard_prediction": {
              "type": "string",
              "enum": ["ALLOW", "LIMIT", "BLOCK", "ESCALATE"]
            },
            "model_guard_prediction_reason": { "type": "string" },
            "predicted_help_ceiling": { "type": ["integer", "null"] },
            "inference_latency_ms": { "type": "number" }
          }
        }
      }
    }
  }
}
```
