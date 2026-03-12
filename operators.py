#swapping of two numbers without  using temporary variable
a = 5
b = 10
a,b = b,a
print(a,b)

output:
10 5


a = 5
b = 10
a = a+b
b = a-b
a = a-b
print(a,b)
output:
10 5

#salary dedection calculator
basic_salary = int(input("enter your salary"))
tax = basic_salary * 0.10
insurance = basic_salary * 0.05
net_salary = basic_salary-tax-insurance
print("Net salary", net_salary)

if net_salary > 50000:
    print("HIGH INCOME")
else:
    print("STANDARD SALARY")

output:
enter your salary 60000
Net salary 51000.0
HIGH INCOME


#finfing the largest of three numbers
a = int(input("enter a value"))
b = int(input("enter b value"))
c = int(input("enter c value"))

if a > b and a > c:
    print("The largest is:", a)
elif b > a and b > c:
    print("The largest is:", b)
else:
    print("The largest is:", c)

output:
enter a value 10
enter b value 20
enter c value 15
The largest is: 20

#check even or odd
num = int(input("enter a number"))
if (num // 2) * 2 == num:
    print("even")   
else:
    print("odd")

output:
enter a number 7
odd

n = 10
for i in range(1, n+1):
    print(i, end=" ")
output:
1 2 3 4 5 6 7 8 9 10

m = 10
n = 20
for i in range(m,n+1):
    print(i, end=" ")
output:
10 11 12 13 14 15 16 17 18 19 20

n = 10
for i in range(10,1,-1):
    print(i, end=" ")
output:
10 9 8 7 6 5 4 3 2


