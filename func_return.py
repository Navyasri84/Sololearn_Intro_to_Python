# def sum(x, y):
#   return x+y
# res = sum(42, 7)
# print(res)

# def foo(x, y):
#   if x >= y:
#     return x
#   else:
#     return y
# x = foo(4, 7)
# print(x)

# def max(x, y):
#   if x >=y:
#     return x
#   else:
#     return y
# if(max(6, 4) > 10):
#   print("Yes")
# else:
#   print("Nope")

# def add_numbers(x, y):
#   total = x + y
#   return total
#   print("This won't be printed")
# print(add_numbers(4, 5))

# def print_numbers():
#     print(1)
#     print(2)
#     return
#     print(4)
#     print(6)
# print_numbers()

'''A function can only return once, thus, if you need to return multiple values, 
you can use a list.'''
# def double(a, b):
#   return [a*2, b*2]
# x = double(6, 9)
# print(x)

# def calc(x, y):
#    return [x+y, x*y]
# res = calc(3, 4)
# print(res[1])

"""We need to calculate the area of a given rectangle.
Your program needs to take the width and length as input and output the area of 
the rectangle."""
# def area(x,y):
#    return x*y
# w = int(input())
# h = int(input())
# print(area(w,h))

# def sum(x):
#     res = 0
#     for i in range(x):
#         res+=i
#     return res
# print(sum(4))

# def print_nums(x):
#   for i in range(x):
#     print(i)
#     return
# print_nums(10)

# def func(x):
#   res = 0
#   for i in range(x):
#      res += i
#   return res
# print(func(3))

"""The given code takes a text and a word as input and passes them to a function called 
search().
The search() function should return "Word found" if the word is present in the text, or 
"Word not found", if it’s not."""
text = input()
word = input()
def search(text, word):
    if word in text:
        return "Word found"
    else:
        return "Word not found"
print(search(text, word))