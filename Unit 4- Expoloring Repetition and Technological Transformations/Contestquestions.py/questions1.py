# l1=input("").split()
# l2=input("").split()
# l3=input("").split()
# l4=input("").split()
# sum =int(l1[0]) + int(l1[1]) + int(l1[2]) + int(l1[3])

# if (int(l2[0]) + int(l2[1]) + int(l2[2]) + int(l2[3]) == sum) and (int(l3[0]) + int(l3[1]) + int(l3[2]) + int(l3[3]) == sum) and (int(l4[0] + l4[1] + l4[2] + l4[3] == sum):
#     print("magic")

# else:
#     print("not magic")



l1=input("").split()
l2=input("").split()
l3=input("").split()
l4=input("").split()
sum1 = 0
for i in range(4):
    sum1 = sum1 + int(l1[i])
print(sum1)

sum2 = 0
for i in range(4):
    sum2 = sum2 + int(l2[i])
print(sum2)

sum3 = 0
for i in range(4):
    sum3 = sum3 + int(l3[i])
print(sum3)

sum4 = 0
for i in range(4):
    sum4 = sum4 + int(l4[i])
print(sum4)


if sum1 == sum2 == sum3 == sum4:
    print("magic")

else:
    print("not magic")

