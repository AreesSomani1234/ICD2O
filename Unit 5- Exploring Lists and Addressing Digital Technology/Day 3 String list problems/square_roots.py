import math
list = [1,2,4,8,16,25]
nlist = []

for num in list:
    num = math.sqrt(num)
    nlist.append(num)

print(f"{nlist}")