'''Lists are used to store items. 
We can create a list by using square brackets with commas separating items.'''

'''accessing any item can be acheived by using Indexing'''

# x = ["a", "b", "c"]
# y = [1, 2, 3, 4, 5]

# print(x[1])
# print(y[3])

'''Strings can be indexed like lists too!
Indexing a string is like creating a list containing each character in the string.'''

# str = "Hello world!"
# print(str[6])

# x = "Python"
# print(x[1] + x[4])

'''
Write a program that takes an input string and outputs the 3rd character of the string.'''

# s=input()
# print(s[2])

'''List operations'''

# nums = [5, 8, 2]
# nums[1] = 42
# print(nums)

# nums = [1,2,3,4,5]
# nums[3] = nums[1]
# print(nums[3])

# nums=[1,2,3]
# print(nums+[4,5,6])

# x=[2,4]
# x+=[6,8]
# print(x[2]//x[0])

# nums=[1,2,3]
# print(nums*3)

# nums=[4, 7, 3, 1]
# for x in nums:
#     print(x*2)

# a=[1,2,3,4]
# r=[x*2 for x in a]
# print(r)

# x=[2,4]
# x=x*3
# print(x)
# print(x[3])

# words=["spam","egg","spam","sausage"]
# print("spam" in words)
# print("egg" in words)
# print("tomato" in words)

# x="hello world"
# if "world" in x:
#   print("Yes")

# nums=[1,2,3]
# print(not 4 in nums)
# print(4 not in nums)
# print(not 3 in nums)
# print(3 not in nums)

# list = [1, 1, 2, 3, 5, 8, 13]
# print(list[list[4]])