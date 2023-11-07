def theEnd(str, bool):
    if bool == True:
        return str[0:1]
    
    if bool == False:
        return str[len(str)-1:len(str)]
    
    if len(str) == 0:
        return "Empty"
    

print(theEnd("Hello", True))
print(theEnd("Hello", False))
print(theEnd("oh", True))
print(theEnd("", True))