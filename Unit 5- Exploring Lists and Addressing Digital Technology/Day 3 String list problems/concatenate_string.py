list = ["hello", "there", "nolan", "is", "a", "monkey"]
def concantenate_strings(list):
    result = ""
    for word in list:
        result += word
    return result


print(concantenate_strings(list))