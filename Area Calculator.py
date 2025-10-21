print("Area Calculator")

print("1) Square")
print("2) Rectangle")
print("3) Triangle")
print("4) Circle")

num = int(input("Please select your number:"))

if num == 1:
    side = int(input("Please Enter Side:"))
    area = side**2
    print("The area of square is : ",area)
elif num == 2:
    length = int(input("please select length:"))
    width = int(input("please select width: "))
    area = length * width
    print("The area of rectangle is : ",area)
elif num == 3:
    length = int(input("please select length:"))
    width = int(input("please select width: "))
    area = 0.5 * (length * width)
    print("The area of triangle is : ",area)
elif num == 4:
    radius = int(input("please enter radius"))
    area = 3.14 * radius**2
    print("The area of circle is : ",area)
else:
    print("Please try again")