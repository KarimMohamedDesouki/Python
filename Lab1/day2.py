import random
# Q1- Given a list of numbers, create a function that returns a list where all similar adjacent
# elements have been reduced to a single element, so [1,2,3.3] returns [1,2,3]
# Note:
# You may create a new list or modify the passed in list.


# Answer:
# newnumbers = []
# numbers = [1,2,3.3,4,5.6,6,7]

# for num in numbers:
#     newnum = int(num)
#     newnumbers.append(newnum)
# print(numbers)
# print(newnumbers)


# -------------------------------------------------------------------------------------------------

# Q2- Consider dividing a string into two halves
# Case1:
# The length is even, the front and back halves are the same length.
# Case2:
# The length is odd, we’ll say that the extra char goes in the front half.
# E.g. ‘abced’, the front half is ‘abc’, the back half’de.
# Given 2 strings, a and b, return a string of the form:
# (a-front + b-front) + (a-back +b-back)


# Answer:

# def divide_string(a, b):
#     # Calculate the midpoint index of each string
#     mid_a = len(a) // 2
#     mid_b = len(b) // 2
    
#     # Divide the strings into front and back halves
#     a_front = a[:mid_a + len(a) % 2]  # Handle odd length
#     a_back = a[mid_a + len(a) % 2:]
    
#     b_front = b[:mid_b + len(b) % 2]  # Handle odd length
#     b_back = b[mid_b + len(b) % 2:]
    
#     # Concatenate the front and back halves of both strings
#     result = a_front + b_front + a_back + b_back
    
#     return result

# # Test cases
# a = "abcde"
# b = "12345"
# print(divide_string(a, b))  # Output: "abc123de45"


# -------------------------------------------------------------------------------------------------

# Q3- Write a Python function that takes a sequence of numbers and determines
# whether all the numbers are different from each other.
# E.X. [1,5,7,9] -> True
# [2,4,5,5,7,9] -> False


# Answer

# a = [1,2,3,4,5,6]

# def compare(list):
#     for i in range(len(list)):
#         for j in range(i+1,len(list)):
#             if list[i]==list[j]:
#                 return False 
#     return True

# print(compare(a))


# -------------------------------------------------------------------------------------------------

# Q4- Given unordered list, sort it using algorithm bubble sort
# ( read about bubble sort and try to implement it)


# Answer

# def bubbleSort(arr):
#     n = len(arr)
#     for i in range(n-1):

#         swapped = False
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j + 1]:
#                 swapped = True
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]

#         if not swapped:
#             return


# # Driver code to test above
# arr = [64, 34, 25, 12, 22, 11, 90]

# bubbleSort(arr)

# print("Sorted array is:")
# for i in range(len(arr)):
#     print("% d" % arr[i], end=" ")


# -------------------------------------------------------------------------------------------------

# Q5- Given unordered list, sort it using algorithm bubble sort
# whether all the numbers are different from each other.
# E.X. [1,5,7,9] -> True
# [2,4,5,5,7,9] -> False


# Answer


# def guess_number_game():
#     # Generate a random number between 1 and 100
#     random_number = random.randint(1, 100)
#     tries = 10
#     guessed_numbers = set()

#     print("Welcome to the Number Guessing Game!")

#     while tries > 0:
#         guess = input("\nEnter your guess (1-100): ")
        
#         # Check if the input is within the valid range
#         if not guess.isdigit() or int(guess) < 1 or int(guess) > 100:
#             print("Please enter a number between 1 and 100.")
#             continue
        
#         guess = int(guess)
        
#         # Check if the guess has been entered before
#         if guess in guessed_numbers:
#             print("You have already guessed that number. Try again.")
#             continue

#         # Decrement the number of tries
#         tries -= 1
        
#         # Add the guess to the set of guessed numbers
#         guessed_numbers.add(guess)
        
#         # Compare the guess with the random number
#         if guess < random_number:
#             print("Your guess is too low. Try again.")
#         elif guess > random_number:
#             print("Your guess is too high. Try again.")
#         else:
#             print("Congratulations! You guessed the number correctly!")
#             break

#     if tries == 0:
#         print(f"\nYou ran out of tries. The correct number was {random_number}.")

#     play_again = input("\nDo you want to play again? (yes/no): ")
#     if play_again.lower() == "yes":
#         guess_number_game()
#     else:
#         print("Thank you for playing!")

# guess_number_game()




