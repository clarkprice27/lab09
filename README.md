# lab09
Lab work for CS-1411 501 lab 09
Background
Something that can be useful for studying for an exam is to create a file of questions and answers.
Then write a program to choose questions at random from the file to see if you and your fellow
students can answer them. Choosing questions at random can help to learn needed information
without relying on a particular sequence of information presentation.
Lab Exercise, 5 points design, 10 points program
Step 1:
Create a Python program to read in a file (Qsand0pts.txt) of quiz questions and answers into a list.
Each question set is stored inside the file using 3 lines.
• The	first	line	contains	the	questions	itself.
• The	 second	 line	 contains the	 choices	 for	 the	 question.	 The	 choices	 are	 separated	 by	 two	
characters,	a	dot	and	underscore;	each	question	may	have	a	different	number	of	choices.	The	
choices	should	be	displayed	with	the	number	associated	with	them,	starting	with	number	one.
• The	third	line	contains	the	number	of	the correct	choice.	
Each question set should be stored as a tuple in the list. Display all of the question sets to the
screen in the following format:
1.		Question
1) First	option
2) Second	option
3) Third	option
2.		Question
1) First	option
2) Second	option
3) Third	option

...
Read in a file of names (names.txt). As you read each name, choose 5 unique and random
questions from the questions file. Store the questions in a set. Enter the name into a dictionary
where the name is the key and the set of questions is the value. Print the names and questions
neatly to the screen where the questions are in ascending order.
Judy Questions 3, 8, 15, 17, 22
Marta Questions 1, 2, 3, 4, 5
Martin Questions 17, 20, 21, 23, 28
…
Save the dictionary to a file called ‘togive.txt’. Each name and question set should be stored on
one line in the file.
Step 2:
Create a Python program to read in the ‘Qsand0pts.txt’ file into a list and to read in the ‘togive.txt’
file into a dictionary as given in the “Lab Preparation” Section. Allow the user to select a name
and then give the associated quiz using the questions in the question set stored in the dictionary.
Show the user his/her score at the end of the quiz. Allow the user to select as many names as
desired and give the quiz for each name.
In the sample run below, Judy is given questions 3, 8, 15, 17, and 22 in order from the questions
file, but the questions are numbered from 1 to 5.
Welcome to the quiz preparation program.
Please input the name of a student who should take a practice quiz (enter EXIT to end the
program): Judy
Hi Judy. Here are your questions.
1.		Question
1. First	option
2. Second	option
3. Third	option
What	is	your	answer?	1
2.		Question
1. First	option
2. Second	option
3. Third	option
What is your answer? 2
…
You scored 3/5 – good job
Please input the name of a student who should take a practice quiz (enter EXIT to end the
program): EXIT
Bye.
For your program, do not use global variables except for DEBUG, validate all input, perform
exception handling, and use at least 4 functions (each function should have its purpose immediately
above the function).
