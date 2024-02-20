shu = 0
n = int(input())

for i in range(0,n):
    l = input()
    if l == "Poblano":
        shu += 1500
    if l == "Mirasol":
        shu += 6000
    if l == "Serrano":
        shu += 15000
    if l == "Cayenne":
        shu += 40000
    if l == "Thai":
        shu += 75000
    if l == "Habanero":
        shu += 125000


print(shu)
