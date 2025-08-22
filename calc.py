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
