import datetime

current_time = datetime.datetime.now()

def setting_time_intervals():
    add_time_intervals = True
    time_intervals = []
    

    while add_time_intervals:
        new_time_interval = input("Enter time interval (HH:MM): ")
        time_intervals.append(new_time_interval)

        continue_loop = input("Would you like to add anymore time intervals (y/n): ")

        if continue_loop == "n":
            add_time_intervals = False
    
    return time_intervals

dispence_drugs = input("Would you like to begin the cycle (y/n): ")
if dispence_drugs == "y":
    dispencing = True
else:
    dispencing = False

times = setting_time_intervals()

while dispencing:
    for el in range(len(times)-1):
        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime("HH:MM")
        if current_time == times[el]:
            print("pill dispenced")




