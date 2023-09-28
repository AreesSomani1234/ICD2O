#distance in km, fuel efficiency in km per liter, 
#current price of fuel per liter, number of passengers in vehicle

a=float(input("Enter the distnace of your trip in km: "))
b=float(input("Enter the fuel efficiency for your car in km/liter: "))
c=float(input("What is the current price for fuel/liter: "))
d=int(input("How many people are in the vehicle: "))
#The total amount of fuel needed
#The total cost of fuel for the trip
#The cost of fuel per passenger 
fuel_need=a/b
fuel_cost=c*a
fuel_pp=(c*a)/d
print()
print(f"The total amount of fuell needed: {fuel_need}")
print(f"The total cost for fuel is: {fuel_cost}")
print(f"The total cost per person is: {fuel_pp}")
