#string reverse using slicing
Text = "Manishavinay"
reverse = Text[::-1]
print("Reversed string:", reverse)

output:
Reversed string: yanivaHsinam

#reverse string using for loop
Text = "VINAYKUMAR"
reverse = ""
for i in Text:
    reverse = i + reverse
print("Reversed string=", reverse)
output:
Reversed string= RAMUKYANIV

#srting reverse using if,else
Text = "malayalam"
reverse = ""
for i in Text:
    reverse = i + reverse
print("Reversed string=", reverse)


if reverse == Text:
    print("it's a palindrome")
else:
    print("Not a palindrome")

output:
Reversed string= malayalam

#sum of digits using while loop
num = int(input("Enter a number: "))
sum = 1

while num > 0:
    digit = num % 10
    sum = sum * digit
    num = num // 10

print("Sum of digits:", sum)
output:
Enter a number: 123
Sum of digits: 6

#armstrong number check
num = int(input("Enter a number: "))
temp = num
sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit ** 3
    num = num // 10

if sum == temp:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
output:
Enter a number: 153 

#reverse of a number
num = 1234
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
print("reverse of number:", reverse)
output:
reverse of number: 4321

#palindrome number check
num = 1331
reverse = 0
temp = num
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if temp == reverse:
    print("Number is palindrome")
else:
    print("Number is not palindrome")
output:
Number is palindrome


#Count Vowels in String
Text = "Hello world"
vowels = "aeiouAEIOU"
count = 0
for i in text:
    if i in vowels:
        count += 1
print("Number of vowels in the string:", count)
output:
Number of vowels in the string: 3

# Count Consonants in String
Text = "Hello world"
vowels = "aeiouAEIOU"
count = 0
for i in Text:
    if  i.isalpha and i not in vowels:
        count += 1
print("Number of consonants in the string:", count)
output:
Number of consonants in the string: 7

#Perfect Number Check
num = 28
sum = 0
for i in range(1, num):
    if num % i == 0:
        sum += i
if sum == num:
    print(" 28 is a Perfect number") 
else:
    print("28 is Not a perfect number")

output:
    28 is a Perfect number

#neon number check
num = 9
square = num ** 2
sum_of_digits = 0
while square > 0:
    digit = square % 10
    sum_of_digits += digit
    square //= 10
if sum_of_digits == num:
    print("Neon number")
else:
    print("Not a neon number")
output:
Neon number

#Strong Number Check
num = 145
temp = num
sum = 0
while num > 0:
    digit = num % 10
    factorial = 1
    for i in range(1, digit + 1):
        factorial *= i
    sum += factorial
    num //= 10
if sum == temp:
    print("Strong number")
else:
    print("Not a strong number")

output:
Strong number

#Harshad Number Check
num = 18
sum_of_digits = 0
temp = num
while num > 0:
    digit = num % 10
    sum_of_digits += digit
    num //= 10
if temp % sum_of_digits == 0:
    print("Harshad number")
else:
    print("Not a Harshad number")

output:
Harshad number

