import random

#2
def amount_of_customers(condition):
    weather = ["sunny", "cloudy", "rainy"]
    customer_count = 0
    if weather == "sunny":
          customer_count += random.randint(30, 50)
          return customer_count
    elif weather == "cloudy":
          customer_count +=  random.randint(20, 40)
          return customer_count
    else:   #Rainy
          customer_count += random.randint(10, 20)
          return customer_count

#1
def weather_conditions():
     probability = random.randint(1, 5)
     if probability == 1 or probability == 2:
          return "rainy"
     elif probability == 3:
          return "cloudy"
     else:
          return "sunny"
     
#dont forget to make condition = weather_conditions()

#3
def humidity(condition, customer_count):
     humidity['dry', 'wet']
     humidity_choice = random.choice(humidity)
     if condition == "sunny" and humidity_choice == 'dry':
          customer_count +=  random.randint(5, 8)
     elif condition == "sunny" and humidity_choice == 'wet':
          customer_count += -2
     elif condition == "cloudy"and humidity_choice == 'dry':
          customer_count += random.randint(2, 4)
     else:
          customer_count += 0
     
     return humidity_choice


#4
def customer_spending(condition, humidity_choice, price):
     customer_spending = 0
     if condition == "sunny" and humidity_choice == 'dry':
          customer_spending = random.randint(0.11, 0.30)
     
     elif condition == "sunny" and humidity_choice == 'wet':
          customer_spending = random.randint(0.05, 0.15)

     elif condition == "cloudy" and humidity_choice == 'dry':
          customer_spending = random.randint(0.03, 0.10)

     elif condition == "cloudy" and humidity_choice == 'wet':
          customer_spending = random.randint(0.02, 0.08)

     else: #rainy
          customer_spending = random.randint(0, 0.03)

     return customer_spending




def advertising_signs(customer_count, condition, humidity_choice, advertising_signs, total_money):
     ad_price = advertising_signs*0.15 
     #while advertising_signs > 15: (ask for help)
     
     if (condition == "sunny" and humidity_choice == 'dry') and 1 <= advertising_signs <= 10:
          customer_count += random.randint(0, 5)

     elif (condition == "sunny" and humidity_choice == 'dry') and 11 <= advertising_signs <= 15:
          customer_count += random.randint(1, 8)

     elif (condition == "rainy") and 1 <= advertising_signs <= 10:
          customer_count += random.randint(0, 2)

     elif (condition == "rainy") and 11 <= advertising_signs <= 15:
          customer_count += random.randint(0, 3)
     
     elif (condition == "sunny" and humidity_choice == 'wet') and 1 <= advertising_signs <= 10:
          customer_count += random.randint(1, 4)

     elif (condition == "sunny" and humidity_choice == 'wet') and 10 <= advertising_signs <= 15:
          customer_count += random.randint(2, 6)

     elif (condition == "cloudy" and humidity_choice == 'dry') and 1 <= advertising_signs <= 10:
          customer_count += random.randint(1, 4)

     elif (condition == "cloudy" and humidity_choice == 'dry') and 10 <= advertising_signs <= 15:
          customer_count += random.randint(2, 4)

     elif (condition == "cloudy" and humidity_choice == 'wet') and 1 <= advertising_signs <= 10:
          customer_count += random.randint(0, 4)

     else:          #cloudy, wet and ad signs 10 - 15
          customer_count += random.randint(0, 5)