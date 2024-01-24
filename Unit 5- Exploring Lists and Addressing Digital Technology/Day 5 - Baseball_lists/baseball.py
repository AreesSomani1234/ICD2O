# Function to read data from file
def read_baseball_data(file_path):
    names, hits, runs, rbis = [], [], [], []
    try:
        with open(file_path, "r") as file:
            # Skip the header line
            next(file)
            for line in file:
                data = line.strip().split(',')
                names.append(data[0])
                hits.append(int(data[1]))
                runs.append(int(data[2]))
                rbis.append(int(data[3]))
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    return names, hits, runs, rbis

# Function to display all baseball player statistics
def display_all_baseball_stats(names, hits, runs, rbis):
    print(f"{'Names':<25}{'Hits':>6}{'Runs':>6}{'RBIS':>6}")
    for index in range(len(names)):
        print(f"|{names[index]:<25}|{hits[index]:>6}|{runs[index]:>6}|{rbis[index]:>6}|")
    
# Function to calculate and display average baseball statistics
def calculate_and_display_average(hits, runs, rbis):
    total = 0
    for index in range (len(hits)):
        total += index
    averagehits = total/len(hits)
    print(averagehits)

    for i in range (len(runs)):
        total += i
    averageruns = total/len(runs)
    print(averageruns)

    for n in range (len(rbis)):
        total += n
    averagerbis = total/len(rbis)
    print(averagerbis)


# Function to identify the baseball player with the highest stats in a category
def stat_leader(category):
    maxIndex = 0
    for index in range(len(names)):
        if category == "Hits":
            if hits[maxIndex] < hits[index]:
                maxIndex = index
        elif category == "RBIs":
            if rbis[maxIndex] < rbis[index]:
                maxIndex = index
        
    if category == "Hits":
        print()
        print(f"The player with the most hits is{names[maxIndex]} is {hits[maxIndex]}")
    elif category == "RBIs":
        print()
        print(f"The player with the most RBIs {names[maxIndex]} is {rbis[maxIndex]}")
        

# Function to display the top 10 players in a specified category
def display_top_10_in_category(category, hits):
    cpy = hits.copy()

    cpy.sort()
    top10Hits = cpy[0:10]

    print(top10Hits)


# Function to allow users to add a new baseball player with their statistics
def add_new_player(names, hits, runs, rbis):
    new_name = input("Enter the new players name: ")
    new_hits = int(input("Enter the new players hits: "))
    new_runs = int(input("Enter the new players runs: "))
    new_RBIS = int(input("Enter the new players RBIs: "))
    names.append(new_name)
    hits.append(new_hits)
    runs.append(new_runs)
    rbis.append(new_RBIS)

# Main program
if __name__ == "__main__":
    # Specify the file path
    file_path = "baseball_stats.txt"

    # Read baseball data from the file
    names, hits, runs, rbis = read_baseball_data(file_path)

    # Display menu and handle user choices
    while True:
        print("\nMenu:")
        print("1. Display all baseball player statistics")
        print("2. Calculate and display average baseball statistics")
        print("3. Identify player with the most hits")
        print("4. Identify player with the most RBIs")
        print("5. Display top 10 players in a category")
        print("6. Add a new baseball player")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            display_all_baseball_stats(names, hits, runs, rbis)
        elif choice == "2":
            calculate_and_display_average(hits, runs, rbis)
        elif choice == "3":
            stat_leader('Hits')
        elif choice == "4":
            stat_leader('RBIs')
        elif choice == "5":
            category = input("Enter the category to display top 10 players: ")
            display_top_10_in_category(category, hits)
        elif choice == "6":
            add_new_player(names, hits, runs, rbis)
        elif choice == "7":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")