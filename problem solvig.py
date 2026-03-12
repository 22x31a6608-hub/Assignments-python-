#rat problem
def min_houses(r, unit, arr):
    if arr is None:
        return -1
    
    food_required = r * unit
    food_collected = 0
    
    for i in range(len(arr)):
        food_collected += arr[i]
        if food_collected >= food_required:
            return i + 1
    return 0
# Example
r = 7
unit = 2
arr = [2, 8, 3, 5, 7, 4, 1, 2]

print(min_houses(r, unit, arr))

output:
4


#Nearest Prime:
def nearest_prime(n):
    if n <= 1:
        return 2
    lower = n - 1
    upper = n + 1
    while True:
        if is_prime(lower):
            return lower
        if is_prime(upper):
            return upper
        lower -= 1
        upper += 1
num = int(input("Enter a number: "))
result = nearest_prime(num)     
print("Nearest prime number:", result)
output:Enter a number: 10
Nearest prime number: 11


#check whether the string is palindrome or not
string = input("Enter a string: ")
if string == string[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

output: 
Enter a string: madam
Palindrome
