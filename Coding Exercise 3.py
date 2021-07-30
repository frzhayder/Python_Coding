
Message='''Author: Fraz Haider
Game: Q-Euro-war 
Version: 2.0
© 2021 Fraz. All rights reserved.'''
print(Message)


userin= input("Enter your name to play:    ")
name=input
Message1= '''\nWelcome to the world of Q-Euro-War.'''
print(Message1)
Message2='''This is a multiple-choice Quiz game,
there are total 5 questions to be answered.
To win the game, you need to answer 4 questions.'''
print(Message2)
    
score = 0;
q_count = 0;

# Q1 information:
question1 = "\nQ1.Which one is the longest river of the continent of Europe?";
choices1  = "\na. Danube \nb. Rhine \nc. Volga";
prompt_question1 = question1 + choices1;
answer1 = "c";

user_in = input(prompt_question1 + "\n\nEnter your answer: ")
print()
if user_in == answer1:
    score = score + 10;
    q_count = q_count + 1;
    print("\n Congrats correct answer. You made {0} points!! still you got 4 questions to answer.".format(score))
else:
    score = score + 0;
    q_count = q_count + 1;
    print("\nIncorrect answer. Aww, what a shame. That wasnt the correct answer. You got {0} points.".format(score))
    #“Aww, what a shame. That wasn’t the correct answer. You got 0 points”.
    
# Q2 information:
question2 = "\nQ2. What is the most populated capital city in Europe?";
choices2  = "\na. Berlin \nb. Madrid \nc. Rome";
prompt_question2 = question2 + choices2;
answer2 = "a";

user_in = input(prompt_question2 + "\n\nEnter your answer: ")
print()
if user_in == answer2:
    score = score + 10;
    q_count = q_count + 1;
    print("\nCongrats correct answer. You got {0} points!!".format(score))
else:
    score = score + 0;
    q_count = q_count + 1;
    print("\nIncorrect answer. Aww, what a shame. That wasnt the correct answer. You got {0} points.".format(score))



    
# Q3 information:
   
question3 = "\nQ3. Which country in Europe is the richest?";
choices3  = "\na. Luxembourg \nb. France \nc. Germany";
prompt_question3 = question3 + choices3;
answer3 = "a";

user_in = input(prompt_question3 + "\n\nEnter your answer: ")
print()
if user_in == answer3:
    score = score + 10;
    q_count = q_count + 1;
    print("\nCongrats correct answer. You got {0} points!!".format(score))
else:
    score = score + 0;
    q_count = q_count + 1;
    print("\nIncorrect answer. Aww, what a shame. That wasnt the correct anser.You got {0} points.".format(score))

# Q4 information:
question4 = "Q4. Which is the poorest country in the Europe?";
choices4  = "\na. France  \nb. Moldova \nc. Malta ";
prompt_question4 = question4 + choices4;
answer4 = "b";

user_in = input(prompt_question4 + "\n\nEnter your answer: ")
print()
if user_in == answer4:
    score = score + 10;
    q_count = q_count + 1;
    print("\nCongrats correct answer. You got {0} points!!".format(score))
else:
    score = score + 0;
    q_count = q_count + 1;
    print("\nIncorrect answer. Aww, what a shame. That wasnt the correct anser. You got {0} points!!".format(score))
    
if score >= 40:
    print("\n\nYou got {0} points in total. You won. Bravo, you're such a pro mate!".format(score))
else:
    print("\n\nYou got {0} points in total. You need to answer one more question to win the game!".format(score))

       
# Q5 information:
   
question5 = "\nQ5. Where is capital of Europe?";
choices5  = "\na. Paris \nb.Brussels  \nc. Dusseldorf";
prompt_question5 = question5 + choices5;
answer5 = "b";

user_in = input(prompt_question5 + "\n\nEnter your answer: ")
print()
if user_in == answer5:
    score = score + 10;
    q_count = q_count + 1;
    print("\nCongrats correct answer. You got {0} points!!".format(score))
else:
    score = score + 0;
    q_count = q_count + 1;
    print("\Incorrect answer. Aww, what a shame. That wasnt the correct anser. You got {0} points.".format(score))

if score >= 40:
    print("\n\nYou got {0} points in total. You won. Bravo, you're such a pro mate!".format(score))
else:
    print("\n\nYou got {0} points in total. Oh dear. So close and yet so far. Good luck next time !".format(score))
