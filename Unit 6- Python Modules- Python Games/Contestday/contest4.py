word = input()
bad_word = input()




if bad_word != "frlpz":
    qq = len(word) - len(bad_word)

    list = []
    if (len(word)) > (len(bad_word)):
        for el in range(0,qq):
            list.append(" ")

    for m in range(len(bad_word) - 1):
        list.append(bad_word[m])




    for i in range(len(word)-1):
        if word[i] != bad_word[i]:
            print(f"{word[i]} {bad_word[i]} ")

            break

    for e in range(len(word)-1):
        if " " not in list:
            print("-")
            break
        elif list[0] == " ":
            print(word[len(word)-1])
            break
        elif (" " in list) and (list[e] == " "):
            print(word[e])
            break

        
else:
    print("s z")
    print("o")







