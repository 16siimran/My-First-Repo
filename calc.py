import math

print("Choose a shape to find the area:")
print("1. Circle")
print("2. Square")
print("3. Rectangle")
print("4. Triangle")

choice = input("Enter choice (1/2/3/4): ")

if choice == '1':
    radius = float(input("Enter radius of the circle: "))
    area = math.pi * radius * radius
    print("Area of Circle =", area)

elif choice == '2':
    side = float(input("Enter side length of the square: "))
    area = side * side
    print("Area of Square =", area)

elif choice == '3':
    length = float(input("Enter length of the rectangle: "))
    width = float(input("Enter width of the rectangle: "))
    area = length * width
    print("Area of Rectangle =", area)

elif choice == '4':
    base = float(input("Enter base of the triangle: "))
    height = float(input("Enter height of the triangle: "))
    area = 0.5 * base * height
    print("Area of Triangle =", area)

else:
    print("Invalid choice!")
