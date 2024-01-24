list = ["python", "program", "is", "hard"]
nlist = []

for i in range(len(list)-1):
    if i % 2 == 0:
        list[i] += list[i].upper()
        nlist += list[i]
    else:
        nlist += list[i]

print(nlist)
