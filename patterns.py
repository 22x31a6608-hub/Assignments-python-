#Print a solid square of stars of size n.
n = int(input("enter a size"))
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()
output:
enter a size 4
* * * *
* * * *
* * * *
* * * *

#Solid Rectangle Pattern
m = int(input("enter number of rows"))
n = int(input("enter number of columns"))
for i in range(m):
    for j in range(n):
       print("*", end=" ")
    print()
output:
enter number of rows 4
enter number of columns 5
* * * * *
* * * * *
* * * * *
* * * * *

#Print a solid rectangle of m rows and n columns.
m = int(input("enter number of rows"))
n = int(input("enter number of columns"))
for i in range(m):
    for j in range(n):
       print("*", end=" ")
    print()
Output:
* * * * *
* * * * *
* * * * *


#Right-Angled Triangle (Left-Aligned)
n = int(input("enter a size"))
for i in range(1, n+1):
    for j in range(i):
        print("*", end=" ")
    print()
Output:
*
* *
* * *
* * * *
* * * * *
#Right-Angled Triangle (Right-Aligned)
n = int(input("enter a size"))
for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end=" ")
    for k in range(i):
        print("*", end=" ")
    print()

Output:
        *
      * *
    * * *
  * * * *
* * * * *

#Inverted Triangle (Left-Aligned)
n = int(input("enter a size"))
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
Output:
* * * * *
* * * *
* * *
* *
*


#Inverted Triangle (Right-Aligned)
n = int(input("enter a size"))
for i in range(n, 0, -1):
    for j in range(n-i):
        print(" ", end=" ")
    for k in range(i):
        print("*", end=" ")
    print()

Output:
* * * * *
  * * * *
    * * *
      * *
        *


#Centered Pyramid Pattern
n = int(input("enter a size"))
for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end=" ")
    for k in range(2*i-1):
        print("*", end=" ")
    print()

Output:
      *
    * * *
  * * * * *
* * * * * * *

#Diamond Pattern
n = int(input("enter a size"))
# Upper half of the diamond
for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end=" ")
    for k in range(2*i-1):
        print("*", end=" ")
    print()
# Lower half of the diamond
for i in range(n-1, 0, -1):
    for j in range(n-i):
        print(" ", end=" ")
    for k in range(2*i-1):
        print("*", end=" ")
    print()

Output:
    *
  * * *
* * * * *
  * * *
    *
#Butterfly Pattern
n = int(input("enter a size"))
# Upper half of the butterfly
for i in range(1, n+1): 
    for j in range(i):
        print("*", end=" ")
    for k in range(2*(n-i)):
        print(" ", end=" ")
    for l in range(i):
        print("*", end=" ")
    print()
# Lower half of the butterfly
for i in range(n, 0, -1):   
    for j in range(i):
        print("*", end=" ")
    for k in range(2*(n-i)):
        print(" ", end=" ")
    for l in range(i):
        print("*", end=" ")
    print()
Output:
*       *
* *   * *
* * * * *
* *   * *
*       *

#Left-Aligned Half Diamond
n = int(input("enter a size"))
# Upper half of the half diamond
for i in range(1, n+1):
    for j in range(i):
        print("*", end=" ")
    print()
# Lower half of the half diamond
for i in range(n-1, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
Output:
*
* *
* * *
* * * *
* * *
* *
*

#Right-Aligned Half Diamond
n = int(input("enter a size"))
# Upper half of the half diamond
for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end=" ")
    for k in range(i):
        print("*", end=" ")
    print()
# Lower half of the half diamond
for i in range(n-1, 0, -1):
    for j in range(n-i):
        print(" ", end=" ")
    for k in range(i):
        print("*", end=" ")
    print()

Output:
      *
    * *
  * * *
* * * *
  * * *
    * *
      *


#Sandglass Pattern
n = int(input("enter a size"))
# Upper half of the sandglass
for i in range(n, 0, -1):
    for j in range(n-i):
        print(" ", end=" ")
    for k in range(2*i-1):
        print("*", end=" ")
    print()
# Lower half of the sandglass
for i in range(2, n+1):
    for j in range(n-i):
        print(" ", end=" ")
    for k in range(2*i-1):
        print("*", end=" ")
    print()


Output:
* * * *
  * * *
    * *
      *
    * *
  * * *
* * * *
#Increasing Width Triangle
n = int(input("enter a size"))
for i in range(1, n+1):
    for j in range(i):
        print("*", end=" ")
    print()

Output:
*
* *
* * *
* * * *
* * * * *

#Decreasing Width Triangle
n = int(input("enter a size"))
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

Output:
* * * * *
* * * *
* * *
* *
*

#Right-Aligned Hill Pattern
n = int(input("enter a size"))
for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end=" ")
    for k in range(i):
        print("*", end=" ")
    print()

Output:
      *
    * *
  * * *
* * * *

#Hollow Square Pattern
n = int(input("enter a size"))
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
Output:
enter a size 4
* * * *
*     *
*     *
* * * *

