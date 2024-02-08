list = ["apple", "kiwi", "banana","strawberry","blueberry"]
count = 0
for word in list:
    count += len(word)
    average = count / len(list)
print(average)