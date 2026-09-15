print("\n***WELCOME TO QUIZ CORNER***")
score = 0

Questions = []
Answers = []
Options = []
user_answers = []

question1 = "1. What is the brain of the computer ?"
option1 = "A)Monitor\n B)Keyboard\n C)Mouse\n D)CPU"
answer1 = "D"

Questions.append(question1)
Options.append(option1)
Answers.append(answer1)

question2 = "2. Which device is used to type text in computer ?"
option2 = "A)Mouse\n B)Monitor\n C)Keyboard\n D)Speaker"
answer2 = "C"

Questions.append(question2)
Options.append(option2)
Answers.append(answer2)

question3 = "3. Which of these is an operating system ?"
option3 = "A)Windows\n B)Google\n C)Youtube\n D)Instagram"
answer3 = "A"

Questions.append(question3)
Options.append(option3)
Answers.append(answer3)

question4 = "4. What does RAM stands for ?"
option4 = "A)Read Access Memory\n B)Random Access Memory\n C)Run Access Memory\n D)Random Application Memory"
answer4 = "B"

Questions.append(question4)
Options.append(option4)
Answers.append(answer4)

question5 = "5. Which device is mainly used to move the pointer on the screen ?"
option5 = "A)Keyboard\n B)Printer\n C)Mouse\n D)Scanner"
answer5 = "C"

Questions.append(question5)
Options.append(option5)
Answers.append(answer5)

for i in range(len(Questions)):
    print(Questions[i])
    print(Options[i])

    user_answer = input("Enter your answer:")
    user_answers.append(user_answer)

    if(user_answer == Answers[i]):
        score = score + 1

print("Quiz Result")
for i in range(len(Questions)):
    print("Question",i+1)
    print("Your answer:",user_answers[i])
    print("Correct answer:",Answers[i])
print("Your Score:",score,"/",len(Questions))




