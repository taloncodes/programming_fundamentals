#   basic calculator - demonstrates basic input/output, variables, and control structures


#   definitions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        print("Error: Division by zero")

# take input

num1 = float(input("please enter the first number of your calculation: "))

operand = str(input("what kind of calculation would you like to perform? ( +, -, * or /"))

num2 = float(input("please enter the second number for you calculation"))

#   calculate

if operand == '+':
    ans = add(num1, num2)
elif operand == '-':
    ans = subtract(num1, num2)
elif operand == '*':
    ans = multiply(num1, num2)
elif operand == '/':
    ans = divide(num1, num2)

#   output

print(f"{num1} {operand} {num2} = {ans} ")
