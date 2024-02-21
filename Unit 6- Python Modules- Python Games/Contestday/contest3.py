N = int(input())

list = []

for i in range(0,N):
    P = int(input())
    list.append(P)

x = max(list)
for i in range(0,len(list)+1):
    if x in list:
        list.remove(x)

y = max(list)
for i in range(0,len(list)+1):
    if y in list:
        list.remove(y)

z = max(list)



num = 0
for i in range(0, len(list)):
    if z == list[i]:
        num = num+1

print(f"{z} {num}")