# calculator.py

# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract two numbers
def subtract(a, b):
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Function to divide two numbers
def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b


# Display menu options
print("Simple Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Take user choice
choice = input("Choose operation (1/2/3/4): ")

# Take numbers as input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform selected operation
if choice == "1":
    print("Result:", add(num1, num2))
elif choice == "2":
    print("Result:", subtract(num1, num2))
elif choice == "3":
    print("Result:", multiply(num1, num2))
elif choice == "4":
    print("Result:", divide(num1, num2))
else:
    print("Invalid choice")