name=(input("Enter your name: "))
print()

#Game 1
print("Game #1: ")
opponent1=input("Opponent's Name: ")
your_points1=int(input("Your points: "))
opponents_points1=int(input("Opponent's points: "))
print()

#Game 2
print("Game #2: ")
opponent2=input("Opponent's Name: ")
your_points2=int(input("Your points: "))
opponents_points2=int(input("Opponent's points: "))
print()

#Game 3
print("Game #3: ")
opponent3=input("Opponent's Name: ")
your_points3=int(input("Your points: "))
opponents_points3=int(input("Opponent's points: "))
print()

#Game 4
print("Game #4: ")
opponent4=input("Opponent's Name: ")
your_points4=int(input("Your points: "))
opponents_points4=int(input("Opponent's points: "))
print()

#Game 5
print("Game #5: ")
opponent5=input("Opponent's Name: ")
your_points5=int(input("Your points: "))
opponents_points5=int(input("Opponent's points: "))
print()

print("Dots and Boxes score tracker")
print(f"Player Name: {name}")
print()
print(f"{'Opponent':>20} {'Your Points':>20} {'Opponent Points':>20} {'Box %':>20}")
print(f"{'================================================================================================='}")
print(f"{opponent1:>20} {your_points1:>20} {opponents_points1:>20} {your_points1/36:>20.2%}")
print(f"{opponent2:>20} {your_points2:>20} {opponents_points2:>20} {your_points2/36:>20.2%}")
print(f"{opponent3:>20} {your_points3:>20} {opponents_points3:>20} {your_points3/36:>20.2%}")
print(f"{opponent4:>20} {your_points4:>20} {opponents_points4:>20} {your_points4/36:>20.2%}")
print(f"{opponent5:>20} {your_points5:>20} {opponents_points5:>20} {your_points5/36:>20.2%}")
print(f"{'================================================================================================='}")
print()
total_points = your_points1 + your_points2 + your_points3 + your_points4 + your_points5
opponent_points = opponents_points1 + opponents_points2 + opponents_points3 + opponents_points4 + opponents_points5
percentage_of_points = total_points/(36*5)
print("Summary:")

print(f"Total points: {total_points}")
print(f"Total opponent's points: {opponent_points}")
print(f"Percentage of points recieved:{percentage_of_points:.2%} ")