#Create a list
list = [6,3,3,5,3,1,-9,-87,35,1,45,3]

#iterate and print the list
# print(list)
# for element in list: #element is the next element in the list.
#     print(element)
#get the sum of all the numbers in the list
# list = [1,2,3,4,5]
# total = 0
# for el in list:
#     total = total + el
# print(total)

# print(sum(list)) #sum() returns the sum of all elements in the list

#print only positive ints in the list
# for el in list:
#     if el > 0 and el % 2 == 0:
#         print(el)


# #Get the largest and smallest number in the list
# smallest = list[0]   #assume the first element is the smallest
# for el in list:   #iterate through the list
#     if el < smallest:  #check if this element is the new smallest
#         smallest = el #if it is make it the smallest
# print(smallest)


# print(min(list))
# print(max(list))

#in a list of strings, get the string that would be considered the largest in terms of alphabetical order
name_list = ["dev", "riya", "joshua", "arees", "JT", "Joshuamoon", "Riya"]
# # biggest_name = name_list[0]   
# # for el in name_list:   
# #     if el > biggest_name: 
# #         biggest_name = el 
# # print(biggest_name)

# print(max(name_list))
# print(min(name_list))

#longest length name (2 ways)
longest = name_list[0]

for el in name_list:
    if len(longest) < len(el):
        longest = el
print(longest)


print(max(name_list,key=len))   # using the key attribute we can change how to use the max