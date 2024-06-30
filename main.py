# #first print statement in python
# print("Bismillah")

# #comments in python
# #this is a single line comment
# ''' this is multiline
# string comment'''

# #escape sequence characters
# print("Hello \n World") #new line

# #separator and end parameters in print statement
# print("Rafey", sep='@', end="Ansari")

# #types of datatypes in python
# a = 1
# b = True
# c = "Harry"
# d = None
# e = 9.9

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))

# #sequence datatypes
# #list
# list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
# print(list1)

# #tuple
# tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
# print(tuple1)

# #dictionary
# dict1 = {"name":"Sakshi", "age":20, "canVote":True}
# print(dict1)

# #calculator

# n = 15
# m = 7
# ans1 = n+m
# print("Addition of",n,"and",m,"is", ans1)
# ans2 = n-m
# print("Subtraction of",n,"and",m,"is", ans2)
# ans3 = n*m
# print("Multiplication of",n,"and",m,"is", ans3)
# ans4 = n/m
# print("Division of",n,"and",m,"is", ans4)
# ans5 = n%m
# print("Modulus of",n,"and",m,"is", ans5)
# ans6 = n//m
# print("Floor Division of",n,"and",m,"is", ans6)

# #typecasting in python
# #explicit
# string = "15"
# number = 7
# string_number = int(string) #throws an error if the string is not a valid integer
# sum= number + string_number
# print("The Sum of both the numbers is: ", sum)

# #implicit
# # Python automatically converts
# # a to int
# a = 7
# print(type(a))
 
# # Python automatically converts b to float
# b = 3.0
# print(type(b))
 
# # Python automatically converts c to float as it is a float addition
# c = a + b
# print(c)
# print(type(c))

# #taking user input
# name=input("Enter your name: ")
# print(name)

# age=int(input("Enter your age: "))
# print(age)

# #string methods
# name = "Rafey"
# print("Hey, " + name)

# print('He said, "I want to eat an apple".')

# #multiline strings
# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
# print(a)
# #Accessing character in string
# print(name[0])
# print(name[1])

# #loopin in string
# for character in name:
#     print(character)

# #String Slicing & Operations on String
# name = "Rafey"
# print(name[0:3]) #Raf
# print(name[2:5]) #fey
# print(name[0:5]) #Rafey
# print(name[0:]) #Rafey
# print(name[:5]) #Rafey
# print(name[:]) #Rafey
# print(name[-1:]) #Rafey

# #length of a string 
# fruit = "Mango"
# len1 = len(fruit)
# print("Mango is a", len1, "letter word.")

# #string as an array
# name = "Rafey"
# print(name[0])
# print(name[1])

# #loop through a string
# alphabets = "ABCDE"
# for i in alphabets:
#     print(i)

# #string methods

# #upper  
# str1 = "AbcDEfghIJ"
# print(str1.upper())

# #lower
# str1 = "AbcDEfghIJ"
# print(str1.lower())

# #strip
# str2 = " Silver Spoon "
# print(str2.strip())

# #rstrip
# str3 = "Hello !!!"
# print(str3.rstrip("!"))

# #replace
# str2 = "Silver Spoon"
# print(str2.replace("Sp", "M"))

# #split
# str2 = "Silver Spoon"
# print(str2.split(" "))      #Splits the string at the whitespace " ".

# #capitalize
# str1 = "hello"
# capStr1 = str1.capitalize()
# print(capStr1)
# str2 = "hello WorlD"
# capStr2 = str2.capitalize()
# print(capStr2)

# #center
# str1 = "Welcome to the Console!!!"
# print(str1.center(50))

# str1 = "Welcome to the Console!!!"
# print(str1.center(50, "."))

# #count
# str2 = "Abracadabra"
# countStr = str2.count("a")
# print(countStr)

# # startswith
# str1 = "Python is a Interpreted Language" 
# print(str1.startswith("Python"))

# #endswith
# str1 = "Welcome to the Console !!!"
# print(str1.endswith("!!!"))

# str1 = "Welcome to the Console !!!"
# print(str1.endswith("to", 4, 10))

# #find
# str1 = "He's name is Dan. He is an honest man."
# print(str1.find("is"))

# str1 = "He's name is Dan. He is an honest man."
# print(str1.find("Daniel"))

# #index
# str1 = "He's name is Dan. Dan is an honest man."
# print(str1.index("Dan"))

# # str1 = "He's name is Dan. Dan is an honest man."
# # print(str1.index("Daniel"))

# #isalnum
# str1 = "WelcomeToTheConsole"
# print(str1.isalnum())

