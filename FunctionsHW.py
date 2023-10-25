import math
#HW1
def Greet_person(First_Name, Last_Name):
    name = (f"Hello {First_Name} {Last_Name}")
    return name 


print(f"{Greet_person('Arees', 'Smith')}")

#HW2
def calculate_bmi(weight, height):
    BMI = weight/(height*height)
    return BMI

weight=float(input("Enter your weight in kg: "))
height=float(input("Enter your height in M: "))

print(f"Your BMI is {calculate_bmi(weight, height):.2f}")

#HW3
def format_sales(name, quantity, price):
    Total_price=price*quantity
    return (f"You purchased {quantity} {name} for a total price of ${Total_price:.2f}")

name='wand'
quantity=74
price=78.99
print(f"{format_sales(name, quantity, price)}")