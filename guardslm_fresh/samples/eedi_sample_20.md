# Eedi: Curated 20 Representative Test Cases for ChatGPT

> **Dataset**: Eedi Question-Anchored Human Tutoring Interventions
> **Domain**: K–12 & Diagnostic Mathematics, Misconception Diagnosis, Socratic Scaffolding

---

## Test Case `EEDI_0001`: Rounding to Decimal Places
- **Question ID**: `104614` | **Messages**: 41 (26 Student, 15 Tutor)
### Diagnostic Question Given to Student:
```text
Alex and Sophie are arguing about rounding 
Alex says \( \mathbf{5 . 4 5 9 8} \) rounded to \( 1 \) decimal place is \( \mathbf{5 . 5} \) 
Sophie says \( \mathbf{5 . 4 5 9 8} \) rounded to \( 2 \) decimal places is \( \mathbf{5 . 4 6} \) 
Who is correct?
```

### Human Tutor Interventions Transcript:

**[Human Tutor (Seq 1)]**:
Hello Lina, just wanted to check, you OK?

**[Human Tutor (Seq 2)]**:
You don't have to have help if you don't want it but I am here if you need anything.

**[Student (Seq 3)]**:
Hi I would you preferred to be called Lina Chen

**[Student (Seq 4)]**:
I need help

**[Student (Seq 5)]**:
On this question I am a bit stuck at this can you help me please

**[Student (Seq 6)]**:
Thx u

**[Human Tutor (Seq 7)]**:
Of course, thank you for correcting me on your name, give me a moment to have a look.

**[Student (Seq 8)]**:
Ok thank you take your time

**[Human Tutor (Seq 9)] _(Pedagogical Move: <Getting Student to Relate>)_**:
Do you have any thoughts about what either Alex or Sophie said?

**[Human Tutor (Seq 10)] _(Pedagogical Move: <Getting Student to Relate>)_**:
Do you think either of them is right or wrong?

**[Student (Seq 11)]**:
I think both are wrong

**[Student (Seq 12)]**:
Is that right ???

**[Human Tutor (Seq 13)] _(Pedagogical Move: <Getting Student to Relate>)_**:
OK. So if Alex is wrong, what do you think would be the right answer for his question?

**[Student (Seq 14)]**:
Both are wrong

**[Student (Seq 15)]**:
Or Sophie is correct

**[Human Tutor (Seq 16)] _(Pedagogical Move: <Press for Accuracy>)_**:
what do you think 5.4598 rounds to to 1dp?

**[Student (Seq 17)]**:
5.45

**[Student (Seq 18)]**:
Maybe or not sure

**[Human Tutor (Seq 19)]**:
That's two decimal places, not one.

**[Student (Seq 20)]**:
5.4510

**[Student (Seq 21)]**:
Can you give me a clue

**[Student (Seq 22)]**:
Please

**[Human Tutor (Seq 23)]**:
An answer to 1 decimal place should have only one digit after the decimal point.

**[Student (Seq 24)]**:
What do you mean by that

**[Human Tutor (Seq 25)] _(Pedagogical Move: <Keep Together>)_**:
Have you worked on rounding before?

**[Student (Seq 26)]**:
Yes

**[Human Tutor (Seq 27)] _(Pedagogical Move: <Press for Accuracy>)_**:
Can you round 5.45 to one decimal place?

**[Student (Seq 28)]**:
54.5

**[Human Tutor (Seq 29)] _(Pedagogical Move: <Revoicing>)_**:
No, the answer would be 5.5

**[Student (Seq 30)]**:
Oh I get it the now

**[Human Tutor (Seq 31)] _(Pedagogical Move: <Keep Together>)_**:
I think maybe you multiplied by ten, is that right?

**[Student (Seq 32)]**:
How does this work

**[Student (Seq 33)]**:
Because like 5.45 to one decimal should be the same no changes

**[Human Tutor (Seq 34)]**:
To 1 decimal place, it's 5.5

**[Student (Seq 35)]**:
Ok

**[Student (Seq 36)]**:
thank you so much

**[Student (Seq 37)]**:
Take care

**[Student (Seq 38)]**:
Enjoy the rest of your day

**[Student (Seq 39)]**:
So nice to speak to you

**[Human Tutor (Seq 40)] _(Pedagogical Move: <Keep Together>)_**:
You're welcome. would you like to talk about Sophie's answer too or would you like me to hand you back to the lesson?

**[Student (Seq 41)]**:
Hand me back to lesson thanks

---

## Test Case `EEDI_0002`: Place Value
- **Question ID**: `129129` | **Messages**: 32 (12 Student, 20 Tutor)
### Diagnostic Question Given to Student:
```text
What is the value of:
\(
\frac{54+58}{2}
\)
```

### Human Tutor Interventions Transcript:

**[Human Tutor (Seq 1)]**:
Hi Nathaniel, How are you today?

**[Student (Seq 2)]**:
im good, im not sure how to solve this

**[Human Tutor (Seq 3)]**:
good :) OK, let's have a look

**[Human Tutor (Seq 4)] _(Pedagogical Move: <Press for Accuracy>)_**:
What do you think this question is asking?

**[Student (Seq 5)]**:
the value of 54+58/2

**[Human Tutor (Seq 6)] _(Pedagogical Move: <Press for Accuracy>)_**:
super! what do you think we should do first?

**[Student (Seq 7)]**:
i think add 54 and 58?

**[Human Tutor (Seq 8)] _(Pedagogical Move: <Press for Accuracy>)_**:
Yes, I agree! what answer does that give?

**[Student (Seq 9)]**:
i think 114?

**[Human Tutor (Seq 10)]**:
not quite

**[Student (Seq 11)]**:
112

**[Human Tutor (Seq 12)]**:
Let's simplify... 54 = 50+4 and 58 = 50+8

**[Human Tutor (Seq 13)]**:
🎉🎉

**[Human Tutor (Seq 14)]**:
Great!!

**[Human Tutor (Seq 15)] _(Pedagogical Move: <Press for Accuracy>)_**:
Now, what is the final part of the question?

**[Student (Seq 16)]**:
we do something with the 2 and 112?

**[Human Tutor (Seq 17)] _(Pedagogical Move: <Revoicing>)_**:
so we have 112/2

**[Human Tutor (Seq 18)] _(Pedagogical Move: <Press for Accuracy>)_**:
what does that line mean?

**[Student (Seq 19)]**:
halve?

**[Human Tutor (Seq 20)]**:
well, the line with the 2 below it is a way of saying half

**[Human Tutor (Seq 21)]**:
but the line in the fraction, is another way of saying divide in Maths

**[Student (Seq 22)]**:
so we divide 112 by 2?

**[Human Tutor (Seq 23)]**:
That's it Nathaniel!! Well done!🎉😊

**[Human Tutor (Seq 24)] _(Pedagogical Move: <Press for Accuracy>)_**:
What answer will you get?

**[Student (Seq 25)]**:
56

**[Human Tutor (Seq 26)] _(Pedagogical Move: <Keep Together>)_**:
Super work Nathaniel! How do you feel about this now you've worked through it?

**[Student (Seq 27)]**:
very good

**[Human Tutor (Seq 28)]**:
👏🎉😊 well done, you've been super today!

**[Student (Seq 29)]**:
thanks for the help

**[Human Tutor (Seq 30)] _(Pedagogical Move: <Keep Together>)_**:
Are you ready to go back and submit your answer?

**[Student (Seq 31)]**:
yup

**[Human Tutor (Seq 32)]**:
No problem!😊

---

## Test Case `EEDI_0003`: Multiples and Lowest Common Multiple
- **Question ID**: `147113` | **Messages**: 34 (17 Student, 17 Tutor)
### Diagnostic Question Given to Student:
```text
Elijah makes a conjecture:
```

