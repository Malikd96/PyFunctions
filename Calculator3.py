#Task 3: Ensure your code can handle division by zero and other potential errors. So if you divide by 0, 
# there is error handling set up to prevent an error from showing in the console.

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multi(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error! Division by 0"
    return a / b

def calculator():
    print("Basic Calculator")
    print("1: add")
    print("2: sub")
    print("3: multi")
    print("4: div")

    choice = input("Select operation (1/2/3/4): ")
    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

    if choice == '1':
        print(f"The result is: {add(num1, num2)}")
    elif choice == '2':
        print(f"The result is: {sub(num1, num2)}")
    elif choice == '3':
        print(f"The result is: {multi(num1, num2)}")
    elif choice == '4':
        print(f"The result is: {div(num1, num2)}")
    else:
        print("Input is invalid!")
calculator()