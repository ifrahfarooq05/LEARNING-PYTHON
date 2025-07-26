#GREETING ACCORDING TO TIME: EXERCISE 2
import time 
t = time.strftime ('%H:%M:%S')
hour = int(time.strftime('%H'))
print(hour)
if hour>=0 and hour<12:
    print("Good Morning")
elif hour>=12 and hour<17:
    print("Good Afternoon")    
elif hour>=17 and hour<19:
    print("Good Evening") 
else:
    print("Good Night")

#CREATING A GENERAL KNOWLEDGE QUIZ: EXERCISE 3
Q1 = str( '''What is the capital city of Canada?
A) Toronto
B) Ottawa
C) Vancouver
D) Montreal ''')
Q2 = str( '''Who wrote the play Romeo and Juliet?
A) Charles Dickens
B) William Shakespeare
C) Jane Austen
D) George Bernard Shaw''')
Q3 = str('''What is the largest planet in our solar system?
A) Earth
B) Saturn
C) Jupiter
D) Neptune''')
print(' "WELCOME TO QUIZ-WHIZZ WITH IFRAH" ')
print( 'Test your brainpower and boost your knowledge with Ifrah’s ultimate quiz challenge!')
print(' " ANSWER THE QUESTIONS AND WIN PRIZES" ')      

print(Q1)
a = input("Your answer: ")
if a=="ottawa":
    print("Correct answer u win 10,000 Rupees")
else:
    print("Wrong answer,Correct answer is Ottawa ")
print(Q2)    
b = input("Your answer: ")
if b=="William Shakespeare":
    print("Correct answer, u win 10,000 Rupees")
else:
    print("Wrong Answer, correct answer is William Shakespeare")
print(Q3)    
c = input("Your Answer: ")
if c== "Jupiter":
    print("Correct answer, u win 10,000 Rupees")
else:
    print("Wrong Answer, Correct answer is Jupiter")
