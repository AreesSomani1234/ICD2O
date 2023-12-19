import random

#2
def amount_of_customers(weather):
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
def get_weather_condition():
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
     humidities = ['dry', 'wet']
     humidity_choice = random.choice(humidities)
     if condition == "sunny" and humidity_choice == 'dry':
          customer_count +=  random.randint(5, 8)
     elif condition == "sunny" and humidity_choice == 'wet':
          customer_count += -2
     elif condition == "cloudy"and humidity_choice == 'dry':
          customer_count += random.randint(2, 4)
     else:
          customer_count += 0
     
     return humidity_choice, customer_count




def customer_input(wallet):
     signs = int(input("Enter the amount of advertising signs you want (0.15 / sign): "))
     price_per_glass = int(input("Enter the price per glass: "))
     sign_price = signs*0.15 
     while sign_price > wallet:
          signs = int(input("Enter the amount of advertising signs you want: "))
          sign_price = signs*0.15 
     
     return signs, price_per_glass, wallet


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




def advertising_signs(customer_count, condition, humidity_choice, signs,):
     
     if (condition == "sunny" and humidity_choice == 'dry') and 1 <= signs <= 10:
          customer_count += random.randint(0, 5)

     elif (condition == "sunny" and humidity_choice == 'dry') and 11 <= signs <= 15:
          customer_count += random.randint(1, 8)

     elif (condition == "rainy") and 1 <= signs <= 10:
          customer_count += random.randint(0, 2)

     elif (condition == "rainy") and 11 <= signs <= 15:
          customer_count += random.randint(0, 3)
     
     elif (condition == "sunny" and humidity_choice == 'wet') and 1 <= signs <= 10:
          customer_count += random.randint(1, 4)

     elif (condition == "sunny" and humidity_choice == 'wet') and 10 <= signs <= 15:
          customer_count += random.randint(2, 6)

     elif (condition == "cloudy" and humidity_choice == 'dry') and 1 <= signs <= 10:
          customer_count += random.randint(1, 4)

     elif (condition == "cloudy" and humidity_choice == 'dry') and 10 <= signs <= 15:
          customer_count += random.randint(2, 4)

     elif (condition == "cloudy" and humidity_choice == 'wet') and 1 <= signs <= 10:
          customer_count += random.randint(0, 4)

     else:          #cloudy, wet and ad signs 10 - 15
          customer_count += random.randint(0, 5)
     
     return customer_count

def update_customers_by_price(num_customers, price, condition, humidity):
     if (condition == "sunny" and humidity == 'dry'):
          if price > 0.5:
               num_customers -= 5
          else:
               num_customers + 1
     elif (condition == "sunny" and humidity == 'wet'):
          if price > 0.3:
               num_customers -= 5
          else:
               num_customers + 0
     elif (condition == "rainy" ):
          if price > 0.24:
               num_customers -= 5
          else:
               num_customers + 1
     elif (condition == "cloudy" and humidity == 'dry'):
          if price > 0.4:
               num_customers -= 5
          else:
               num_customers + 1
     else: #cloudy, wet
          if price > 0.26:
               num_customers -= 5
          else:
               num_customers + 1
     return num_customers

def display_balance_sheet(day, num_customers, price, num_signs, old_wallet, wallet):
     print(f"Today's day is {day}. You had {num_customers} customers. Your price per glass was {price}.") 
     print(f"You had {num_signs} total signs. Your wallet at the beginning of the day was {old_wallet}. You now have {wallet}$.")

def get_play_again():
     UI = input("Type in 'y' if you would like to play again or 'n' if you'd like to stop playing: ")
     while UI not in ('y', 'n'):
          print("Invalid Answer!")
          UI = input("Type in 'y' if you would like to play again or 'n' if you'd like to stop playing: ")
     if UI == "y":
          return True
     elif UI == "n":
          return False



def sim_day(wallet, day):
     old_wallet = wallet
     weather = get_weather_condition()
     num_customers = amount_of_customers(weather)
     humidity1, num_customers = humidity(weather, num_customers)
     print(f"Today's weather forecast is {weather}. The humidity is {humidity1}.")
     num_signs, price, wallet = customer_input(wallet)
     num_customers = advertising_signs(num_customers, weather, humidity1, num_signs)
     num_customers = update_customers_by_price(num_customers, price, weather, humidity1)
     wallet += num_customers * price
     display_balance_sheet(day, num_customers, price, num_signs, old_wallet, wallet)
     if wallet > 0:
          play_again = get_play_again()
          return wallet, play_again
     else:
          return 0, False


wallet = 2.00
day = 1
wallet, play_again = sim_day(wallet, day)
while(play_again):
     day += 1
     wallet, play_again = sim_day(wallet, day)


