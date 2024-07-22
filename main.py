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

# # F string
# txt = "For only {price:.2f} dollars!"
# print(txt.format(price = 49))

# val = 'Geeks'  
# print(f"{val}for{val} is a portal for {val}.")  
# name = 'Tushar'  
# age = 23  
# print(f"Hello, My name is {name} and I'm {age} years old.")

# print(f"{2 * 30}")

# # docstrings

# def square(n):
#     '''Takes in a number n, returns the square of n'''
#     return n**2
# print(square(5))

# def square(n):
#     '''Takes in a number n, returns the square of n'''
#     return n**2
# print(square.__doc__)

# # Recursion 
# def factorial(num): 
#     if (num == 1 or num == 0):
#         return 1
#     else:
#         return (num * factorial(num - 1)) 
  
# # Driver Code 
# num = 7; 
# print("Number: ",num)
# print("Factorial: ",factorial(num))

# # Sets
# info = {"Carla", 19, False, 5.9, 19}
# print(info)

# sets={}
# print(type(sets)) #output: dict

# # accesing set items using loop
# info = {"Carla", 19, False, 5.9}
# for item in info:
#     print(item)

# # Joining Sets

# # union() and update()
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities3 = cities.union(cities2)
# print(cities3)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities.update(cities2)
# print(cities)

# # intersection and intersection_update()
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities3 = cities.intersection(cities2)
# print(cities3)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities.intersection_update(cities2)
# print(cities)

# # symmetric_difference and symmetric_difference_update()
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities3 = cities.symmetric_difference(cities2)
# print(cities3)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities.symmetric_difference_update(cities2)
# print(cities)

# # difference() and difference_update()
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Seoul", "Kabul", "Delhi"}
# cities3 = cities.difference(cities2)
# print(cities3)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Seoul", "Kabul", "Delhi"}
# print(cities.difference(cities2))

# # Set Methods

# # isdisjoint()
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# print(cities.isdisjoint(cities2))

# # issuperset()
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Seoul", "Kabul"}
# print(cities.issuperset(cities2))
# cities3 = {"Seoul", "Madrid","Kabul"}
# print(cities.issuperset(cities3))

# # issubset()
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Delhi", "Madrid"}
# print(cities2.issubset(cities))

# # add()
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities.add("Helsinki")
# print(cities)

# # update()
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Helsinki", "Warsaw", "Seoul"}
# cities.update(cities2)
# print(cities)

# # remove()/discard()
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities.remove("Tokyo")
# print(cities)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities.remove("Seoul")
# print(cities)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities.discard("Seoul")
# print(cities)

# # pop()
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# item = cities.pop()
# print(cities)
# print(item)

# # del
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# del cities
# print(cities)

# # clear()
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities.clear()
# print(cities)

# # check if item exists
# info = {"Carla", 19, False, 5.9}
# if "Carla" in info:
#     print("Carla is present.")
# else:
#     print("Carla is absent.")

# # Python Dictionaries
# info = {'name':'Karan', 'age':19, 'eligible':True}
# print(info)

# print(info['name']) #accesing single values
# print(info.get('eligible'))

# # accesing multival
# print(info.values())

# # accessing keys
# info = {'name':'Karan', 'age':19, 'eligible':True}
# print(info.keys())

# # accessing key-value pairs
# info = {'name':'Karan', 'age':19, 'eligible':True}
# print(info.items())

# # Dictionary Methods

# # update()
# info = {'name':'Karan', 'age':19, 'eligible':True}
# print(info)
# info.update({'age':20})
# info.update({'DOB':2001})
# print(info)

# # clear()
# info = {'name':'Karan', 'age':19, 'eligible':True}
# info.clear()
# print(info)

# # pop()
# info = {'name':'Karan', 'age':19, 'eligible':True}
# info.pop('eligible')
# print(info)

# # popitem()
# info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
# info.popitem()
# print(info)

# # del
# info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
# del info['age']
# print(info)

# info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
# del info
# print(info)

# # else in loop
# for x in range(5):
#     print ("iteration no {} in for loop".format(x+1))
# else:
#     print ("else block in loop")
# print ("Out of loop")

# # Exception Handling
# try:
#     num = int(input("Enter an integer: "))
# except ValueError:
#     print("Number entered is not an integer.")

# # finally clause
# try:
#     num = int(input("Enter an integer: "))
# except ValueError:
#     print("Number entered is not an integer.")
# else:
#     print("Integer Accepted.")
# finally:
#     print("This block is always executed.")

# # Custom Errors
# salary = int(input("Enter salary amount: "))
# if not 2000 < salary < 5000:
#     raise ValueError("Not a valid salary")

# # short hand if else
# a = 2
# b = 330
# print("A") if a > b else print("B")

# a = 330
# b = 330
# print("A") if a > b else print("=") if a == b else print("B")

# # Enumerate
# # Loop over a list and print the index and value of each element
# fruits = ['apple', 'banana', 'mango']
# for index, fruit in enumerate(fruits):
#     print(index, fruit)

# # Loop over a list and print the index (starting at 1) and value of each element
# fruits = ['apple', 'banana', 'mango']
# for index, fruit in enumerate(fruits, start=1):
#     print(index, fruit)

# # VENV 
# import math

# result = math.sqrt(9)
# print(result)  # Output: 3.0

# print(dir(math))

# # if "__name__ == "__main__" in Python
# import rafey

# rafey.main()

# import os 
# # Open the file in read-only mode
# f = os.open("sample.txt", os.O_RDONLY)
# # Read the contents of the file
# contents = os.read(f, 1024)
# # Close the file
# os.close(f)

