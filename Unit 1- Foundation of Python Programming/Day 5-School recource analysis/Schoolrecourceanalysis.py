#Water Fountains
water_fountain=int(input("How many water fountains are there: "))
fountain_location=input("Enter the locations of the water fountains (seperated by comas): ")
fountain_condition=input("What conditions are the fountains in: ")
#Restrooms
restrooms=int(input("How many restrooms are there: "))
restroom_location=input("Enter the locations of the restrooms (seperated by comas): ")
restroom_condition=input("What conditions are the restrooms in: ")
#Cafeteria
seating_capacity=int(input("Enter the seating capacity of the cafeteria: "))
daily_attendence=int(input("Enter the daily average attendence: "))
cafe_condition=input("What are the conditions of the cafeteria: ")
#classrooms
classrooms=int(input("How many classrooms are there: "))

print()
print("Data Collected")
print()
#1
print("1. Water Fountains")
print(f"Number of water fountains: {water_fountain}")
print(f"Locations: {fountain_location}")
print(f"Fountain condition: {fountain_condition}")
#2
print()
print("2. Restrooms")
print(f"Number of restrooms: {restrooms}")
print(f"Locations: {restroom_location}")
print(f"Restroom Condition: {restroom_condition}")
#3
print()
print("3. Cafeteria")
print(f"Seating capacity: {seating_capacity}")
print(f"Average daily attendance: {daily_attendence}")
print(f"Cafeteria Condition: {cafe_condition}")
print()
#4
print("4. Classrooms")
print(f"Total number of classrooms: {classrooms}")
print(f"Number of water fountains per classroom: {water_fountain/classrooms}")
print(f"Number of restrooms per Classroom: {restrooms/classrooms}")
