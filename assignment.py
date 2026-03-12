#question 1
side1 = 5
side2 = 6
side3 = 7
perimeter = side1 + side2 + side3
print("perimeter of triangle", perimeter)

#question 2
amount = 3700
thousand = amount // 1000
amount = amount % 1000

five_hundred = amount // 500
amount = amount % 500

print("1000's", thousand)
print("500's", five_hundred)
print("remaining", amount)

#question 3
maths = int(input("enter maths marks="))
physics = int(input("enter physics marks="))  
chemistry = int(input("enter chemistry marks="))
Average_marks = (maths + physics + chemistry)//3
if maths| physics| chemistry < 35:
    print("fail")
elif Average_marks >= 75:
    print("Distinction")
elif Average_marks >= 60:
    print("first class")
elif Average_marks >= 50:
    print("you're final result second class")
else:
    print("you're just pass")

