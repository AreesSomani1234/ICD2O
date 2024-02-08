def user_input():
    num1 = float(input("Enter a number: "))
    sign = input("Enter what function you want to use (+,-,/,*,**): ")
   
    while sign not in ["+","-","/","*","**"]:
        print("Incorrect input! Try again!")
        sign = input("Enter what function you want to use (+,-,/,*,**): ")
    
    num2 = float(input("Enter a number: "))
    return num1, sign, num2


def calculation(num1,num2,sign):
    answer = 0
    if sign == "+":
        answer = num1 + num2
    elif sign == "-":
        answer = num1 - num2
    elif sign == "/":
        answer = num1 / num2
    elif sign == "*":
        answer = num1 * num2
    elif sign == "**":
        answer = num1 ** num2

    return answer

num1, sign, num2 = user_input()

result = calculation(num1, num2, sign)

print(f"Result: {result:.3f}")