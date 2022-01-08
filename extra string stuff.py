# slicing strings
print("--- slicing strings ---")
print("--- 1st Example ---")

b = "sandwich"
print(b[2:5])
# this prints the elements that are in the index 2 - 5 so its 3, 4, 5
# this is how it looks like (remember that starts at 0) :
# sandwich
# 01234567
#   !!!!
print("--- 2nd example ---")
a = "pycharm"
print(a[2:])
# this prints from index 2 to the end
# pycharm
# 0123456
#   !!!!!

print("--- 3rd example ---")
g = "Hello"
print(g[-5:-2])
# this prints from index -5 to -2
# Hello
# this is how negative indexes work. I highly suggest searching "index in python" and going to images
# -5, -4, -3, -2, -1
# 0, 1, 2, 3, 4, 5

# Modify Strings
print("--- modify strings ---")
print("--- 1st example ---")

# this just converts the characters to uppercase
p = "Hello, World!"
print(p.upper())

# .lower converts the characters to lower case
# .strip deletes white spaces
print("--- 2nd example ---")

ap = " Hello, World! "
print(ap.strip()) # returns "Hello, World!"

print("--- 3rd example --- ")
# .replace replaces the first value in the parenthesis with the 2nd value.
aq = "Hello, World!"
print(aq.replace("H", "J")) # H is the first value and J is the 2nd value

# .split separate words in a string
print("--- 4th example ---")
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

# string concatenation
# the empty space between is an element in python so it prints that too
print("--- 1st example ---")
o = "Hello"
l = "World"
hj = o + " " + l
print(hj)

