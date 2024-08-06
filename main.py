def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def main():
    print("Simple Calculator")
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            operation = input("Enter operation (+, -, *, /): ")

            if operation == '+':
                print(f"Result: {add(num1, num2)}")
            elif operation == '-':
                print(f"Result: {subtract(num1, num2)}")
            elif operation == '*':
                print(f"Result: {multiply(num1, num2)}")
            elif operation == '/':
                print(f"Result: {divide(num1, num2)}")
            else:
                print("Invalid operation")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
