#HW1
def multiply(number1,number2):
    print(f"{number1*number2}")

multiply(3,4)

#HW2
def calculate_cylinder_volume(radius,height):
    print(f"{(3.14159*radius**2)*height:.2f}")

r=float(input("Enter the radius: "))
h=float(input("Enter the height: "))

calculate_cylinder_volume(r,h)

#HW3
def print_triangle():
    print(f"l")
    print(f"lll")
    print(f"lllll")
    print(f"lllllll")
print_triangle()

#HW4
def say_hello(name):
    print(f"Hello {name}")

name=input("Enter your name: ")
say_hello(name)

#HW5
import math
def calculate_circle_area(radius):
    print(f"{math.pi*(radius**2):.2f}")

radius=float(input("Enter the circles radius: "))
calculate_circle_area(radius)

#HW6
def print_square(character,size):
    print(f"{character*size}")
    print(f"{character*size}")
    print(f"{character*size}")
    print(f"{character*size}")

character=("*")
size=4
print_square(character,size)

#HW7
def create_power(number, power):
    print(f"{number**power:.2f}")

create_power(8,9)

#HW8
def calculate_area_triangle(base,height):
    print(f"The area of the triangle is {base*height/2:.2f}")

calculate_area_triangle(7.886,7.345)