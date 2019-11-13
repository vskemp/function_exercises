# FUNCTION EXERCISES

#////////////////////////////////////////////////
            # EASY LEVEL
#////////////////////////////////////////////////

# In Python, you create a function by:
# 1. Using the def keyword
# 2. Naming the function
# 3. Declaring parameters ("ingredients")
# 4. Providing the body of the function as a code block

# MADLIB

# Write a function that accepts two arguments: a name and a subject.
# The function should return a String with the name and subject interpolated in.


# input_1 = input("Give me a name! ")
# input_2 = input("Give me a subject! ")
# madlib = ((input_1) + "'s favorite subject is " + (input_2) + ".")
# print(madlib)


# def madstr(name, subject):
#     return f"{name}'s favorite subject is {subject}."
# print(madstr("Vero", "math"))
# print(madstr("chris", "history"))
# print(madstr(input("Give me a name! "), input("Give me a subject! ")))


# //////////////////////////////////////////////

# 3. Fahrenheit to Celsius conversion
# 2. Celsius to Fahrenheit conversion


# Write a function that takes a temperature in 
# Celsius, converts it Fahrenheit, and returns
# the value. AND VICE VERSA

# temp = int(input("What is the temperature?\n"))
# unit = str(input("Please enter the unit of measure (f or c):\n"))


# def convert(temp, unit):
#     if unit == "c":
#         temp = 9.0 / 5.0 * temp + 32
#         return "%s degrees Fahrenheit"% temp
#     if unit == "f":
#         temp = (temp - 32)  / 9.0 * 5.0
#         return "%s degrees Celsius"% temp

# print(convert(temp, unit))

# /////////////////////////////////////////////

# 4. is_even function
# Write a function that accepts a number 
# as an argument and returns a Boolean value. 
# Return True if the number is even;
# return False if it is not even.

# user_num = int(input("Give me a number! Is it even? "))
# def is_even(user_num):
#     if user_num % 2 == 0:
#         return True
#     else:
#         return False
# print(is_even(user_num))

# //////////////////////////////////////////////

# 5. is_odd function
# Write an is_odd function that uses your is_even function to determine if a number is odd. (That is, do not do the calculation - call a function that does the calculation.)

# Hint: You'll use the not keyword
# user_num = int(input("Give me a number! Is it odd? "))
# def is_odd(user_num):
#     if user_num % 2 == 0:
#         return not True
#     else: 
#         return not False
# print(is_odd(user_num))

#////////////////////////////////////////////////

# 6. only_evens function
# Write a function that accepts a List of numbers as an argument.
# Return a new List that includes only the even numbers.
# Messed around and made sure you could put in a string input and make it an intager list

# def is_even(user_num):
#     if user_num % 2 == 0:
#         return True
#     else:
#         return False

# list3 = []
# list2 = input("Give me an list of numbers! I'll give you the even ones back! ")
# print(list2)
# print(list2.split(" "))

# for str1 in list2.split(" "):
#     list3.append(int(str1))


# def even_list(arr):
#     evens = []
#     for number in arr:
#         if is_even(number):
#             evens.append(number)
#     return evens
# print(even_list(list3))

#/////////////////////////////////////////////

# Write a function that accepts a List of numbers as an argument.
# Return a new List that includes only the odd numbers.
# Hint: use your is_odd() function to determine which numbers to include in your new List.

# def is_odd(user_num):
#     if user_num % 2 == 0:
#         return not True
#     else: 
#         return not False

# list3 = []
# list2 = input("Give me a list of numbers! I'll give you the odd ones back! ")
# print(list2)
# print(list2.split(" "))

# for str1 in list2.split(" "):
#     list3.append(int(str1))


# def odd_list(arr):
#     odd = []
#     for number in arr:
#         if is_odd(number):
#             odd.append(number)
#     return odd
# print(odd_list(list3))

#////////////////////////////////////////////
            #MEDIUM LEVEL
#///////////////////////////////////////////

# 1. Find the smallest number
# Write a function 'smallest' that accepts a 'List of numbers' as an argument.
# It should return the smallest number in the List.

# list_of_numbers = [4, 2, 7, 23, 45, 12, 87, 35, 35]

# def smallest(list_to_small):
#     min = list_of_numbers[0]
#     for num_small in list_to_small:
#         if num_small < min:
#             min = num_small
#     return min
# print(smallest(list_of_numbers))

#//////////////////////////////////////////

# 2. Find the largest number
# Write a function 'largest' that accepts a 'List of numbers' as an argument.

# It should return the largest number in the List.

# list_of_numbers = [6, 23, 0, 26, 98, 65, 37, 28, 67, 3]

# def largest(list_to_large):
#     max = list_of_numbers[0]
#     for num_large in list_to_large:
#         if num_large > max:
#             max = num_large
#     return max
# print(largest(list_of_numbers))

#////////////////////////////////////////////

# 3. Find the shortest String
# Write a function 'shortest' that accepts a 'List of Strings' as an argument.
# It should return the shortest String in the List.

# shortest "accepts" a list of strings
# or shortest "expects to recieve" a list of strings

# some_words = ["Booger", "Toby", "Sally", "Clark", "Nanoo", "Mochi"]

# def shortest(word_list):
#     # assume the first one is the shortest
#     the_shortest = word_list[0]
#     # work through the list
#     #or check every item on the list
#     for word in word_list:
#         if len(word) < len(the_shortest):
#         # compare lengths
#         #if we find one that is shorter, we "save" that as the new "shortest"
#             the_shortest = word
#     return the_shortest
# the_word = shortest(some_words)
# print(the_word)

#///////////////////////////////////////////

# 4. Find the longest String
# Write a function longest that accepts a List of Strings as an argument.

# It should return the longest String in the List.

# some_words = ["Booger", "Toby", "Sally", "Clark", "Nanoo", "Mochi"]

# def longest(word_list):
#     the_longest = word_list[0]
#     for word in word_list:
#         if len(word) > len(the_longest):
#             the_longest = word
#     return the_longest
# the_word = longest(some_words)
# print(the_word)
