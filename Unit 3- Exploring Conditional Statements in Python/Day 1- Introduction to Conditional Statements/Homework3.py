def squirrel_play(temp, is_summer):
   if is_summer == True:
        return 100 >= temp >= 60
   if is_summer == False:
    return 90 >= temp >= 60
        
   

print(squirrel_play(91, False))