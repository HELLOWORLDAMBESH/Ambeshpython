import math

# Input coefficients
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Calculate the discriminant
d = b**2 - 4*a*c

# Check for roots based on the discriminant
if d > 0:
    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)
    print(f"Roots are real and different:\nRoot 1 = {root1}\nRoot 2 = {root2}")
elif d == 0:
    root = -b / (2*a)
    print(f"Roots are real and equal:\nRoot = {root}")
else:
    # Complex roots
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(-d) / (2*a)
    print(f"Roots are complex:\nRoot 1 = {real_part} + {imaginary_part}i\nRoot 2 = {real_part} - {imaginary_part}i")
