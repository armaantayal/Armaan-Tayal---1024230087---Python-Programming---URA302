#PYTHON WORKSHEET 1
#Submitted by ARMAAN TAYAL(1024230087)

#q1
print("Twinkle, twinkle, little star,")
print("\tHow I wonder what you are!")
print("\t\tUp above the world so high,")
print("\t\tLike a diamond in the sky.")
print("Twinkle, twinkle, little star,")
print("\tHow I wonder what you are!")

#q2
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(last_name, first_name)

#q3
import math

radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius**2
print("The area of the circle with radius", radius, "is:", area)

#q4
color_list = ["Red", "Green", "White", "Black"]
print("First color:", color_list[0])
print("Last color:", color_list[-1])

#q5
n = input("Enter an integer (n): ")
n1 = int(n)
n2 = int(n + n)
n3 = int(n + n + n)
result = n1 + n2 + n3
print("The value of n+nn+nnn is:", result)

#q6
data = input("Enter comma-separated numbers: ")
number_list = data.split(',')
number_tuple = tuple(number_list)
print("List:", number_list)
print("Tuple:", number_tuple)

#q7
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (9/5) * celsius + 32
print(celsius, "C is equal to", fahrenheit, "F")

#q8
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))
print("Original numbers: a =", a, ", b =", b)

# Swapping the numbers using a temporary variable
temp = a
a = b
b = temp

# Incrementing the swapped numbers by 1
a = a + 1
b = b + 1

print("Swapped and incremented numbers: a =", a, ", b =", b)

#q9
num = int(input("Enter an integer: "))
if num % 2 == 0:
    print("The number", num, "is even.")
else:
    print("The number", num, "is odd.")

#q10
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("The year", year, "is a leap year.")
else:
    print("The year", year, "is not a leap year.")

#q11
import math

x1 = float(input("Enter x-coordinate of first point: "))
y1 = float(input("Enter y-coordinate of first point: "))
x2 = float(input("Enter x-coordinate of second point: "))
y2 = float(input("Enter y-coordinate of second point: "))

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("The Euclidean distance is:", distance)

#q12
angle1 = float(input("Enter the first angle: "))
angle2 = float(input("Enter the second angle: "))
angle3 = float(input("Enter the third angle: "))

if angle1 + angle2 + angle3 == 180 and angle1 > 0 and angle2 > 0 and angle3 > 0:
    print("These angles can form a triangle.")
else:
    print("These angles cannot form a triangle.")

#q13
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in decimal): "))
time = float(input("Enter the number of years: "))
compounding_frequency = float(input("Enter the number of times interest is compounded per year: "))

amount = principal * (1 + rate / compounding_frequency)**(compounding_frequency * time)
compound_interest = amount - principal

print("The compound interest is:", round(compound_interest, 2))
print("The total amount after compounding is:", round(amount, 2))

#q14
N = int(input("Enter a positive integer: "))

if N > 1:
    is_prime = True
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            is_prime = False
            break
    if is_prime:
        print("The number", N, "is prime.")
    else:
        print("The number", N, "is not prime.")
else:
    print("The number", N, "is not prime.")

#q15
N = int(input("Enter a positive integer (N): "))
sum_of_squares = 0
for i in range(1, N + 1):
    sum_of_squares += i**2

print("The sum of squares up to", N, "is:", sum_of_squares)
