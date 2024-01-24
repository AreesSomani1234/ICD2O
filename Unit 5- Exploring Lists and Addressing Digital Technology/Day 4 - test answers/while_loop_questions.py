#1
n = 0
while n <= 0:
    n = int(input("Enter a positive number: "))

#2
    import random
    num = random.randint(1,10)
    geuss = int(input("Enter a number from 1-10: "))
    while geuss != num:
        geuss = int(input("Enter a number from 1-10: "))
        if geuss < num:
            print("to low")
        elif geuss > num:
            print("to High")
    print("Correct")
    
#3
n = 2
sum = 0
while sum <= 10:
    sum += n
    n += 2
print(sum)