#Hollow Rectangle Pattern
m = int(input("enter number of rows"))
n = int(input("enter number of columns"))
for i in range(m):
    for j in range(n):
        if i == 0 or i == m-1 or j == 0 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

Output:
* * * * *
*       *
*       *
* * * * *

#Hollow Right-Angled Triangle (Left-Aligned)
n = int(input("enter a size"))
for i in range(1, n+1):
    for j in range(i):
        if j == 0 or j == i-1 or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

Output:
*
* *
*   *
*     *
* * * * *


#Hollow Right-Angled Triangle (Right-Aligned)
n = int(input("enter a size"))
for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end=" ")
    for k in range(i):
        if k == 0 or k == i-1 or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

output:
        *
      * *
    *   *
  *     *
* * * * *

#Hollow Inverted Triangle (Left-Aligned)
n = int(input("enter a size"))
for i in range(n, 0, -1):
    for j in range(i):
        if j == 0 or j == i-1 or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

Output:
* * * * *
*     *
*   *
* *
*

#Hollow Inverted Triangle (Right-Aligned)
n = int(input("enter a size"))
for i in range(n, 0, -1):
    for j in range(n-i):
        print(" ", end=" ")
    for k in range(i):
        if k == 0 or k == i-1 or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

Output:
* * * * *
  *     *
    *   *
      * *
        *

#Hollow Pyramid Pattern
n = int(input("enter a size"))
for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end=" ")
    for k in range(2*i-1):
        if k == 0 or k == 2*i-2 or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

Output:
      *
    *   *
  *       *
* * * * * * *

#Hollow Diamond Pattern
n = int(input("enter a size"))
# Upper half of the hollow diamond
for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end=" ")
    for k in range(2*i-1):
        if k == 0 or k == 2*i-2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
# Lower half of the hollow diamond
for i in range(n-1, 0, -1):
    for j in range(n-i):
        print(" ", end=" ")
    for k in range(2*i-1):
        if k == 0 or k == 2*i-2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

Output:
    *
  *   *
*       *
  *   *
    *

#Hollow Butterfly Pattern
n = int(input("enter a size"))
# Upper half of the hollow butterfly
for i in range(1, n+1): 
    for j in range(i):
        if j == 0 or j == i-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    for k in range(2*(n-i)):
        print(" ", end=" ")
    for l in range(i):
        if l == 0 or l == i-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

Output:
*       *
* *   * *
*   *   *
*       *
*   *   *
* *   * *
*       *

#Hollow Hourglass Pattern
n = int(input("enter a size"))
# Upper half of the hollow hourglass
for i in range(n, 0, -1):
    for j in range(n-i):
        print(" ", end=" ")
    for k in range(2*i-1):
        if k == 0 or k == 2*i-2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
# Lower half of the hollow hourglass
for i in range(2, n+1):
    for j in range(n-i):
        print(" ", end=" ")
    for k in range(2*i-1):
        if k == 0 or k == 2*i-2:
            print("*", end=" ")
        else:
            print(" ", end=" ") 
    print()

Output:
* * * * *
*       *
  *   *
    *
  *   *
*       *
* * * * *

#Increasing Number Triangle
n = int(input("enter a size"))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
Output:
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

#Print numbers from 1 to n in triangle form.
n = int(input("enter a size"))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

Output:
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

#Repeating Row Number Triangle
n = int(input("enter a size"))
for i in range(1, n+1):
    for j in range(i):
        print(i, end=" ")
    print()

Output:
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
#Continuous Number Triangle
n = int(input("enter a size"))
num = 1
for i in range(1, n+1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

Output:
1
2 3
4 5 6
7 8 9 10

#Reverse Row Number Triangle
n = int(input("enter a size"))
for i in range(1, n+1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

Output:
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1

#Inverted Number Triangle
n = int(input("enter a size"))
for i in range(n, 0, -1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

Output:
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1

#Right-Aligned Number Triangle
n = int(input("enter a size"))
for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end=" ")
    for k in range(1, i+1):
        print(k, end=" ")
    print()
Output:
        1
      1 2
    1 2 3
  1 2 3 4
1 2 3 4 5


#Pyramid Number Pattern
n = int(input("enter a size"))
for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end=" ")
    for k in range(1, 2*i):
        print(k, end=" ")
    print()
Output:
      1
    1 2 1
  1 2 3 2 1
1 2 3 4 3 2 1


#Even Number Triangle
n = int(input("enter a size"))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(2*j, end=" ")
    print()
Output:
2
2 4
2 4 6
2 4 6 8
2 4 6 8 10

#Odd Number Triangle
n = int(input("enter a size"))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(2*j-1, end=" ")
    print()
Output:
1
1 3
1 3 5
1 3 5 7
1 3 5 7 9

#Pascal’s Triangle
n = int(input("enter a size"))
for i in range(n):
    num = 1
    for j in range(i+1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)
    print()

Output:
1   
1 1
1 2 1
1 3 3 1
1 4 6 4 1













