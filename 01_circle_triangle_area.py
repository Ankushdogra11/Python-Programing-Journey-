# Program to take the required dimensions as input from the user
# and calculate and display the area of a circle and a triangle.

r = int(input("Enter radius :- "))
b = int(input("Enter Base :- "))
h = int(input("Enter Height :- "))
A = 3.14 * r**2
a = 1/2 * h * b

print(f"Area of circle = {A}")
print(f"Area of Triangle = {a}")
