#!/usr/bin/env python3
#this is an exapmle of creating functions

#first we prompt the user for an input

name = input("greetings traveller what is your name? ")

#next we create a funtion to interpret the name and print hello next to it

def hello():
    response = (f"Hello {name}")
    print(response)

hello()  #this calls our newly created funtion.

#next we will ask the user for a number

number = int(input("what is your favorite number?  "))

#next create a function that takes that number and multiplies it by 11

def multiply():
    calculation = number * 11
    print(f"ahh well here it is multiplied by 11: {calculation}")
    return calculation


multiply()
