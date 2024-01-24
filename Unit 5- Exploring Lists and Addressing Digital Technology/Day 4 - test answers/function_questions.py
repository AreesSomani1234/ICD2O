#1
str = "Joshuaa"
def count_vowels(str):
    str.lower()
    count = 0
    vowels = ["a","e","i","o","u","y"]
    for i in range(0,len(str)):
        if str[i] in vowels:
            count += 1
    return count

print(count_vowels(str))

#2
def reverse_string(str):
    backwards = ""
    for i in range(len(str)-1, -1, -1):
        backwards += str[i]
    return backwards

print(reverse_string(str))

#3
def remove_vowels(str):
    nstr = ""
    vowels = ["a","e","i","o","u","y"]
    for i in range(0,len(str)-1):
        if str[i] not in vowels:
            nstr += str[i]
    return nstr

print(remove_vowels(str))





