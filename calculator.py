def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {"+":add, "-":subtract, "*":multiply, "/":divide}   

def calculator():
    n1 = float(input("Enter the first number: "))

    while True:
        n2 = float(input("Enter the next number: "))
        for symbol in operations:
            print(symbol)
        operation = input("Pick an operation: ")

        result = operations[operation](n1, n2)

        print(f"{n1} {operation} {n2} = {result}")

        answer = input(f"Type 'y' to continue calculating with {result}, or type 'n' to do a new calculation: ")

        if answer == "y":
            n1 = result
        else:
            calculator()    

calculator()
    



    


