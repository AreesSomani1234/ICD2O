#1
# list = ["lebron","monkey","chicken","longwordsssss","a"]
# count = 0
# for word in list:
#     count += len(word)
#     average = count/len(list)

# print(average)

#3
# str = ""
# for word in list:
#     str += word

# print(str)


#5
# for el in range(len(list)-1):
#     if el % 2 == 0:
#         list[el] = list[el].upper()
# print(list)

list = ["apple", "kiwi", "banana","strawberry","blueberry"]
new = []
for word in range(len(list)-1,-1,-1):
    new.append(list[word])
print(new)