### Human Tutor Interventions Transcript:

**[Student (Seq 1)]**:
is it c

**[Human Tutor (Seq 2)]**:
Hi, another wordy one! One sec while I read it through.

**[Student (Seq 3)]**:
kkkkkkkkk

**[Human Tutor (Seq 4)] _(Pedagogical Move: <Press for Accuracy>)_**:
Ok think about an example... What's the lowest common multiply of 3 and 5?

**[Human Tutor (Seq 5)]**:
*multiple

**[Student (Seq 6)]**:
15

**[Human Tutor (Seq 7)] _(Pedagogical Move: <Keep Together>)_**:
Yep, do we get that by multiplying them together?

**[Student (Seq 8)]**:
45

**[Human Tutor (Seq 9)]**:
I mean multiplying 3 and 5 together gives us the lowest common multiple, 15

**[Student (Seq 10)]**:
oh so am i rigt or not

**[Human Tutor (Seq 11)]**:
For the question, we're trying to decide if multiplying numbers together gives us their lowest common multiple

**[Human Tutor (Seq 12)] _(Pedagogical Move: <Keep Together>)_**:
So did it work for 3 and 5?

**[Student (Seq 13)]**:
yes

**[Human Tutor (Seq 14)]**:
Great, so it works at least sometimes...

**[Student (Seq 15)]**:
is it b

**[Human Tutor (Seq 16)] _(Pedagogical Move: <Press for Reasoning>)_**:
Can you prove it?

**[Student (Seq 17)]**:
no

**[Human Tutor (Seq 18)] _(Pedagogical Move: <Press for Accuracy>)_**:
Is there an example where it doesn't work?

**[Student (Seq 19)]**:
i dont know

**[Student (Seq 20)]**:
d

**[Human Tutor (Seq 21)] _(Pedagogical Move: <Press for Accuracy>)_**:
Let's try... 4 and 6. What's the lowest common multiple?

**[Student (Seq 22)]**:
its d

**[Student (Seq 23)]**:
24

**[Student (Seq 24)]**:
12

**[Human Tutor (Seq 25)] _(Pedagogical Move: <Keep Together>)_**:
Yeah 12! Is that the same as multiplying 4 x 6?

**[Student (Seq 26)]**:
is it d

**[Human Tutor (Seq 27)]**:
Well it worked for 3 and 5, but not 4 and 6

**[Human Tutor (Seq 28)] _(Pedagogical Move: <Keep Together>)_**:
So that's sometimes, right?

**[Student (Seq 29)]**:
so b

**[Human Tutor (Seq 30)]**:
Yep. I just wanted you to see why!

**[Student (Seq 31)]**:
is it b then]

**[Human Tutor (Seq 32)] _(Pedagogical Move: <Revoicing>)_**:
Yes, B

**[Human Tutor (Seq 33)]**:
Bye!

**[Student (Seq 34)]**:
bye

---

## Test Case `EEDI_0004`: Averages and Range from Frequency Table
- **Question ID**: `108130` | **Messages**: 27 (7 Student, 20 Tutor)
### Diagnostic Question Given to Student:
```text
The table shows the numbers of TVs in the households of students in a different class.

What is the range for the number of TVs?
```

### Human Tutor Interventions Transcript:

**[Human Tutor (Seq 1)]**:
Hi Liam!

**[Student (Seq 2)]**:
Hi again

**[Human Tutor (Seq 3)]**:
So, the range is...

**[Human Tutor (Seq 4)]**:
the largest value minus the smallest value

**[Human Tutor (Seq 5)]**:
But we need to think what the data is about...

**[Human Tutor (Seq 6)]**:
it's about number of TVs

**[Human Tutor (Seq 7)]**:
So, we need to look at the highest and lowest number of TVs

**[Student (Seq 8)]**:
Would that be 4 and 2?

**[Student (Seq 9)]**:
Wait 0

**[Human Tutor (Seq 10)]**:
Have another look...

**[Human Tutor (Seq 11)]**:
At least one person has to have given that answer...

**[Human Tutor (Seq 12)]**:
otherwise that number of TVs doesn't exist in this survey really...

**[Student (Seq 13)]**:
So 4 and 2?

**[Human Tutor (Seq 14)] _(Pedagogical Move: <Revoicing>)_**:
4 is correct...

**[Human Tutor (Seq 15)] _(Pedagogical Move: <Keep Together>)_**:
but some people have 1 Tv... can you see those 7 people who have 1 TV?

**[Student (Seq 16)]**:
Yes

**[Human Tutor (Seq 17)]**:
Great...

**[Human Tutor (Seq 18)]**:
so the largest number of TVs is 4

**[Human Tutor (Seq 19)]**:
And the lowest number of TVs that anyone has is 1.

**[Human Tutor (Seq 20)]**:
So, the range = 4-1

**[Human Tutor (Seq 21)] _(Pedagogical Move: <Press for Accuracy>)_**:
= ?

**[Student (Seq 22)]**:
Ohh 3

**[Human Tutor (Seq 23)]**:
Great!

**[Human Tutor (Seq 24)] _(Pedagogical Move: <Keep Together>)_**:
Does this all make sense?

**[Student (Seq 25)]**:
Yes thankyou

**[Human Tutor (Seq 26)]**:
Great!

**[Human Tutor (Seq 27)]**:
Well done! Bye for now 👋

---

## Test Case `EEDI_0005`: Rounding to Decimal Places
- **Question ID**: `104615` | **Messages**: 25 (7 Student, 18 Tutor)
### Diagnostic Question Given to Student:
```text
What is \( \mathbf{3 . 1 5 3} \) rounded to the nearest \( \mathbf{0 . 0 2} \) ?
```

### Human Tutor Interventions Transcript:

**[Human Tutor (Seq 1)]**:
Hi again Zainab  😁👋

**[Human Tutor (Seq 2)] _(Pedagogical Move: <Keep Together>)_**:
How can I help?!

**[Student (Seq 3)]**:
I don't know how to work out this question.

**[Human Tutor (Seq 4)]**:
So for this one we need to think about the 0.02 times table values near 3.153 😃

**[Human Tutor (Seq 5)] _(Pedagogical Move: <Press for Accuracy>)_**:
Can you think about what value would be in the 0.02 times table near 3.153.. Any ideas? 💡

**[Student (Seq 6)]**:
What is the 0.02 times table value?

**[Human Tutor (Seq 7)]**:
I'll give you the value below, see if you can find the value above..

**[Human Tutor (Seq 8)]**:
So the value in the 0.02 times table below 3.153 would be 3.14

**[Human Tutor (Seq 9)] _(Pedagogical Move: <Keep Together>)_**:
Does that make sense? 😊👍

**[Student (Seq 10)]**:
I think so

**[Human Tutor (Seq 11)] _(Pedagogical Move: <Press for Accuracy>)_**:
So what would the value above 3.153 be in the 0.02 times table? 🧠

**[Human Tutor (Seq 12)] _(Pedagogical Move: <Press for Accuracy>)_**:
3.1 to 3.12 to 3.14 to ...

**[Student (Seq 13)]**:
3.16

**[Human Tutor (Seq 14)]**:
Nailed it 🔨🔨🔨

**[Human Tutor (Seq 15)] _(Pedagogical Move: <Press for Accuracy>)_**:
So now we need to decide if 3.153 is closer to 3.14 or 3.16

**[Human Tutor (Seq 16)] _(Pedagogical Move: <Press for Accuracy>)_**:
Can you work that out? 😃

**[Student (Seq 17)]**:
3.16 ia closer

**[Human Tutor (Seq 18)]**:
Exactly so that's your answer ✅✅✅

**[Human Tutor (Seq 19)] _(Pedagogical Move: <Revoicing>)_**:
3.153 rounded to the nearest 0.02 is 3.16 😁😁😁

