# Q1- Write a Python program which accepts the user's first and last name and print them in
# reverse order with a space between them.

# Answer:

# fname = input("write your Firstname :")
# lname = input("write your Lastname :")

# Fullname = (lname + " " + fname)

# print(f"your Full name is {Fullname}")

# -------------------------------------------------------------------------------------------------

# Q2- Write a Python program that accepts an integer (n) and computes the value of
# n+nn+nnn. 
# Sample value of n is 5
# Expected Result : 615

# Answer:

# n = int(input("enter the number n :"))
# nn = int(str(n*2))
# nnn = int(str(n*3))

# total = n + nn + nnn

# print(f"Sample value of n is {n}")
# print(f"Expected Result : {total}")

# -------------------------------------------------------------------------------------------------

# Q3- 3- Write a Python program to print the following here document.
# Sample string :
# a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example

# Answer:

# print('''Sample string :
#     a string that you "don\'t" have to escape 
#     This 
#     is a ....... multi-line heredoc
#     string --------> example''')

# -------------------------------------------------------------------------------------------------

# Q4- Write a Python program to get the volume of a sphere with radius 6.

# Answer:

# equation v=4/3*3.14*math.pow(r,3)

# radius = int(6)
# pi = float(3.14)
# # radius ** 3 means exponential like math.pow(radius , 3)
# Volume = 4/3 * pi * (radius**3)

# print(f"the Volume of the sphere is : {Volume}")

# -------------------------------------------------------------------------------------------------

# Q5- Write a Python program that will accept the base and height of a triangle and compute
# the area.

# Answer:

# equation = 1/2*base*height

# base = int(input("what is the base of the triangle :"))
# height = int(input("what is the height of the triangle :"))

# Area = 1/2 * base * height

# print(f"the Area of the triangle is : {Area}")


# -------------------------------------------------------------------------------------------------

# Q6- Write a Python program that will accept the base and height of a triangle and compute
# the area.

# Answer:

# rows = 5
# for i in range(0,rows):
#     for j in range(0, i + 1):
#         print("*",end="")
#     print()
# for i in range(rows,0, -1):
#     for j in range(0, i - 1):
#         print("*",end="")
#     print()

# -------------------------------------------------------------------------------------------------

# Q7- Write a Python program that accepts a word from the user and reverse it.


# Answer:


# word = input("hello user can you give me a word :")

# word = word[::-1]

# print(f"the reverse of what you entered is {word}")

# -------------------------------------------------------------------------------------------------

# Q8- Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.


# Answer:

# for i in range(0,7):
#     if i == 3 or i == 6:
#         continue
#     print(i)    

# -------------------------------------------------------------------------------------------------

# Q9- Write a Python program to get the Fibonacci series between 0 to 50
# Note : The Fibonacci Sequence is the series of numbers :
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Every next number is found by adding up the two numbers before it.
# Expected Output : 1 1 2 3 5 8 13 21 34


# Answer:

# n = 0
# m = 1

# while n < 50:
#     print(n)
#     n, m = m, n + m


# -------------------------------------------------------------------------------------------------

# Q10- Write a Python program that accepts a string and calculate the number of digits and letters


# Answer:

# digits = 0
# letters = 0
# word = input("enter the string you want :")

# for char in word:
#     if char.isdigit:
#         digits +=1
#     if char.isalpha:
#         letters +=1


# print(f'the word you entered is "{word}" has "{digits}" numberof digits and "{letters}" number of letters')