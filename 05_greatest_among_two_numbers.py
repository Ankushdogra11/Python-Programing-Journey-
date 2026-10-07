# Program to take two numbers as input and compare them
# to find the greater number or check if both numbers are equal.
a = int(input("Enter Ist number :- "))
b = int(input("Enter sec number :- "))

if a > b:
    print(f"{a} is Greater than {b}")
elif b > a:
    print(f"{b} is Greater than {a}")
else:
    print("Both numbers are equal ")
