def main():
    operations = {
        1: "1. Addition",
        2: "2. Subtraction",
        3: "3. Multiply",
        4: "4. Division"
    }
    
    for key in operations:
        print(operations[key])
    
    choice = int(input("Enter your choice (1-4): "))
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    
    if choice == 1:
        addition(a, b)
    elif choice == 2:
        subtraction(a, b)
    elif choice == 3:
        multiply(a, b)
    elif choice == 4:
        if b == 0:
            print("Error: Division by zero is not allowed.")
        else:
            division(a, b)
    else:
        print("Invalid choice. Please select a number between 1 and 4.")

def addition(a, b):
    print("Result:", a + b)

def subtraction(a, b):
    print("Result:", a - b)
    
def multiply(a, b):
    print("Result:", a * b)
    
def division(a, b):
    print("Result:", a / b)

main()
