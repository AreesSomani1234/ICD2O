#length, width ,height, cost per brick, dimensions of a standard brick
a=float(input("Enter length of one wall in meters: "))
b=float(input("Enter width of one wall in meters: "))
c=float(input("Enter height of one wall in meters: "))
d=float(input("Enter the cost per brick: "))
e=float(input("Enter length of brick in meters: "))
f=float(input("Enter width of brick in meters: "))
g=float(input("Enter height of brick in meters: "))

row1=a/e
height1=c/g
wall1=(row1*height1)*2
wsa=(a*c)*2

row2=b/e
height2=c/g
wall2=(row2*height2)*2
wsa2=(b*c)*2


twsa3=wsa+wsa2
total=wall1+wall2
total_cost=total*d

print()
print("House details:")
print(f"Wall SA: {twsa3}")
print(f"Bricks required {total}")
print(f"Total Cost: {total_cost}$")




