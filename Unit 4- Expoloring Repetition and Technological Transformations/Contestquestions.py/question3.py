str = input().strip()

max_length = 0

for i in range(len(str)):
    for j in range(i, len(str)):
        substring = str[i:j + 1]
        if substring == substring[:-1]:
            max_length = max(max_length, len(substring))

print(max_length)


    
