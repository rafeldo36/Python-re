# Creating a game like kbc using list

data=[
   ["Which planet in the solar system is known as the “Red Planet”?",
    "Mars", "Jupiter", "Saturn", "Uranus",1
    ],
   [
       "What is the capital of Japan?",
       "Beijing",'Tokyo',"Seoul" ,"Bangkok", 2
   ],
   [
       " Which river is the longest in the world?",
       "Amazon",'Ganga',"Nile" ,"Yangtze", 3
   ],
   [
       " What animal is the national symbol of Australia?",
       "Kangaroo",'Koala',"Emu" ,"Crocodile", 1
   ],
   [
       "What chemical element is designated as “Hg”?",
       "Silver",'Tin',"Copper" ,"Mercury",4 
   ],
]

levels = [20000, 40000, 80000, 160000, 320000]
money = 0
for i in range(0, len(data)):
    question = data[i]
    print(f'\n\nQuestion for Rs.{levels[i]}')
    print(f'a. {question[1]} b. {question[2]}')
    print(f'c. {question[3]} d. {question[4]}')
    reply = int(input("Enter your answer (1-4) or 0 to quit:\n"))
    if ( reply == 0):
        money = levels[i-1]
        break
    if(reply == question[-1]):
        print(f'Correct answer, you have won Rs. {levels[i]}')
        if(i == 2):
            money = 80000
        elif(i == 4):
            money = 320000
    else:
        print('Wrong answer')
        break
    
print(f'Your take home money is {money}')