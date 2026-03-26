num = int(input("Enter number: "))
flag = True

if num <= 1:
    flag = False
else:
    for i in range(2, num):
        if num % i == 0:
            flag = False
            break

if flag:
    print("Prime")
else:
    print("Not Prime")

output:
Enter number: 122
Not Prime


num = input("Enter number: ")

if num == num[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
output:
Enter number: 121
Palindrome

num = int(input("Enter number: "))
temp = num
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
output:
Enter number: 122
Not Palindrome

num = int(input("Enter number: "))
rev = int(str(num)[::-1])

if num == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

output:
Enter number: 158
Not Palindrome

num = int(input("Enter number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

output:
Enter number: 8745
Odd

n = int(input("Enter number: "))
sum = 0

for i in range(n, 0, -1):
    sum += i

print("Sum:", sum)
output:
Enter number: 18
Sum: 171

lst = [2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in lst:
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num, end=" ")
        
output:
2 3 5 7

import math

num = int(input("Enter number: "))
flag = True

if num <= 1:
    flag = False
else:
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            flag = False
            break

print("Prime" if flag else "Not Prime")

output:
Enter number: 25
Not Prime
