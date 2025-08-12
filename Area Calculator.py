import math
print("""
==================
Area Calculator 📐
==================

1) Triangle
2) Rectangle
3) Square
4) Circle
5) Quit """)

x = input("which shape: ")
# area of Triangle 
if x == "1": 
    h = int(input("what is the height: "))
    b = int(input("what is the base: "))
    area=(h * b)/2 
    print(f'The area is {area}')
# area of Rectangle
elif x == "2":
    l = int(input("what is the length: "))
    w = int(input("what is the width: "))
    area = l * w 
    print(f'The area is {area}')
# area of Square
elif x == "3":
    s=int(input("what is the side: "))
    area = s**2
    print(f'The area is {area}')
#area of Circle
elif x == "4":
    r = int(input("what is the radius: "))
    area = math.pi * (r**2)
    print(f'The area is {area}')
# Quit
elif x == "5":
    print("Thank you for using the area calculator")
#incorrect commands enter
else: 
    print("Incorrect commands enter, please run the python code again")