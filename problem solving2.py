1.Armstrong number
num = int(input("Enter number: "))
temp = num
n = len(str(num))
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** n
    temp //= 10

if sum == num:
    print("Armstrong Number")
else:
    print("Not Armstrong")

output:
Enter number: 500
Not Armstrong

2.Neon number
num = int(input("Enter number: "))
square = num * num
sum = 0

while square > 0:
    digit = square % 10
    sum += digit
    square //= 10

if sum == num:
    print("Neon Number")
else:
    print("Not Neon")

output:
Enter number: 850
Not Neon

output:
enter number: 9
neon


3.strong number
import math
num = int(input("Enter number: "))
temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    sum += math.factorial(digit)
    temp //= 10

if sum == num:
    print("Strong Number")
else:
    print("Not Strong")

output:
Enter number: 145
Strong Number

4.perfect number
num = int(input("Enter number: "))
sum = 0

for i in range(1, num):
    if num % i == 0:
        sum += i

if sum == num:
    print("Perfect Number")
else:
    print("Not Perfect")
output:
Enter number: 6
Perfect Number

5. Harshad Number
num = int(input("Enter number: "))
temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit
    temp //= 10

if num % sum == 0:
    print("Harshad Number")
else:
    print("Not Harshad")

output:
Enter number: 18
Harshad Number   