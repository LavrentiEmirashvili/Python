from art import logo
import os

def addition(a,b):
    return  a + b
def substraction(a,b):
    return  a - b
def multiplication(a,b):
    return  a * b
def division(a,b):
    return  a / b

operations = {
    "+": addition,
    "-": substraction,
    "*": multiplication,
    "/": division
}
def calculate():
    os.system("cls")
    print(logo)
    a = int(input("What's the first number?:"))
    for i in operations:
        print(i)


    # for i in operations:
    #     if operationChoice == i:
    #         answer = operations[i](a,b)


    should_continue = True
    while should_continue:
        operationChoice = input("Pick an operation:")
        operation = operations[operationChoice]
        b = int(input("What's the next number?:"))
        answer = operation(a, b)
        print(f"{a} {operationChoice} {b} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.:") == "y":
            a = answer
        else:
            should_continue = False    
            calculate()

calculate()




# ignore

# def operate(num1,operation,num2):
#     if operation == "+":
#         answer = num1 + num2 
#     elif operation == "-":
#         answer = num1 - num2 
#     elif operation == "*":
#         answer = num1 * num2 
#     elif operation == "/":
#         if num2 == 0:
#             print("Error: Division by zero is not allowed.")
#             return num1, "n"  
#         answer = num1 / num2 
#     else:
#         print("Invalid operation.")
#         return num1, "n"
#     print(f"{num1} {operation} {num2} = {answer}")
#     continuecalc = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation:")
#     return answer, continuecalc

# num1 = float(input("What's the first number?:"))
# operation = input("+\n-\n*\n/\nPick an operation:")
# num2 = float(input("What's the second number?:"))

# os.system("cls")

# answer, continuecalc = operate(num1, operation, num2)


# while continuecalc == "y":
#     operation = input("+\n-\n*\n/\nPick an operation: ")
#     num2 = float(input("What's the second number?: "))
#     answer, continuecalc = operate(answer, operation, num2)

# os.system("cls")


# num1 = float(input("What's the first number?: "))
# operation = input("+\n-\n*\n/\nPick an operation: ")
# num2 = float(input("What's the second number?: "))

# operate(num1, operation, num2)