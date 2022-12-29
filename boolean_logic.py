'''and operator---> It is True, if both conditions evaluate to True'''

# if (1 == 1) and (2 + 2 > 3):
#   print("true")
# else:
#   print("false")

'''or operator---> It is True if either (or both) of its conditions are True, 
and False if both conditions are False.'''

# print( 1 == 1 or 2 == 2 )
# True
# print( 1 == 1 or 2 == 3 )
# True
# print( 1 != 1 or 2 == 2 )
# True
# print( 2 < 1 or 3 > 6 )
# False

'''The not operator works a little differently. 
not takes just one argument, and inverts it.

The result of not True is False, and not False goes to True'''

# print(not 1 == 1)
# False
# print(not 1 > 7)
# True

# if not True:
#    print("1")
# elif not (1 + 1 == 3):
#    print("2")
# else:
#    print("3")

'''What is the result of this condition, when''' 
# hour = 9 
# day = 23
# if (hour > 12 and day <= 15) or (hour < 10):
#     print("True")
# else:
#     print("False")

'''Given the age of a person as an input, output their age group.
Here are the age groups you need to handle:

Child: 0 to 11
Teen: 12 to 17
Adult: 18 to 64'''

age = int(input())
if(age>=0 and age<=11):
    print("Child")
elif(age>=12 and age<=17):
    print("Teen")
elif(age>=18 and age<=64):
    print("Adult")