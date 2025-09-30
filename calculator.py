#calculator
operator = input("Choose operator (+, -, /, *): ")
number1 = float(input("First number: "))
number2 = float(input("Second number: "))
if operator == '+':
    result = number1 + number2
    print(result)
elif operator == '-':
    result = number1 - number2
    print(result)
elif operator == '/':
    if number2 != 0:
        result = number1 / number2
        print(result)
    else:
        print("Error! Can't divide by Zero.")
elif operator == '*':
    print(number1 * number2)        
else:
    print("Invalid character!")    
        