**[Human Tutor (Seq 20)]**:
WELL DONE!!! 🏆😊✅👌👀🧠

**[Student (Seq 21)]**:
Thank you! This really helped. 😁

**[Human Tutor (Seq 22)]**:
So pleased to hear 😃👍

**[Human Tutor (Seq 23)]**:
Ready to go back to eedi? 🤖

**[Student (Seq 24)]**:
Yes.

**[Human Tutor (Seq 25)]**:
Of course! Nice one for requesting help 😊👍 bye for now 👋👋👋

---

## Test Case `EEDI_0006`: Multiplying and Dividing Negative Numbers
- **Question ID**: `89558` | **Messages**: 20 (8 Student, 12 Tutor)
### Diagnostic Question Given to Student:
```text
Statement 1: \( \quad p \times(-q)=(-p) \times q \)
Statement 2: \( \quad-(q)^{2}=q^{2} \)
What can you say about the above statements, where \( p \) and \( q \) represent different numbers?
```

### Human Tutor Interventions Transcript:

**[Human Tutor (Seq 1)] _(Pedagogical Move: <Keep Together>)_**:
Hi How can I help?

**[Student (Seq 2)]**:
I’m a bit confused with this question

**[Human Tutor (Seq 3)]**:
Ok, let's take a look together!

**[Human Tutor (Seq 4)] _(Pedagogical Move: <Press for Accuracy>)_**:
So, what is p x - q?

**[Student (Seq 5)]**:
Um well I know it would be a negative but I don’t really know the answer

**[Human Tutor (Seq 6)] _(Pedagogical Move: <Revoicing>)_**:
That's what we need really, so it would be -pq

**[Human Tutor (Seq 7)]**:
As if we multiply two letters we write them next to each other

**[Student (Seq 8)]**:
Ok

**[Human Tutor (Seq 9)] _(Pedagogical Move: <Keep Together>)_**:
Does -p x q give us the same answer?

**[Student (Seq 10)]**:
Yes

**[Human Tutor (Seq 11)]**:
Great, so statement 1 is true

**[Student (Seq 12)]**:
Ok

**[Human Tutor (Seq 13)]**:
Now statement 2

**[Student (Seq 14)]**:
I don’t think it works

**[Human Tutor (Seq 15)] _(Pedagogical Move: <Revoicing>)_**:
I don't think it does either, as the left one stays negative, but the right one is positive

**[Human Tutor (Seq 16)] _(Pedagogical Move: <Press for Accuracy>)_**:
So which answer do you think we need?

**[Student (Seq 17)]**:
A

**[Human Tutor (Seq 18)]**:
I agree!

**[Human Tutor (Seq 19)]**:
Well done Sophia :)

**[Student (Seq 20)]**:
Ok thank you

---

## Test Case `EEDI_0007`: Prime Numbers and Prime Factors
- **Question ID**: `103042` | **Messages**: 24 (8 Student, 16 Tutor)
### Diagnostic Question Given to Student:
```text
Which is the next prime number greater than \( 100 ? \)
```

### Human Tutor Interventions Transcript:

**[Human Tutor (Seq 1)] _(Pedagogical Move: <Keep Together>)_**:
Hey! How can I help? 😃

**[Student (Seq 2)]**:
I don't know my prime numbers past 40

**[Human Tutor (Seq 3)] _(Pedagogical Move: <Press for Accuracy>)_**:
No worries, what do you know about prime numbers?

**[Student (Seq 4)]**:
They can only be divided by one and Itself

**[Human Tutor (Seq 5)]**:
perfect!

**[Human Tutor (Seq 6)] _(Pedagogical Move: <Press for Accuracy>)_**:
So looking at the answer options, is there any that you know can be divided by something other than 1 or itself?

**[Human Tutor (Seq 7)] _(Pedagogical Move: <Press for Accuracy>)_**:
Is there one that you could rule out?

**[Student (Seq 8)]**:
103

**[Human Tutor (Seq 9)] _(Pedagogical Move: <Press for Accuracy>)_**:
What can you divided 103 by to get a whole number answer?

**[Human Tutor (Seq 10)]**:
*divide

**[Student (Seq 11)]**:
6

**[Human Tutor (Seq 12)]**:
103/6 = 17.1666...

**[Human Tutor (Seq 13)]**:
103 is actually prime.

**[Human Tutor (Seq 14)]**:
I was thinking we could rule out 105 as it ends in a 5

**[Student (Seq 15)]**:
Yes

**[Human Tutor (Seq 16)] _(Pedagogical Move: <Press for Reasoning>)_**:
Why can we rule it out as it ends in a 5?

**[Student (Seq 17)]**:
Because 5 is in the 5 times tables

**[Human Tutor (Seq 18)]**:
Brilliant!

**[Human Tutor (Seq 19)] _(Pedagogical Move: <Press for Accuracy>)_**:
What about 101?

**[Student (Seq 20)]**:
101 is the answer to the question

**[Human Tutor (Seq 21)]**:
It is, fantastic!

**[Human Tutor (Seq 22)] _(Pedagogical Move: <Keep Together>)_**:
Happy to go back to the lesson?

**[Student (Seq 23)]**:
Yes

**[Human Tutor (Seq 24)]**:
😁👋

---

## Test Case `EEDI_0008`: Solving Linear Inequalities
- **Question ID**: `106909` | **Messages**: 32 (15 Student, 17 Tutor)
### Diagnostic Question Given to Student:
```text
Leo and Sophie are arguing about solving inequalities.
Leo says \( -2 m>12 \) gives \( m>-6 \)
Sophie says \( -2+m>12 \) gives \( m>14 \)
Who is correct?
```

### Human Tutor Interventions Transcript:

**[Human Tutor (Seq 1)]**:
Hello :)

**[Student (Seq 2)]**:
hi im really confused on this question

**[Student (Seq 3)]**:
an you help me please

**[Human Tutor (Seq 4)]**:
of course!

**[Student (Seq 5)]**:
ok

**[Human Tutor (Seq 6)] _(Pedagogical Move: <Press for Accuracy>)_**:
So we need to work out -2m > 12 first, how can we do that? :)

**[Student (Seq 7)]**:
find out what m is

**[Human Tutor (Seq 8)] _(Pedagogical Move: <Revoicing>)_**:
Exactly, so m is being multiplied by -2

**[Human Tutor (Seq 9)] _(Pedagogical Move: <Press for Accuracy>)_**:
So we need to do the opposite, which is?

**[Student (Seq 10)]**:
divide by -2

**[Human Tutor (Seq 11)]**:
Super :)

**[Human Tutor (Seq 12)] _(Pedagogical Move: <Press for Accuracy>)_**:
What does that give us ? :0

**[Student (Seq 13)]**:
thank you what would i do next

**[Student (Seq 14)]**:
would it be -1

**[Human Tutor (Seq 15)] _(Pedagogical Move: <Revoicing>)_**:
Not quite, we need to do -6 divided by -2

**[Student (Seq 16)]**:
3

**[Human Tutor (Seq 17)]**:
Super :

**[Human Tutor (Seq 18)]**:
:)

**[Student (Seq 19)]**:
:)

**[Human Tutor (Seq 20)]**:
Now there's one other thing we need to do when we divide by negatives if we use inequalities, we have to flip the inequality sign around :)

**[Student (Seq 21)]**:
ok

**[Human Tutor (Seq 22)] _(Pedagogical Move: <Press for Accuracy>)_**:
So what does that mean our inequality will be? :)

**[Student (Seq 23)]**:
would it be leos

**[Human Tutor (Seq 24)] _(Pedagogical Move: <Revoicing>)_**:
Yep it is Leo's that we're doing :)

**[Student (Seq 25)]**:
sorry im still confused on how i know whether it is sophies or leoms or sophies and leos

