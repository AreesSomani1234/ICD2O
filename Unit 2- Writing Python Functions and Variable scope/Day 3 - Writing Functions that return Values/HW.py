#HW1
import math

def area_of_circle(r):
    area=(math.pi*(r**2))
    return area

are=area_of_circle(8)
print(f"The are of the circle with a radius of 8 is {are:.2f}.")


#HW2
def area_of_rectangle(length, width):
    area=length*width
    return area
print(f"the area of a rectangle is {area_of_rectangle(7,9)}")

#HW3
def Volume_of_cylinder(radius, height):
    volume = math.pi*(radius**2)*height
    return volume

r=float(input("Enter radius: "))
h=float(input("Enter the height: "))

print(f" The volume of a cylinder with a radius of {r} and a height of {h} has volume of {Volume_of_cylinder(r,h):.2f}")


