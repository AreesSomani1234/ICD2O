import math
#HW1
def middleThree(word):
    length=len(word)
    middle=length/2
    h = word[int(middle) - 1:int(middle) + 2]
    return h


print(f"{middleThree('Candy')}")

#HW2
def Last_Chars(str_a, str_b):
    first_character_of_a = str_a[0:1]
    last_character_of_b = str_b[len(str_b)-1:len(str_b)]
    return (f"{first_character_of_a}{last_character_of_b}")


print (f"{Last_Chars('Hello', 'bye')}")

#HW3
def last_two(str):
    length = len(str)
    without_last_two = str[0:length-2]
    second_last = str[length-2:length-1]
    last = str[length-1:length]
    return (f"{without_last_two}{last}{second_last}")

print (last_two('chicken'))

#HW4
def extra_front(str):
    d = str[0:2]*3
    return d
print (extra_front('amazing'))