**[Human Tutor (Seq 26)] _(Pedagogical Move: <Revoicing>)_**:
Ok, so Leo and Sophie both have different questions

**[Student (Seq 27)]**:
oh wait i think i know

**[Student (Seq 28)]**:
is the answer B

**[Human Tutor (Seq 29)]**:
It is :)

**[Student (Seq 30)]**:
thank you for your help claire

**[Human Tutor (Seq 31)]**:
I'll let you pop that in. Please take the lesson offered after you put in your answer, it will really help 😊

**[Human Tutor (Seq 32)]**:
You're welcome! :)

---

## Test Case `EEDI_0009`: Surface Area of Prisms
- **Question ID**: `131463` | **Messages**: 26 (17 Student, 9 Tutor)
### Diagnostic Question Given to Student:
```text
What is the volume of this cuboid?
```

### Human Tutor Interventions Transcript:

**[Student (Seq 1)]**:
what is the answer

**[Human Tutor (Seq 2)] _(Pedagogical Move: <Keep Together>)_**:
Hi! Can you see the feedback tells you which calculation to use?

**[Student (Seq 3)]**:
i dont get it

**[Student (Seq 4)]**:
what feedback

**[Student (Seq 5)]**:
???#

**[Student (Seq 6)]**:
???

**[Student (Seq 7)]**:
i did the area

**[Student (Seq 8)]**:
add all the side areas

**[Human Tutor (Seq 9)] _(Pedagogical Move: <Revoicing>)_**:
D ❌ - I think you have found the surface area. Remember we multiply the length by the width by the height to find the volume of a cuboid

**[Human Tutor (Seq 10)]**:
This question wants the volume not the area :)

**[Student (Seq 11)]**:
I know its not D

**[Student (Seq 12)]**:
oh ok

**[Student (Seq 13)]**:
what is volume is it sound

**[Human Tutor (Seq 14)] _(Pedagogical Move: <Revoicing>)_**:
Volume is the space inside

**[Student (Seq 15)]**:
what is the space inside please

**[Human Tutor (Seq 16)]**:
Like if you filled the shape with clay, how much clay could you fit inside

**[Student (Seq 17)]**:
how do you work it out

**[Student (Seq 18)]**:
on this question

**[Human Tutor (Seq 19)]**:
That's what the feedback tells you :) the ones I copied, it says multiply the length by the width by the height to find the volume

**[Student (Seq 20)]**:
10 X 5 is 50

**[Human Tutor (Seq 21)] _(Pedagogical Move: <Press for Accuracy>)_**:
Good, and x4?

**[Student (Seq 22)]**:
200

**[Student (Seq 23)]**:
so is it c

**[Human Tutor (Seq 24)] _(Pedagogical Move: <Keep Together>)_**:
Great, that is correct :) Good to go?

**[Student (Seq 25)]**:
bye thanks for your help

**[Human Tutor (Seq 26)]**:
Bye!

---

## Test Case `EEDI_0010`: Time
- **Question ID**: `75997` | **Messages**: 24 (7 Student, 17 Tutor)
### Diagnostic Question Given to Student:
```text
Which clock shows ten to twelve at night?
```

### Human Tutor Interventions Transcript:

**[Human Tutor (Seq 1)]**:
Hi again :)

**[Student (Seq 2)]**:
hello srry to disturb

**[Human Tutor (Seq 3)]**:
No need to apologise!

**[Student (Seq 4)]**:
i need help on this question

**[Human Tutor (Seq 5)]**:
You went for A, which is 12 minutes past 10

**[Human Tutor (Seq 6)] _(Pedagogical Move: <Press for Accuracy>)_**:
What time does B show?

**[Student (Seq 7)]**:
12 minute past 50

**[Student (Seq 8)]**:
50 minutes past 12

**[Human Tutor (Seq 9)] _(Pedagogical Move: <Revoicing>)_**:
Yes brilliant, 50 minutes past 12

**[Human Tutor (Seq 10)]**:
which is 12 minutes to 1

**[Human Tutor (Seq 11)]**:
Sorry 10 minutes to 1**

**[Human Tutor (Seq 12)]**:
Which isn't what we are looking

**[Human Tutor (Seq 13)] _(Pedagogical Move: <Press for Accuracy>)_**:
how about C?

**[Student (Seq 14)]**:
its 12 : 50 AM

**[Human Tutor (Seq 15)]**:
Excellent! so 10 to 1 again

**[Human Tutor (Seq 16)]**:
So it isn't A, B or C!

**[Human Tutor (Seq 17)] _(Pedagogical Move: <Press for Accuracy>)_**:
How about D? :)

**[Student (Seq 18)]**:
is it D?

**[Human Tutor (Seq 19)] _(Pedagogical Move: <Revoicing>)_**:
D shows 10 to 12 at night-time, so yes, 10 to 12 at night :)

**[Human Tutor (Seq 20)]**:
Super work!

**[Human Tutor (Seq 21)]**:
Well done ⭐⭐⭐⭐⭐

**[Human Tutor (Seq 22)] _(Pedagogical Move: <Keep Together>)_**:
Are you ok to return to the lesson now?

**[Student (Seq 23)]**:
will i get 100  coins this time>

**[Human Tutor (Seq 24)]**:
Sure thing

---

## Test Case `EEDI_0011`: Direct Proportion
- **Question ID**: `131361` | **Messages**: 45 (21 Student, 24 Tutor)
### Diagnostic Question Given to Student:
```text
Liam and Sophie are discussing similar shapes
```

### Human Tutor Interventions Transcript:

**[Student (Seq 1)]**:
hi again...

**[Human Tutor (Seq 2)] _(Pedagogical Move: <Keep Together>)_**:
Hi Julian :)
How can I help?

**[Student (Seq 3)]**:
iam stuck in this question

**[Human Tutor (Seq 4)]**:
No problem, let's take a lool

**[Human Tutor (Seq 5)]**:
*look!

**[Student (Seq 6)]**:
okay

**[Human Tutor (Seq 7)] _(Pedagogical Move: <Press for Accuracy>)_**:
Do you know what 'similar shapes' are?

**[Student (Seq 8)]**:
yeah i guess it like shapes that have the same perimeter and area i guess

**[Human Tutor (Seq 9)] _(Pedagogical Move: <Revoicing>)_**:
Great idea, but not quite!

Similar shapes have all the same angles and proportions, but they are enlargements of each other

**[Student (Seq 10)]**:
oyh

**[Human Tutor (Seq 11)]**:
So for example if I had a triangle with sides lengths, 1cm, 2cm, 3cm

**[Human Tutor (Seq 12)]**:
And another with side lengths 10cm, 20cm, 30cm

**[Student (Seq 13)]**:
yes

**[Human Tutor (Seq 14)]**:
As long as they also had the same angles then they will be similar. One is just 10 times bigger than the other

**[Human Tutor (Seq 15)] _(Pedagogical Move: <Keep Together>)_**:
So take another look at the question. Can you spot a pattern like that with any of the lengths?

**[Student (Seq 16)]**:
so i am trying to think and i think its is c

**[Student (Seq 17)]**:
C

**[Human Tutor (Seq 18)] _(Pedagogical Move: <Press for Accuracy>)_**:
What's the pattern between Liam's triangles?

**[Student (Seq 19)]**:
both has the same angle and the have 5,5 and 6,6

**[Student (Seq 20)]**:
i gues

**[Student (Seq 21)]**:
i guess

**[Human Tutor (Seq 22)]**:
Ah, all 3 sides will have to be in the same proportion, not just 2

**[Student (Seq 23)]**:
oh the shape also

**[Human Tutor (Seq 24)]**:
Now Liam has added 1cm to all the lengths to get from the first triangle to the second, but that doesn't keep them in proportion

**[Student (Seq 25)]**:
right

**[Human Tutor (Seq 26)]**:
We need to MULTIPLY  all the lengths by the same scale factor like I did in my example (x10)

