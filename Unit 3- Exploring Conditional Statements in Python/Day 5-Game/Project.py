import random

def choose_superhero():
    print("Choose your superhero: ")
    print("1. Tyreek The Turtle")
    print("2. Jaguar John")
    print("3. Math Man")
    superhero = input("Enter number of your chosen superhero: ")

    while superhero not in ['1','2','3']:
        print("Invalid number")
        print("Choose your superhero: ")
        print("1. Tyreek The Turtle")
        print("2. Jaguar John")
        print("3. Math Man")
        superhero = input("Enter number of your chosen hero: ")
    
    if superhero == '1':
        return 'Tyreek The Turtle'
    elif superhero == '2':
        return 'Jaguar John'
    else:
        return 'Math Man'
    
def game_intro(player_superhero):
    print()
    print(f"Greetings, you are the legendary {player_superhero}!")
    print("The Evil Villan Bernard has 5 hostages on the top of the CN tower ")
    print("It is your job to stop him or he will eat the hostages. Good Luck!")
    print("You win by killing Bernard and living. you start at 30-50 health and bernard starts at 50-75 health")
    print("Note: Every eaten hostage will make you lose health in the end")


def make_decision():
    print("You now enter the CN tower you have 3 options")
    print("1. Take the Stairs")
    print("2. Take the elevator")
    print("3. Give up and go home.")
    decision = input("Enter the number for your decision. ")
    
    while decision not in ['1', '2', '3']:
        print("Invalid number")
        decision = input("Enter the number for your decision: ")

    return decision

def superhero_mission(action, player_superhero):   
    bernard_hp = random.randint(50,75)
    your_health = random.randint(30, 50)
    hostage_count = 5
    if action == '1':
        print("Ok choice ")
        print("Now you confront the villian at the top of the CN tower")
        print("but since you took so long Bernard ate 1 of the 5 hostages. ")
        print("Also you are very tired so you will do less damage")
        bernard_hp = bernard_hp - random.randint(25, 75)
        your_health = your_health - random.randint(5,40)
        hostage_count = hostage_count - 1

    if action == '2':
        print ("Great Choice")
        print("Now you confront Bernard prepare for an epic battle ")
        bernard_hp = bernard_hp - random.randint(70, 100)
        your_health = your_health - random.randint(1,25)

    if action == '3':
        print("All the hostages have been eaten because you didn't show up.")
        print("But Bernard found you at home and is ready to fight.")
        print("You were caught off guard so Bernard has the advantage.")
        print("Since you were caught off guard wou will do less damage and Bernard will do more damage.")
        bernard_hp = bernard_hp - random.randint(1, 70)
        your_health = your_health - random.randint(30,700)
        hostage_count = 0
    
    return your_health, bernard_hp, hostage_count

def bonus_points(your_health, hostage_count):
    if hostage_count == 5:
        your_health = your_health + 10

    elif 1 <= hostage_count <= 4:
        your_health = your_health - 5

    else:
        your_health = your_health - 10

def health_management(your_health, bernard_hp):
    if your_health <= 0 and bernard_hp > 0:
        print(f'Your final health is {your_health} and Bernards final health is {bernard_hp}. You lose, because Bernard is still alive and your dead.')
    
    elif your_health <= 0 and bernard_hp <= 0:
        print(f'Your final health is {your_health} and Bernards final health is {bernard_hp}. You killed bernard but still lose because you died.')
    
    elif your_health >= 0 and bernard_hp >= 0:
        print(f'Your final health is {your_health} and Bernards final health is {bernard_hp}. You live but Bernard lives to so You lose')
    else:
        print(f'Your final health is {your_health} and Bernards final health is {bernard_hp}. You Win because you killed Bernard!')
         

hero = choose_superhero()
print()
game_intro(hero)
print()
decision = make_decision()
print()
your_health, bernard_hp, hostage_count = superhero_mission(decision, hero)
print()
bonus_points(your_health, hostage_count)
health_management(your_health, bernard_hp)
