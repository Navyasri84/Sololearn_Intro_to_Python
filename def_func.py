'''Functions
You can create your own functions by using the def statement.'''
# def my_func():
#   print("spam")
#   print("spam")
#   print("spam")
# my_func()

'''once you’ve defined a function, you can call it multiple times in your code.'''
# def hello():
#   print("Hello world!")
# hello()
# hello()
# hello()

'''The function needs to be defined before it can be called. Calling a function 
before its definition will cause an error.'''
# hello()

# def hello():
#   print("Hello world!")

"""We have a function that outputs "Welcome, user" as it is called. We want to make it 
more personalized, so redesign the given function so that it will take the name of the 
user as input and output the welcome message with it."""
# name=input()
# def welcome(name):
#    print("Welcome, "+name)
# welcome(name)

'''Arguments
Functions can take arguments, which can be used to generate the function output.'''

# def exclamation(word):
#   print(word + "!")
# exclamation("spam")

# def print_double(x):
#    print(2 * x)
# print_double(3)

'''You can call the same function with different arguments.'''
# def exclamation(word):
#   print(word + "!")

# exclamation("spam")
# exclamation("eggs")
# exclamation("python")

'''you can define functions with more than one argument; separate them with commas. '''
# def print_sum_twice(x, y):
#   print(x + y)
#   print(x + y)

# print_sum_twice(5, 8)

"""The given program defines a function printBill(), which takes one string argument 
and outputs formatted text.
You need to take the user input and call the function by passing the input as its argument.
"""
# def printBill(text):
 
#   print("======")
#   print(text)
#   print("======")
# text=input()
# printBill(text)

# def msg(num, ch):
#   print(ch+str(num))
# msg(18, 'A')