# # Open the file in write-only mode
# f = os.open("sample.txt", os.O_WRONLY)
# # Write to the file
# os.write(f, b"Hello, world!")
# # Close the file
# os.close(f)

# import os
# # Get a list of the files in the current directory
# files = os.listdir(".")
# print(files)  

# import os

# # Create a new directory
# os.mkdir("newdir")

# import os

# # Run the "ls" command and get the output as a file-like object
# f = os.popen("dir")

# # Read the contents of the output
# output = f.read()
# print(output)  # Output: ['myfile.txt', 'otherfile.txt']

# # Close the file-like object
# f.close()

# import os 

# if(not os.path.exists("data")):
#     os.mkdir("data")
    
# for i in range (0, 100):
#     os.mkdir(f"data/Day{i+1}")

# for i in range(0, 100):
#     os.rename(f"data/Day{i+1}", f"data/Tutorial {i+1}")
    
# # global and local
# x = 10 # global variable

# def my_function():
#   y = 5 # local variable
#   print(y)

# my_function()
# print(x)
# print(y) # this will cause an error because y is a local variable and is not accessible outside of the function


# f = open('sample.txt', 'r')
# contents = f.read()
# print(contents)

# f = open('sample.txt',"w")
# overwrite = f.write('Hi world')

# f = open('myfile.txt', 'a')
# overwrite = f.write('Hello, world!')

# print(overwrite)

# with open('myfile.txt', 'r') as f:
#     contents = f.read()
#     print(contents)

# f = open("myfile.txt","r")
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)

# f = open('myfile.txt', 'w')
# lines = ['line 1\n', 'line 2\n', 'line 3\n']
# f.writelines(lines)
# f.close()

# f = open('myfile.txt','w')
# lines = ['line 1', 'line 2', 'line 3']
# for line in lines:
#     f.write(line + '\n')
# f.close()


# # seek
# with open('myfile.txt', 'r') as f:
#   # Move to the 10th byte in the file
#   f.seek(10)

#   # Read the next 5 bytes
#   data = f.read(5)
#   print(data)

# # tell()
# with open('myfile.txt', 'r') as f:
#   # Read the first 10 bytes
#   data = f.read(10)

#   # Save the current position
#   current_position = f.tell()

#   # Seek to the saved position
#   f.seek(current_position)

# # truncate()
# with open('sample.txt', 'w') as f:
#   f.write('Hello World!')
#   f.truncate(5)

# with open('sample.txt', 'r') as f:
#   print(f.read())

# # Lambda functions
# # Function to double the input
# def double(x):
#   return x * 2
# # Lambda function to double the input
# lambda x: x * 2

# # Function to calculate the product of two numbers
# def multiply(x, y):
#     return x * y
# # Lambda function to calculate the product of two numbers
# lambda x, y: x * y

# # Lambda function to calculate the product of two numbers,
# # with additional print statement
# lambda x, y: print(f'{x} * {y} = {x * y}')

# # Map, Filter and Reduce

# # map
# # List of numbers
# numbers = [1, 2, 3, 4, 5]

# # Double each number using the map function
# doubled = map(lambda x: x * 2, numbers)

# # Print the doubled numbers
# print(list(doubled))

# # filter
# # List of numbers
# numbers = [1,2,3,4,5]

# # Get only the even numbers using the filter function
# evens = filter(lambda x: x % 2 == 0, numbers)

# #Print the even numbers
# print(list(evens))

# # reduce
# from functools import reduce

# # List of numbers
# numbers = [1, 2, 3, 4, 5]

# # Calculate the sum of the numbers using the reduce function
# sum = reduce(lambda x, y: x + y, numbers)

# # Print the sum
# print(sum)

# # 'is' vs '==' in Python

# a = [1, 2, 3]
# b = [1, 2, 3]

# print(a == b)  # True
# print(a is b)  # False

# a = "hello"
# b = "hello"

# print(a == b)  # True
# print(a is b)  # True

# a = 5
# b = 5

# print(a == b)  # True
# print(a is b)  # True

# # Introduction to Object-oriented programming

# # Python Class and Objects
# class Details:
#     name = "Rafey"
#     age = 23

# obj1 = Details()
# print(obj1.name)
# print(obj1.age)

# # self parameter
# class Details:
#     name = "Rafey"
#     age = 23

#     def desc(self):
#         print("My name is", self.name, "and I'm", self.age, "years old.")

# obj1 = Details()
# obj1.desc()

# # Constructors

# # parameterized constructor
# class Details:
#     def __init__(self, animal, group):
#         self.animal = animal
#         self.group = group

# obj1 = Details("Crab", "Crustaceans")
# print(obj1.animal, "belongs to the", obj1.group, "group.")

# # default constructor
# class Details:
#   def __init__(self):
#     print("Crab belongs to Crustaceans group")
# obj1=Details()

# # Python Decorators
# import logging

# def log_function_call(func):
#     def decorated(*args, **kwargs):
#         logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
#         result = func(*args, **kwargs)
#         logging.info(f"{func.__name__} returned {result}")
#         return result
#     return decorated

# @log_function_call
# def my_function(a, b):
#     return a + b

# def greet(fx):
#   def mfx(*args, **kwargs):
#     print("Good Morning")
#     fx(*args, **kwargs)
#     print("Thanks for using this function")
#   return mfx

# @greet
# def hello():
#   print("Hello world")

# @greet
# def add(a, b):
#   print(a+b)
  
# # greet(hello)()
# hello()
# # greet(add)(1, 2)
# add(1, 2)
