def input_bug_counts(bug_type):
    count = int(input(f"Enter the count of {bug_type}: "))
    return count

def calculate_percent(total, count):
    percent_of_bug_type = count/total
    return percent_of_bug_type

def input_bug_type_and_count():
    bug_type = input("Enter the type of bug: ")
    count = input_bug_counts(bug_type)
    return bug_type, count

def display_table(bug1, count1, bug2, count2, bug3, count3):
    total = count1+count2+count3
    total_percent = (count1/total) + (count2/total) + (count3/total)
    print(f"{'Bug Type':<10} {'Count':>20} {'Percentage':>15}")
    print("="*50)
    print(f"{bug1:<10} {count1:>20} {calculate_percent(total, count1):>15.2%}")
    print(f"{bug2:<10} {count2:>20} {calculate_percent(total, count2):>15.2%} ")
    print(f"{bug3:<10} {count3:>20} {calculate_percent(total, count3):>15.2%} ")
    print("="*50)
    print(f"{'Total':<10} {total:>20} {total_percent:>15.2%} ")

bug1, count1 = input_bug_type_and_count()
bug2, count2 = input_bug_type_and_count()
bug3, count3 = input_bug_type_and_count()

display_table(bug1, count1, bug2, count2, bug3, count3)