**[Student (Seq 27)]**:
so the answer is C right

**[Human Tutor (Seq 28)] _(Pedagogical Move: <Press for Accuracy>)_**:
Take a look at Sophie's triangle. Is there anything you can multiply the lengths of the first triangle by to get the lengths in the second triangle?

**[Human Tutor (Seq 29)] _(Pedagogical Move: <Revoicing>)_**:
Not C - we have just shown that Liam's triangles are not similar

**[Student (Seq 30)]**:
oh ok

**[Student (Seq 31)]**:
only liam is correct

**[Human Tutor (Seq 32)] _(Pedagogical Move: <Revoicing>)_**:
Not quite. Liam is NOT correct, as his triangles are NOT similar

**[Human Tutor (Seq 33)]**:
Let's go through Sophie's together

**[Human Tutor (Seq 34)]**:
Her first triangle has lengths of:
4cm, 5cm, 6cm

**[Human Tutor (Seq 35)]**:
Her second triangle has lengths of:
2cm, 2.5cm, 3cm

**[Human Tutor (Seq 36)] _(Pedagogical Move: <Press for Accuracy>)_**:
Do you notice a pattern between those 2 sets of lengths?

**[Student (Seq 37)]**:
yes i do

**[Student (Seq 38)]**:
now i know the answer is B

**[Human Tutor (Seq 39)]**:
Super! Because in Sophie's we can multiply all the lengths in the smaller triangle by 2 to get the larger triangle

**[Human Tutor (Seq 40)]**:
So they are similar :)

**[Student (Seq 41)]**:
YAY i guess i worked out

**[Student (Seq 42)]**:
thanks

**[Human Tutor (Seq 43)]**:
It seems like this is a new topic for you so I'd recommend clicking on the "more practice" button when offered so that you get the help videos on this

**[Student (Seq 44)]**:
okay

**[Human Tutor (Seq 45)]**:
Great! Have a good day :)

---

## Test Case `EEDI_0012`: Function Machines
- **Question ID**: `147373` | **Messages**: 30 (8 Student, 22 Tutor)
### Diagnostic Question Given to Student:
```text
Liam and Emma are discussing this function machine
```

### Human Tutor Interventions Transcript:

**[Human Tutor (Seq 1)] _(Pedagogical Move: <Keep Together>)_**:
Hi! How can I help?

**[Student (Seq 2)]**:
I’m not sure on how to solve this as I find questions like this hard

**[Human Tutor (Seq 3)]**:
So if we start with m + 2. Liam says we +2m

**[Human Tutor (Seq 4)] _(Pedagogical Move: <Press for Accuracy>)_**:
what would m + 2 + 2m be?

**[Student (Seq 5)]**:
4m

**[Human Tutor (Seq 6)]**:
Ooh not quite

**[Human Tutor (Seq 7)] _(Pedagogical Move: <Press for Accuracy>)_**:
We could add the m and the 2m? What would that get? Remember what number is technically in front of the m by itself

**[Student (Seq 8)]**:
I’m not sure

**[Human Tutor (Seq 9)]**:
That's okay

**[Human Tutor (Seq 10)]**:
So if we've got m that's the same as 1m

**[Human Tutor (Seq 11)] _(Pedagogical Move: <Keep Together>)_**:
Are you happy with that?

**[Student (Seq 12)]**:
Yes

**[Human Tutor (Seq 13)] _(Pedagogical Move: <Press for Accuracy>)_**:
Brill so we've got 1m +2m What does that get?

**[Student (Seq 14)]**:
3m

**[Human Tutor (Seq 15)]**:
Perfect

**[Human Tutor (Seq 16)]**:
And then we have +2 left over so it's 3m + 2. We cannot simplify that

**[Human Tutor (Seq 17)]**:
So Liam is correct

**[Human Tutor (Seq 18)]**:
Now to check emma

**[Human Tutor (Seq 19)] _(Pedagogical Move: <Press for Accuracy>)_**:
(m + 2) x 3 What does that equal?

**[Student (Seq 20)]**:
6m?

**[Human Tutor (Seq 21)]**:
Remember you can't add letters and numbers together

**[Human Tutor (Seq 22)]**:
So we've got to multiply those separately. m x 3

**[Human Tutor (Seq 23)] _(Pedagogical Move: <Press for Accuracy>)_**:
2 x 3?

**[Student (Seq 24)]**:
6

**[Human Tutor (Seq 25)] _(Pedagogical Move: <Press for Accuracy>)_**:
and then m x3?

**[Student (Seq 26)]**:
3m

**[Human Tutor (Seq 27)]**:
Perfect

**[Human Tutor (Seq 28)] _(Pedagogical Move: <Revoicing>)_**:
3m + 6

**[Human Tutor (Seq 29)]**:
So only Liam is correct

**[Human Tutor (Seq 30)]**:
I'll leave you to put your answer in

---

## Test Case `EEDI_0013`: Adding and Subtracting Negative Numbers
- **Question ID**: `89436` | **Messages**: 31 (14 Student, 17 Tutor)
### Diagnostic Question Given to Student:
```text
Number line with two arrows, one labelled -3 and one labelled with the letter a, going from 4 to -5 on the number line.
```

### Human Tutor Interventions Transcript:

**[Student (Seq 1)]**:
hi

**[Human Tutor (Seq 2)]**:
Hi this is Leo one of the tutors at Eedi

**[Human Tutor (Seq 3)] _(Pedagogical Move: <Keep Together>)_**:
How can I help?

**[Student (Seq 4)]**:
👋 this question

**[Human Tutor (Seq 5)]**:
No worries, let me just take a quick look at it 👍

**[Student (Seq 6)]**:
😀this is my first time with you

**[Student (Seq 7)]**:
I know that you are a good tutor

**[Human Tutor (Seq 8)] _(Pedagogical Move: <Press for Accuracy>)_**:
So, we are start at 4 and go back 3 spaces, what number do we get to?

**[Student (Seq 9)]**:
1

**[Human Tutor (Seq 10)]**:
👍

**[Human Tutor (Seq 11)] _(Pedagogical Move: <Press for Accuracy>)_**:
How do we get from 1 to -5?

**[Student (Seq 12)]**:
and we minus 4 from it ?

**[Human Tutor (Seq 13)] _(Pedagogical Move: <Revoicing>)_**:
Not quite, if we are at 1 and minus 4 we would get to -3, we want to get to -5

**[Human Tutor (Seq 14)]**:
From 1 we could minus 1 and that would get us to 0

**[Human Tutor (Seq 15)] _(Pedagogical Move: <Press for Accuracy>)_**:
How many would we have to take away to get from 0 to -5?

**[Student (Seq 16)]**:
5 steps backwards

**[Human Tutor (Seq 17)]**:
👍

**[Student (Seq 18)]**:
so it is c

**[Human Tutor (Seq 19)] _(Pedagogical Move: <Press for Accuracy>)_**:
So altogether how many steps backwards do we need to take to get from 1 to -5?

**[Student (Seq 20)]**:
4

**[Student (Seq 21)]**:
thank you😄

**[Human Tutor (Seq 22)] _(Pedagogical Move: <Revoicing>)_**:
Not quite, going 4 back only gets us to -3 because we would go from 1 to 0 then to -1, -2 and -3

**[Human Tutor (Seq 23)]**:
We want to get to -5

**[Student (Seq 24)]**:
5 steps backwards

**[Student (Seq 25)]**:
i mean b is the answer

**[Human Tutor (Seq 26)] _(Pedagogical Move: <Revoicing>)_**:
Perfect, b would be the answer

**[Human Tutor (Seq 27)]**:
We would need to go 6 back in total

**[Human Tutor (Seq 28)]**:
I will pass you back to the bot so you can type in  the answer

