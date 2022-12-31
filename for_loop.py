'''The for loop is used to iterate over a given sequence, such as lists or strings.'''

# words = ["hello", "world", "spam", "eggs"]
# for word in words:
#   print(word + "!")

# nums=[4, 7, 3, 1]
# for x in nums:
#     print(x*2)

# str="testing for loops"
# i=0
# for x in str:
#   if(x=='t'):
#     i+=1
# print(i)

'''Similar to while loops, the break and continue statements can be used in for loops, 
to stop the loop or jump to the next iteration.'''

# text="some text"
# for x in text:
#   if x=='e':
#     break
#   print(x)

# list=[2, 3, 4, 5, 6, 7]
# for x in list:
#    if(x%2==1 and x>4):
#       print(x)
#       break

'''The for loop is useful when the number of iterations is fixed. For example, 
iterating over a fixed list of items in a shopping list.

The while loop is useful in cases when the number of iterations isn’t known and 
depends on some calculations and conditions in the code block of the loop. For example, 
ending the loop when the user enters a specific input in a calculator program.'''

"""Given a list of numbers, calculate their sum using a for loop."""
# x = [42, 8, 7, 1, 0, 124, 8897, 555, 3, 67, 99]
# sum=0
# for num in x:
#     sum+=num
# print(sum)

# nums=[1, 2, 3, 4]
# res=0
# for x in nums:
#     if(x%2==0):
#         continue
#     else:
#         res+=x
# print(res)

# for i in range(10):
#   if not i%2==0:
#     print(i+1)

""" Find the sum of the first N numbers."""
# N=int(input())
# sum=0
# for i in range(0,N+1):
#     sum+=i
# print(sum)