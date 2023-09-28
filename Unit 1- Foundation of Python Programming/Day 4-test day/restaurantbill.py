#Drink,appetizer, entree, desert
a=float(input("What was the cost of your drink: "))
b=float(input("What was the cost of your appetizer: "))
c=float(input("What was the cost of your entree: "))
d=float(input("What was the cost of your dessert: "))
e=float(input("Enter the tip rate: "))
s=a+b+c+d
g=e/100
print("Bill summary")
print(f"Subtotal: {s}")
print(f"Total tip: {(s*g)}")
print(f"The total cost: {(s*g)+s}")