**[Student (Seq 29)]**:
bye👋👋

**[Student (Seq 30)]**:
😘

**[Human Tutor (Seq 31)]**:
Don't forget to take the lesson if you would like some more practice, keep up the good work

---

## Test Case `EEDI_0014`: Linear Sequences (nth term)
- **Question ID**: `147255` | **Messages**: 26 (10 Student, 16 Tutor)
### Diagnostic Question Given to Student:
```text
Which sequence matches this graph?
```

### Human Tutor Interventions Transcript:

**[Student (Seq 1)]**:
Hi Lila

**[Human Tutor (Seq 2)]**:
Hi Cassandra 😁👋

**[Human Tutor (Seq 3)] _(Pedagogical Move: <Keep Together>)_**:
How can I help?!

**[Student (Seq 4)]**:
i don’t understand the question or the graph

**[Human Tutor (Seq 5)]**:
OK so the graph gives the position and value of the term 😁👌

**[Human Tutor (Seq 6)] _(Pedagogical Move: <Press for Accuracy>)_**:
So in position 1 what is the value of the term? 👀

**[Student (Seq 7)]**:
4?

**[Human Tutor (Seq 8)] _(Pedagogical Move: <Revoicing>)_**:
Brilliant so the first term in the sequence needs to have 4 things in it 😃👌

**[Human Tutor (Seq 9)] _(Pedagogical Move: <Press for Accuracy>)_**:
What about term 2?

**[Student (Seq 10)]**:
7

**[Human Tutor (Seq 11)]**:
FANTASTIC WORKING OUT 😃🏆👍💥⭐😊😁✅

**[Human Tutor (Seq 12)] _(Pedagogical Move: <Keep Together>)_**:
So can you see a sequence from A, B, C and D that has 4 in its first term and 7 in the second?!

**[Student (Seq 13)]**:
No

**[Human Tutor (Seq 14)]**:
Top tip, count the sticks...

**[Student (Seq 15)]**:
Ohhh

**[Student (Seq 16)]**:
C

**[Student (Seq 17)]**:
??

**[Human Tutor (Seq 18)]**:
Nailed it 🔨🔨🔨

**[Human Tutor (Seq 19)]**:
WELL DONE!!! 🏆😊✅👌👀🧠😁👌

**[Human Tutor (Seq 20)] _(Pedagogical Move: <Keep Together>)_**:
Does this question make more sense now? 😊

**[Student (Seq 21)]**:
Yeah 😊😊

**[Human Tutor (Seq 22)]**:
Awesome to hear! 👂

**[Human Tutor (Seq 23)]**:
Ready to go back to eedi? 🤖

**[Student (Seq 24)]**:
Yeah x

**[Human Tutor (Seq 25)]**:
Excellent ✅

**[Human Tutor (Seq 26)]**:
Bye for now 👋👋👋

---

## Test Case `EEDI_0015`: Simplifying and Equivalent Ratios
- **Question ID**: `101404` | **Messages**: 48 (18 Student, 30 Tutor)
### Diagnostic Question Given to Student:
```text
Lee and Drew are arguing about equivalent ratios.
Lee says \( 4: 14 \) is equivalent to \( 1: 3.5 \)
Drew says \( 4: 14 \) is equivalent to \( 6: 21 \)
Who is correct?
```

### Human Tutor Interventions Transcript:

**[Human Tutor (Seq 1)]**:
HI this is Alex one of the tutors at Eedi

**[Human Tutor (Seq 2)]**:
How can I help?

**[Student (Seq 3)]**:
every qestion makes no sense

**[Student (Seq 4)]**:
*question

**[Human Tutor (Seq 5)]**:
Did you watch the teach videos?

**[Student (Seq 6)]**:
yes :p

**[Human Tutor (Seq 7)]**:
Good

**[Human Tutor (Seq 8)] _(Pedagogical Move: <Press for Accuracy>)_**:
How do I simplify the ratio 4:14?

**[Student (Seq 9)]**:
2:7

**[Student (Seq 10)]**:
?

**[Human Tutor (Seq 11)]**:
👍

**[Human Tutor (Seq 12)] _(Pedagogical Move: <Keep Together>)_**:
Is 2:7 equivalent to 1:3.5?

**[Student (Seq 13)]**:
no?

**[Human Tutor (Seq 14)] _(Pedagogical Move: <Press for Accuracy>)_**:
How do we get from 2 to 1 using multiplication/ division?

**[Student (Seq 15)]**:
divide by 2?

**[Human Tutor (Seq 16)]**:
👍

**[Human Tutor (Seq 17)] _(Pedagogical Move: <Press for Accuracy>)_**:
What is 7 divided by 2?

**[Student (Seq 18)]**:
2.5

**[Human Tutor (Seq 19)]**:
Not quite

**[Human Tutor (Seq 20)] _(Pedagogical Move: <Keep Together>)_**:
6 divided by 2 is three, so it must be bigger than 3

**[Student (Seq 21)]**:
3.5

**[Human Tutor (Seq 22)]**:
Perfect

**[Human Tutor (Seq 23)]**:
So 2:7 will be equivalent to 1:3.5 as both parts if the ratio have been divided by 2

**[Human Tutor (Seq 24)] _(Pedagogical Move: <Keep Together>)_**:
Is 2:7 equivalent to 6:21?

**[Student (Seq 25)]**:
no?

**[Human Tutor (Seq 26)] _(Pedagogical Move: <Press for Accuracy>)_**:
Think about what we would have to multiply 2 and 7 by to get 6 and 21

**[Human Tutor (Seq 27)] _(Pedagogical Move: <Keep Together>)_**:
Is it the same number?

**[Student (Seq 28)]**:
no

**[Student (Seq 29)]**:
?

**[Human Tutor (Seq 30)] _(Pedagogical Move: <Press for Accuracy>)_**:
2x ? = 6

**[Student (Seq 31)]**:
3

**[Human Tutor (Seq 32)] _(Pedagogical Move: <Press for Accuracy>)_**:
7x?=21

**[Student (Seq 33)]**:
3

**[Human Tutor (Seq 34)]**:
Excellent

**[Human Tutor (Seq 35)]**:
Both parts of the ratio 2:7 have been multiplied by 3 to give 6:21 this means they are equivalent