# #isalpha
# str1 = "Welcome"
# print(str1.isalpha())

# # islower
# str1 = "hello world"
# print(str1.islower())

# #isprintable
# str1 = "hello world"
# print(str1.isprintable())

# #isspace
# str1 = "        "       #using Spacebar
# print(str1.isspace())
# str2 = "        "       #using Tab
# print(str2.isspace())

# #istitle
# str1 = "World Health Organization" 
# print(str1.istitle())

# str2 = "To kill a Mocking bird"
# print(str2.istitle())

# # isupper
# str1 = "WORLD HEALTH ORGANIZATION" 
# print(str1.isupper())

# #swapcase
# str1 = "Python is a Interpreted Language" 
# print(str1.swapcase())

# #title
# str1 = "He's name is Dan. Dan is an honest man."
# print(str1.title())

# # if-else-statement
# applePrice = 200
# budget = 200
# if (applePrice <= budget):
#     print("Alexa, add 1 kg Apples to the cart.")
# else:
#     print("Alexa, do not add Apples to the cart.")
    

# elif statements
# num = int(input("Enter any number: "))
# if (num < 0):
#     print(num, "is negative.")
# elif (num == 0):
#     print("Number is Zero.")
# else:
#     print(num, "is positive.")

# #nested if-elif-else statements
# num = int(input("Enter any number: "))
# if(num<0):
#     print(num, " is negative.")
# elif(num > 0):
#     if(num <= 10):
#         print(num, "is in between 1-10.")
#     elif(num <= 20):
#         print(num, "is in between 11-20.")
#     else:
#         print(num, "is greater than 20.")
# else:
#     print("Number is zero")

# #Exercise 2
# import time
# times = time.strftime('%H:%M:%S')
# print("The time is",times)
# timestamp = int(time.strftime('%H')) 

# if(timestamp >= 6 and timestamp <= 12):
#     print("Good Morning")
# elif(timestamp >=12 and timestamp <= 16):
#     print("Good Afternoon")
# elif(timestamp >=16 and timestamp <= 18):
#     print("Good Evening")
# else:
#     print("Good Night")
    
    
# #match-case statements
# x = int(input("Enter x: "))
# # x is the variable to match
# match x:
#     # if x is 0
#     case 0:
#         print("x is zero")
#     # case with if-condition
#     case 4 if x % 2 == 0:
#         print("x % 2 == 0 and case is 4")
#     # Empty case with if-condition
#     case _ if x < 10:
#         print("x is < 10")
#     # default case(will only be matched if the above cases were not matched)
#     # so it is basically just an else:
#     case _:
#         print(x)
        
# # for loops

# #iterating over a string
# name = 'Rafeldo'
# for i in name:
#     print(i, end=", ")
    
# # iterating over a list
# colors = ["Red", "Green", "Blue", "Yellow"]
# for x in colors:
#     print(x)
    
# #range 
# for k in range(5):
#     print(k)
# for k in range(4,9):
#     print(k)
# for k in range(4,9,2):
#     print(k)

# # while loop
# count = 5
# while (count > 0):
#   print(count)
#   count = count - 1
  
# # else with while loop
# x = 5
# while (x > 0):
#     print(x)
#     x = x - 1
# else:
#     print('counter is 0')
    
# # do-while loop
# while True:
#   number = int(input("Enter a positive number: "))
#   print(number)
#   if not number > 0:
#     break

# # break and continue

# for i in range(1,101,1):
#     print(i ,end=" ")
#     if(i==50):
#         break
#     else:
#         print("Mississippi")
# print("Thank you")

# for i in range(0,100):
#     if (i%2!=0):
#         continue
#     print(i)

# for i in [2,3,4,6,8,0]:
#     if (i%2!=0):
#         continue
#     print(i)

# #functions
# def name(fname, lname):
#     print("Hey,", fname, lname)
# name("Rafey", "Ansari")

# #Function Arguments and return statement

# #default arguments
# def name(fname, mname = "Jhon", lname = "Whatson"):
#     print("Hello,", fname, mname, lname)

# name("Amy")

# # Keyword arguments
# def name(fname, mname, lname):
#     print("Hello,", fname, mname, lname)

# name(mname = "Peter", lname = "Wesker", fname = "Jade")

# # Required arguments:
# def name(fname, mname, lname):
#     print("Hello,", fname, mname, lname)

# name("Peter", "Ego", "Quill")

# # variable length arguments
# #Arbitrary Arguments
# def name(*name):
#     print("Hello,", name[0], name[1], name[2])

