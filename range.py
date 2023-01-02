'''Range
Python makes it super easy to create number sequences using the range() function.
By default, it starts from 0, increments by 1 and stops before the specified number.'''

# numbers = range(10)
# print(numbers)

# numbers = list(range(10))
# print(numbers)

# nums=list(range(5))
# print(nums[4])

'''If range is called with one argument, it’ll produce an object with values from 0 to that argument. 
If it’s called with two arguments, it’ll produce values from the first to the second.'''

# numbers=list(range(3,8))
# print(numbers)

'''There’s also a third argument you can use with range(), and it’s really useful. 
It’s called Step and it determines the interval of the sequence produced. '''

# numbers=list(range(5,20,2))
# print(numbers)

# nums=list(range(3,15,3))
# print(nums[2])

# x=list(range(7,3,-1))
# print(x)

# for i in range(5):
#   print("hello! "+str(i))

"""Write a program that takes two integers as input and outputs the range of numbers 
between the two inputs as a list."""

# a=int(input())
# b=int(input())
# num=list(range(a,b))
# print(num)
# print(num[4])