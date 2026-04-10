#1. Write a Python program to reverse a given string using slicing.
string = "Hello, World"
reversed_string = string[::-1]  
print(reversed_string)
#output:
#dlroW ,olleH


#2. Write a Python program to print every alternate character from a given string using slicing.
string = "Hello, World"
alternate_characters = string[::2]
print(alternate_characters)
#output:
#Hlo ol


#3. Write a Python program to extract the middle three characters from a given string (assume the string length is odd and at least 3).
string = "Hello, World"
middle_three = string[len(string)//2 - 1:len(string)//2 + 2]
print(middle_three)
#output:
##llo

#4. Write a Python program to reverse a list of integers using slicing without using loops or built-in reverse functions.
list_of_integers = [1, 2, 3, 4, 5]
reversed_list = list_of_integers[::-1]
print(reversed_list)
#output:
[5, 4, 3, 2, 1]

#5. Write a Python program to remove the first and last characters from a given string using slicing.
string = "Hello, World"
modified_string = string[1:-1]
print(modified_string)
#output:
#ello, Worl
