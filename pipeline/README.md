# PROCTOR Synthesis, Validation & Analysis Pipeline

This directory contains the core reproducible scripts used to synthesize, validate, profile, and render the PROCTOR 2,000-session benchmark:

1. **`validation_harness.py`**: Automated validation harness enforcing the 13 quality assurance gates (including Gate 9: Zero-Leak verification, monotonicity checks, schema compliance, and Levenshtein de-duplication).
2. **`sample_pack_synthesis.py`**: Example staged batch synthesis script showing how raw StudyChat, Eedi, and GoH inputs are assembled into governed multi-turn sessions under explicit meta-prompts and policy cards.
3. **`merge_and_randomize_benchmark.py`**: Deterministic dataset compilation and randomization script generating the parallel dual corpora (`with_cua` and `no_cua`) under fixed seed 42.
4. **`analyze_benchmark_statistics.py`**: Comprehensive profiling script calculating label distributions, longitudinal turn dynamics, archetype quotas, and assistance hierarchy cross-tabulations.
5. **`generate_interactive_report.py`**: HTML dashboard generator producing the visual standalone benchmark audit report (`docs/guardslm_2000_benchmark_report.html`).
6. **`goh_academic_sampler.py`**: Sampler extracting multi-turn adversarial trajectories from the Geometry of Harmfulness benchmark.
7. **`lms_snapshot_service.py`**: CUA (Computer-Use Agent) DOM accessibility tree and LMS state telemetry generator.
8. **`generate_blog_charts.py`**: Script generating publication-grade vector (SVG) and raster (PNG) charts and Datawrapper CSV tables.
