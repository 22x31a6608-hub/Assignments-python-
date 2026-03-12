#time and space complexity for prime check
def is_prime(n):
    # numbers less than 2 are not prime
    if n < 2:
        return False
    
    # check divisibility up to square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True


num = int(input("Enter a number: "))

if is_prime(num):
    print("Prime number")
else:
    print("Not a prime number")

output:
Enter a number: 7
Prime number

#check palindrome for 3 approaches
def is_palindrome_string(s):
    return s == s[::-1]
def is_palindrome_iterative(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True 
def is_palindrome_recursive(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome_recursive(s[1:-1])
word = input("Enter a word: ")
if is_palindrome_string(word):
    print("Palindrome (String Reversal)")
else:
    print("Not a palindrome (String Reversal)")
if is_palindrome_iterative(word):
    print("Palindrome (Iterative)")
else:
    print("Not a palindrome (Iterative)")
if is_palindrome_recursive(word):
    print("Palindrome (Recursive)")
else:
    print("Not a palindrome (Recursive)")
output:
Enter a word: radar
Palindrome (String Reversal)
Palindrome (Iterative)
Palindrome (Recursive)

#check number is even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
output:
Enter a number: 8
Even

#sum of numbers from 1 to n
n = int(input("Enter a number: "))
total = 0
for i in range(1, n + 1):
    total += i
print("Sum of numbers from 1 to", n, "is:", total)
output:
Enter a number: 5
Sum of numbers from 1 to 5 is: 15

#print primes from a list
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
numbers = [10, 15, 2, 3, 5, 7, 11]
primes = [num for num in numbers if is_prime(num)]  
print("Prime numbers in the list:", primes)
output:
Prime numbers in the list: [2, 3, 5, 7, 11]


