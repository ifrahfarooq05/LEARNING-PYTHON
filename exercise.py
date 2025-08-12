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

#EXERCISE 3 KON BANEGA CRORE PATI:
questions= [
    ["what is the national game of pakistan?","cricket","hockey","football","basketball","basketball",2],
    ["name the capital of Pakistan?","Karachi","Lahore","Islamabad","multan",3],
    ["Which city of Pakistan is called city of lights?","Karachi","Lahore","Islamabad","multan",1],
    ["Name national flower of pakistan?","lily","roses","sunflower","jasmines",4]
]
levels= [10000,20000,300000,1000000,2000000]

for i in range(0, len(questions)):
    question= questions[i]
    money = 0
    print(f"Question for Rs. {levels[i]}")
    print(f"Q: {question[0]}")
    print(f" 1.{question[1]}  2.{question[2]}")
    print(f" 3.{question[3]}  4.{question[4]}")
    reply= int(input("Enter your answer(1-4) or 0 to quit: "))  
    if(reply==0):
        money = levels[i-1]
        break
    if (reply== question[-1] ):
       print(f"correct answer you have won Rs. {levels[i]} ")
       if (i==4):
           money= 160000
    else:
      print("Wrong answer")
      break 
print(f"Your take of money is {money}")

#EXERCISE 4 CODE LANGUAGE
def talkincode(l):
    if len(l)<3:        #if string is less than 3 words.
        m= l[::-1]     
                 #add characters start and end of that string    
        l= "abc"  
        o="efg" 
        n = o+ m+l    
        print(n)
    else:
        print( l[::-1] )  #if its greater than 3 then simply reverse the strings
  
lang= input("Enter: ")  
talkincode(lang)



    
