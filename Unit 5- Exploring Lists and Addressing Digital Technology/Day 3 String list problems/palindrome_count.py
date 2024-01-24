list = ["level", "python", "radar", "civic", "list"]
count = 0
for word in list:
    is_palindrome = True
    for i in range(len(word)):
        if word[i] != word[len(word)-i-1]:
            is_palindrome = False
    if is_palindrome:
        count += 1
print(count)