**[Student (Seq 36)]**:
ok ( :p

**[Human Tutor (Seq 37)]**:
So, we can use all this to see who is correct Lee, Drew, both or neither

**[Human Tutor (Seq 38)] _(Pedagogical Move: <Press for Accuracy>)_**:
What do you think?

**[Student (Seq 39)]**:
is drew correct?

**[Human Tutor (Seq 40)]**:
Drew is correct

**[Human Tutor (Seq 41)] _(Pedagogical Move: <Getting Student to Relate>)_**:
What about Lee?

**[Student (Seq 42)]**:
no?

**[Human Tutor (Seq 43)]**:
Remember we said 4:14 = 2:7

**[Human Tutor (Seq 44)]**:
and 2:7 = 1:3.5

**[Student (Seq 45)]**:
yes he is correct

**[Human Tutor (Seq 46)]**:
As both parts of the ratio had been divided by 2

**[Human Tutor (Seq 47)]**:
Great.

**[Human Tutor (Seq 48)] _(Pedagogical Move: <Press for Accuracy>)_**:
So which option is the correct one?

---

## Test Case `EEDI_0016`: Expanding Single Brackets
- **Question ID**: `77771` | **Messages**: 34 (15 Student, 19 Tutor)
### Diagnostic Question Given to Student:
```text
Expand \( 4(3 c+2) \)
```

### Human Tutor Interventions Transcript:

**[Student (Seq 1)]**:
I think I got this ques

**[Student (Seq 2)]**:
toin right

**[Human Tutor (Seq 3)]**:
Hi Amir

**[Student (Seq 4)]**:
hi

**[Human Tutor (Seq 5)]**:
how are you this evening?

**[Student (Seq 6)]**:
fine how is yours

**[Human Tutor (Seq 7)]**:
good thank you

**[Human Tutor (Seq 8)] _(Pedagogical Move: <Keep Together>)_**:
let's have a look at this question?

**[Human Tutor (Seq 9)] _(Pedagogical Move: <Press for Accuracy>)_**:
What does expand mean?

**[Student (Seq 10)]**:
muptiple

**[Human Tutor (Seq 11)]**:
fantastic!🎉

**[Human Tutor (Seq 12)]**:
so, 4(3c+2) means

**[Human Tutor (Seq 13)]**:
4 x 3c

**[Student (Seq 14)]**:
12c

**[Human Tutor (Seq 15)]**:
+

**[Human Tutor (Seq 16)]**:
4 x 2

**[Student (Seq 17)]**:
8

**[Human Tutor (Seq 18)]**:
if yoy put it all together...

**[Human Tutor (Seq 19)]**:
you*

**[Human Tutor (Seq 20)] _(Pedagogical Move: <Press for Accuracy>)_**:
What do you get?

**[Student (Seq 21)]**:
no I pressed the wrong button its 12c = 8

**[Student (Seq 22)]**:
"="

**[Human Tutor (Seq 23)] _(Pedagogical Move: <Revoicing>)_**:
not =

**[Student (Seq 24)]**:
+

**[Human Tutor (Seq 25)] _(Pedagogical Move: <Revoicing>)_**:
there is a + between.. so add the 2 parts together

**[Human Tutor (Seq 26)]**:
That's it - well done!😊🎉

**[Student (Seq 27)]**:
12c + 8

**[Human Tutor (Seq 28)]**:
Perfect 😊

**[Student (Seq 29)]**:
I pressed the wrong button thx

**[Student (Seq 30)]**:
am good now

**[Human Tutor (Seq 31)]**:
Fab - shall I send you back?

**[Student (Seq 32)]**:
yes please

**[Human Tutor (Seq 33)]**:
Great work Amir

**[Student (Seq 34)]**:
thx bye

---

## Test Case `EEDI_0017`: Reverse Percentages (Original Amount)
- **Question ID**: `143355` | **Messages**: 20 (9 Student, 11 Tutor)
### Diagnostic Question Given to Student:
```text
Lina buys a painting for \( £ 80 \) and sells it for \( £ 140 \).
What percentage profit is this?
```

### Human Tutor Interventions Transcript:

**[Human Tutor (Seq 1)] _(Pedagogical Move: <Keep Together>)_**:
Hi Ethan, how can I help?

**[Student (Seq 2)]**:
i dont understand the question to work it out

**[Human Tutor (Seq 3)]**:
to work out percentage profit, you need to use the formula: difference in price/original x 100

**[Student (Seq 4)]**:
i did that and the percentage isnt on there

**[Human Tutor (Seq 5)] _(Pedagogical Move: <Press for Accuracy>)_**:
okay what is the difference in price?

**[Student (Seq 6)]**:
140

**[Human Tutor (Seq 7)]**:
not quite, she buys the painting for £80 & sells it for £140

**[Human Tutor (Seq 8)] _(Pedagogical Move: <Press for Accuracy>)_**:
what is the difference?

**[Student (Seq 9)]**:
60

**[Human Tutor (Seq 10)] _(Pedagogical Move: <Press for Accuracy>)_**:
okay good, now what is the original price?

**[Student (Seq 11)]**:
80

**[Human Tutor (Seq 12)] _(Pedagogical Move: <Revoicing>)_**:
okay so the formula will be 60/80 x 100

**[Student (Seq 13)]**:
thank you for your help😀

**[Human Tutor (Seq 14)] _(Pedagogical Move: <Press for Accuracy>)_**:
what do you think the answer is?

**[Student (Seq 15)]**:
yes

**[Student (Seq 16)]**:
75%

**[Human Tutor (Seq 17)]**:
good! well done

**[Human Tutor (Seq 18)] _(Pedagogical Move: <Keep Together>)_**:
would you like any more help?

**[Student (Seq 19)]**:
no thank you

**[Human Tutor (Seq 20)]**:
okay I'll let you get back to the lesson 😊

---

## Test Case `EEDI_0018`: Basic Angle Facts (straight line, opposite, around a point, etc)
- **Question ID**: `76840` | **Messages**: 37 (14 Student, 23 Tutor)
### Diagnostic Question Given to Student:
```text
Image of four angles meeting at a point. One angle is marked with the right-angle symbol, one is 50 degrees, one is 170 degrees and the last one is marked with a square.
```

### Human Tutor Interventions Transcript:

**[Human Tutor (Seq 1)]**:
Hi Nina :)

**[Human Tutor (Seq 2)] _(Pedagogical Move: <Keep Together>)_**:
How can I help you? :)

**[Student (Seq 3)]**:
I'm confused on this question

**[Human Tutor (Seq 4)]**:
Okie doke :)

**[Human Tutor (Seq 5)]**:
So here we need to use one of those facts to help us find the angle where the black square is

**[Human Tutor (Seq 6)]**:
There are 4 different reasons there, so we need to choose which one is the right one :)

**[Student (Seq 7)]**:
I'm not sure how to find the answer

**[Human Tutor (Seq 8)]**:
Ok, let's go through and check if they work for us. A says angles at a point sum to 360

**[Human Tutor (Seq 9)] _(Pedagogical Move: <Keep Together>)_**:
Do we have angles around a point on the diagram?

**[Student (Seq 10)]**:
Yes I think

**[Human Tutor (Seq 11)]**:
Yes it is :)

**[Student (Seq 12)]**:
Oh so the answer is A

**[Human Tutor (Seq 13)] _(Pedagogical Move: <Keep Together>)_**:
Because all the angles there are around exactly one point. Do we know every angle except one of them? :)

**[Student (Seq 14)]**:
Not really

**[Human Tutor (Seq 15)] _(Pedagogical Move: <Press for Accuracy>)_**:
Which ones don't we know? :)

**[Student (Seq 16)]**:
170 and 50

**[Human Tutor (Seq 17)]**:
Super, we do :)

**[Student (Seq 18)]**:
I don't know them

**[Human Tutor (Seq 19)] _(Pedagogical Move: <Press for Accuracy>)_**:
And then the top right has a little white square in. Do you remember what that means? 😊

**[Student (Seq 20)]**:
I have no idea

**[Human Tutor (Seq 21)] _(Pedagogical Move: <Press for Accuracy>)_**:
No problem, so that means it is a right-angle. Do you know how big a right-angle is? :)

**[Student (Seq 22)]**:
90

**[Human Tutor (Seq 23)]**:
Perfect! ⭐

**[Human Tutor (Seq 24)] _(Pedagogical Move: <Revoicing>)_**:
So that means we know that there are 4 angles there, and we know 3 of them are 50, 170 and 90

**[Human Tutor (Seq 25)] _(Pedagogical Move: <Press for Accuracy>)_**:
So how would we work out the missing one? 😊

**[Student (Seq 26)]**:
Add them together? I'm not sure

**[Human Tutor (Seq 27)] _(Pedagogical Move: <Revoicing>)_**:
Yep we can add them together, well done :)

**[Student (Seq 28)]**:
310?

**[Human Tutor (Seq 29)] _(Pedagogical Move: <Press for Accuracy>)_**:
Adding them together gives us 310, and then if we used the fact that all the angles have to add to 360, then we know our missing one must be? :)

**[Student (Seq 30)]**:
50

**[Human Tutor (Seq 31)]**:
Exactly! ⭐⭐

**[Human Tutor (Seq 32)]**:
Well done 😁

**[Student (Seq 33)]**:
Thanks for the help

**[Human Tutor (Seq 34)]**:
And so we've managed to use only that first fact :)

