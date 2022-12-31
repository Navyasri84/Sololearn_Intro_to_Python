'''A function is a group of related statements that performs a specific task.
Functions help break our program into smaller and modular chunks. As our program grows 
larger and larger, functions make it more organized and manageable.
And functions make our code reusable.'''
# print("name")

'''Functions can have multiple arguments'''
# range(2,20)

'''List Functions'''
# nums=[1,3,5,2,4]
# print(len(nums))

# letters=["a","b","c"]
# letters+=["d"]
# print(len(letters))

# nums=[1,2,3]
# nums.append(4)
# print(nums)

# words=["Python","fun"]
# words.insert(1,"is")
# print(words)

# nums=[9,8,7,6,5]
# nums.append(4)
# nums.insert(2,11)
# print(len(nums))

# letters=['p','q','r','s','p','u']
# print(letters.index('r'))
# print(letters.index('p'))
# print(letters.index('q'))
# print(letters.index('t'))

# x=[1,8,42,3]
# print(min(x))
# print(max(x))

'''
list.count(item): Returns a count of how many times an item occurs in a list.
list.remove(item): Removes an item from a list.
list.reverse(): Reverses items in a list.'''
# x = [2, 4, 6, 2, 7, 2, 9]
# print(x.count(2))
# x.remove(4)
# print(x)
# x.reverse()
# print(x)

'''The queue is represented by a list. 
Write a program to take an input, add it to the end of the queue, and output the 
resulting list'''

# queue=['John','Amy','Bob','Adam']
# add=input()
# queue.append(add)
# print(queue)

# nums=[2,4,8,9,5]
# nums.insert(1,3)
# nums.remove(9)
# nums.insert(0,nums.count(8))
# print(nums[3])

'''string functions'''
# nums=[4,5,6]
# msg="Numbers:{0}{1}{2}".format(nums[0],nums[1],nums[2])
# print(msg)

# a="{x},{y}".format(x=5,y=12)
# print(a)

# x=", ".join(["spam","eggs","ham"])
# print(x)

'''split() is the opposite of join(). It turns a string with a certain separator 
into a list.'''
# str="some text goes here"
# x=str.split(' ')
# print(x)

# x="Hello ME"
# print(x.replace("ME","world"))

# print("This is a sentence.".upper())
# print("AN ALL CAPS SENTENCE".lower())

"""Replace all of the # characters in the given input with spaces and output the result"""
# msg=input()
# msg=msg.replace(' ','#')
# print(msg)