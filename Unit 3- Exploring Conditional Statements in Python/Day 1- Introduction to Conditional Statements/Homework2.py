def not_string(s):
    if s[0:3] == "not":
        return s
    if s[0:3] != "not":
        return "not" + s
    

print(not_string("hello"))


