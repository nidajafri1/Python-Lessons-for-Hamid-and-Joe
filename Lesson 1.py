# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 15:01:32 2020

@author: n.jafri
"""
#Homework:
    #1) Go

#1) Lists and its built-in functions, appending, pop, removing and del, 
#           setting the variable again, indexing
#2) iterating through lists - for loops and break and continue
#3) functions - raise exceptions
#4) scoping

#lists [] #append, #pop (deletes last function), #index

l = [3, 4, 5, 100, 1000, "krish"]
shopping_list = ["apples", "weetabix", "bottle opener", "shaving cream"]

l = [3, 4, 5, 1000] #a simple list

print(l) #rpint out to view data type, length, object

print(type(l))
print(len(shopping_list))

print(type(l))
print(len(l))

l.append("krish") #add element
l[2] = 2 #change element
l.remove("krish") #remove element
del l[1:2] #remove element

print(shopping_list[:2])
print(l[2]) #indexing
print(l[0:1])

for element in l:
    print(element)

for element in l: #iterating, for loops
    print(l)
    
for element in l: #break - stops iterating after first element
    if element > 2:
        print(element)
        break

for element in l: #continue
    if element > 1:
        print('found!')
        continue
    
for i in range(start, stop, break):
    
for i in range(2, 10, 3):
    print(i)

for i in shopping_list[0:2]:
    print(i)

#the instruction is range(start, stop[, step])
for i in range(2, 100, 2): #range
    print(i, end = ',')
    
#while loops and scoping
x = 0

def haha():
    x=0
    
while x < 10: #you must break
    #x=0
    print(x)
    x += 1
    
while True: #infinite loop, interrupt by ctrl c
    print(x)
    x += 1
    x = x+1
    
#functions - define function by def and put in your argument 
            #in the paranthesis
#type hinting is important

def hello(name):
    print("Hello function.", name)

print("Hello function. Joe")    
print("Hello function. Pro")
print("Hello function. Gemma")
print("Hello function. Mich")
    
hello("Joe")
hello("Provhat")
hello("Gemma")
hello("Michelle")  #DRY, do not repeat yourself. 
                    #You can just edit it within variables
                    
#functions with positional arguments

#see here, instead of printing a hard-coded greeting and name, you can make
#them into variables.

def greet(greeting, name):
    return '{}, how are you, {}'.format(greeting, name)

greet('hello', 'hamid')


def greet(greeting, name):
    return '{}. How are you, {}'.format(greeting, name)

#Next week, remind me to cover *args and **kwargs

def addd(x, y):
    return x+y

addd(2, 3)

def addd(*args):
    my_sum = 0
    for i in args:
        my_sum += i
    return my_sum
        
addd(2, 3, 4 ,5 ,6, 100000)

def pascal():
    i = 1
    