# name("James", "Buchanan", "Barnes")

# # Keyword Arbitrary Arguments:
# def name(**name):
#     print("Hello,", name["fname"], name["mname"], name["lname"])

# name(mname = "Buchanan", lname = "Barnes", fname = "James")

# # return Statement
# def name(fname, mname, lname):
#     return "Hello, " + fname + " " + mname + " " + lname

# print(name("James", "Buchanan", "Barnes"))

# # Python Lists
# lst1 = [1,2,2,3,5,4,6]
# lst2 = ["Red", "Green", "Blue"]
# print(lst1)
# print(lst2)

# details = ["Abhijeet", 18, "FYBScIT", 9.8]
# print(details)

# # list index 
# colors = ["Red", "Green", "Blue", "Yellow", "Green"]
# #          [0]      [1]     [2]      [3]      [4]
# print(colors[2])
# print(colors[4])
# print(colors[0])

# # negative indexing
# colors = ["Red", "Green", "Blue", "Yellow", "Green"]
# #          [-5]    [-4]    [-3]     [-2]      [-1]
# print(colors[-1])
# print(colors[-3])
# print(colors[-5])

# # Check whether an item in present in the list?
# colors = ["Red", "Green", "Blue", "Yellow", "Green"]
# if "Yellow" in colors:
#     print("Yellow is present.")
# else:
#     print("Yellow is absent.")
    
#     # range of index
# animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
# print(animals[3:7])	#using positive indexes
# print(animals[-7:-2])	#using negative indexes'

# List comprehension

# # Accepts items with the small letter “o” in the new list
# names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
# namesWith_O = [item for item in names if "o" in item]
# print(namesWith_O)

# #  Accepts items which have more than 4 letters
# names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
# nameshavingMax4 = [item for item in names if (len(item) > 4)]
# print(nameshavingMax4)

# List Methods

# # list.sort()
# colors = ["violet", "indigo", "blue", "green"]
# colors.sort()
# print(colors)

# num = [4,2,5,3,6,1,2,1,2,8,9,7]
# num.sort()
# print(num)

# # reverse order
# colors = ["voilet", "indigo", "blue", "green"]
# colors.sort(reverse=True)
# print(colors)

# num = [4,2,5,3,6,1,2,1,2,8,9,7]
# num.sort(reverse=True)
# print(num)

# # reverse()
# colors = ["violet", "indigo", "blue", "green"]
# colors.reverse()
# print(colors)

# num = [4,2,5,3,6,1,2,1,2,8,9,7]
# num.reverse()
# print(num)

# # index()
# colors = ["violet", "green", "indigo", "blue", "green"]
# print(colors.index("green"))

# num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
# print(num.index(3))

# # count()
# colors = ["violet", "green", "indigo", "blue", "green"]
# print(colors.count("green"))

# num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
# print(num.count(2))

# # copy()
# colors = ["violet", "green", "indigo", "blue"]
# newlist = colors.copy()
# print(colors)
# print(newlist)

# # append()
# colors = ["violet", "green", "indigo", "blue"]
# colors.append("red")
# print(colors)

# # insert()
# colors = ["violet", "green", "indigo", "blue"]
# colors.insert(2, "red")
# print(colors)

# # extend()
# #add a list to a list
# colors = ["violet", "indigo", "blue"]
# rainbow = ["green", "yellow", "orange", "red"]
# colors.extend(rainbow)
# print(colors)

# # concatenating two list
# colors = ["violet", "indigo", "blue", "green"]
# colors2 = ["yellow", "orange", "red"]
# print(colors + colors2)

# # TUPLESSS

# tuple1 = (1,2,2,3,5,4,6)
# tuple2 = ("Red", "Green", "Blue")
# print(tuple1)
# print(tuple2)

# details = ("Abhijeet", 18, "FYBScIT", 9.8)
# print(details)

# indexing same as list

# # Manipulating Tuples
# countries = ("Spain", "Italy", "India", "England", "Germany")
# temp = list(countries)
# temp.append("Russia")       #add item 
# temp.pop(3)                 #remove item
# temp[2] = "Finland"         #change item
# countries = tuple(temp)
# print(countries)

# countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
# countries2 = ("Vietnam", "India", "China")
# southEastAsia = countries + countries2
# print(southEastAsia)

# # Tuple methods

# # count()
# Tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
# res = Tuple1.count(3)
# print('Count of 3 in Tuple1 is:', res)

# # index()
# Tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2)
# res = Tuple.index(3)
# print('First occurrence of 3 is', res)