**[Human Tutor (Seq 35)]**:
You're very welcome! I'll let you get back and put your answer in, it might be worth taking the lesson for this one, just for a bit more practice of using that fact 😊

**[Student (Seq 36)]**:
OK

**[Human Tutor (Seq 37)]**:
Enjoy the rest of your day! ☀

---

## Test Case `EEDI_0019`: Written Subtraction
- **Question ID**: `77590` | **Messages**: 56 (20 Student, 36 Tutor)
### Diagnostic Question Given to Student:
```text
At the start of the day, there was \( £ 1,578 \) in the till. \( £ 6,537 \) was taken and \( £ 3,485 \) was handed out. How much money was left?
```

### Human Tutor Interventions Transcript:

**[Human Tutor (Seq 1)]**:
Hey Yasmin :) How are you?

**[Student (Seq 2)]**:
Good

**[Student (Seq 3)]**:
How are you

**[Human Tutor (Seq 4)] _(Pedagogical Move: <Keep Together>)_**:
How are you getting on with this question?

**[Human Tutor (Seq 5)]**:
I'm good thanks :)

**[Student (Seq 6)]**:
You cannot subtract 6537 from 1578 without it going into negative

**[Human Tutor (Seq 7)]**:
let's look at what the questions says

**[Human Tutor (Seq 8)]**:
to start there is £1,578 in the till

**[Human Tutor (Seq 9)]**:
£6,537 is taken

**[Human Tutor (Seq 10)] _(Pedagogical Move: <Press for Accuracy>)_**:
what does that mean?

**[Student (Seq 11)]**:
6537 has been taken from 1578

**[Human Tutor (Seq 12)]**:
not quite

**[Human Tutor (Seq 13)]**:
it's in a till context, so it means that amount has been taken in

**[Human Tutor (Seq 14)]**:
and then £3,485 was handed out (as in out of the till)

**[Student (Seq 15)]**:
Oh so it's been added

**[Human Tutor (Seq 16)]**:
that's right 😊

**[Student (Seq 17)]**:
And then subtracted

**[Human Tutor (Seq 18)]**:
👏😁 perfect

**[Student (Seq 19)]**:
😀

**[Human Tutor (Seq 20)] _(Pedagogical Move: <Keep Together>)_**:
shall we get to the answer to check?

**[Student (Seq 21)]**:
Yes!!!!!!!!!!!!!!!!!!!

**[Human Tutor (Seq 22)]**:
ok, let's go!

**[Human Tutor (Seq 23)]**:
so we start with £1,578

**[Human Tutor (Seq 24)] _(Pedagogical Move: <Press for Accuracy>)_**:
then what?

**[Student (Seq 25)]**:
Then you add on 6537

**[Human Tutor (Seq 26)] _(Pedagogical Move: <Press for Accuracy>)_**:
what does that give?

**[Student (Seq 27)]**:
Anybody have a calculator  😂

**[Human Tutor (Seq 28)]**:
can you use one on your device (laptop / phone)

**[Student (Seq 29)]**:
Sure

**[Human Tutor (Seq 30)]**:
ok, super

**[Human Tutor (Seq 31)]**:
take your time

**[Student (Seq 32)]**:
8115

**[Human Tutor (Seq 33)]**:
brilliant Yasmin

**[Human Tutor (Seq 34)] _(Pedagogical Move: <Press for Accuracy>)_**:
Now, what is our next step>

**[Human Tutor (Seq 35)]**:
?

**[Student (Seq 36)]**:
I love how you take your time with me

**[Human Tutor (Seq 37)]**:
good good, it's important not to rush

**[Student (Seq 38)]**:
Subtract 3485 from 8115

**[Human Tutor (Seq 39)]**:
lovely

**[Human Tutor (Seq 40)]**:
let me know when you're ready with an answer

**[Student (Seq 41)]**:
4630☺️

**[Human Tutor (Seq 42)]**:
super work Yasmin

**[Human Tutor (Seq 43)] _(Pedagogical Move: <Keep Together>)_**:
Does this match any of the possible answers?

**[Student (Seq 44)]**:
C

**[Human Tutor (Seq 45)]**:
⭐👏🎉

**[Human Tutor (Seq 46)]**:
fabulous Yasmin

**[Human Tutor (Seq 47)]**:
It was really just the wording in that question! Your maths is spot on!!

**[Human Tutor (Seq 48)]**:
well done

**[Student (Seq 49)]**:
What's your favourite colour

**[Student (Seq 50)]**:
Before I go

**[Human Tutor (Seq 51)]**:
that's not important, but well done today

**[Human Tutor (Seq 52)] _(Pedagogical Move: <Keep Together>)_**:
Can I help you with anything else on the bot?

**[Student (Seq 53)]**:
No thank you

**[Human Tutor (Seq 54)]**:
ok, no problem

**[Student (Seq 55)]**:
Bye

**[Human Tutor (Seq 56)]**:
I'll send you back now :) Bye Yasmin

---

## Test Case `EEDI_0020`: Time Series and Line Graphs
- **Question ID**: `79107` | **Messages**: 26 (10 Student, 16 Tutor)
### Diagnostic Question Given to Student:
```text
How many months have an average temperature above 23⁰C ?
```

### Human Tutor Interventions Transcript:

**[Human Tutor (Seq 1)]**:
Hello Sanjay 👋👋👋

**[Human Tutor (Seq 2)] _(Pedagogical Move: <Keep Together>)_**:
Can I help you with these types of questions?!

**[Student (Seq 3)]**:
yes please

**[Human Tutor (Seq 4)]**:
Of course 😊👌

**[Human Tutor (Seq 5)] _(Pedagogical Move: <Press for Accuracy>)_**:
Do you know where 23 degrees is on the y-axis?!

**[Student (Seq 6)]**:
yes

**[Human Tutor (Seq 7)] _(Pedagogical Move: <Press for Accuracy>)_**:
Great if you move your finger across the graph... How many dots are above this line? 🧠

**[Human Tutor (Seq 8)]**:
Remember 23 degrees is not MORE than 23....

**[Student (Seq 9)]**:
it is less than 23?

**[Human Tutor (Seq 10)] _(Pedagogical Move: <Keep Together>)_**:
It is 23... So we can't count it as more than 23. If that makes sense? 😊

**[Human Tutor (Seq 11)] _(Pedagogical Move: <Press for Accuracy>)_**:
So how many months are there? 🧠

**[Student (Seq 12)]**:
8

**[Human Tutor (Seq 13)] _(Pedagogical Move: <Press for Accuracy>)_**:
Ahhh you have accidentally counted the months below 23 degrees... What has the question asked you to find? 😁

**[Student (Seq 14)]**:
how many moths have an have an average temperature above 23 degries c

**[Human Tutor (Seq 15)] _(Pedagogical Move: <Revoicing>)_**:
Great work so we don't count the dots below 23 degrees, we need to count the dots above 23 degrees 👍👍👍

**[Human Tutor (Seq 16)] _(Pedagogical Move: <Press for Accuracy>)_**:
Can you do that now and let me know how many there are...

**[Student (Seq 17)]**:
okay

**[Student (Seq 18)]**:
4

**[Human Tutor (Seq 19)]**:
Nailed it 🔨🔨🔨

**[Human Tutor (Seq 20)]**:
Well done Sanjay!

**[Student (Seq 21)]**:
thank you

**[Human Tutor (Seq 22)]**:
Always read the question carefully and remember if it says above or below it cannot be the same as

**[Student (Seq 23)]**:
okay

**[Human Tutor (Seq 24)]**:
Ready to go back to eedi? 🤖🤖🤖

**[Student (Seq 25)]**:
yes

**[Human Tutor (Seq 26)]**:
Of course, I'll pass you back. Nice work today 👍👍👍

---

