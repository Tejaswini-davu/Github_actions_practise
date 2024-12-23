# Function to calculate the square of a number
def square(num):
    return num ** 2

# Function to add two numbers
def add_numbers(num1, num2):
    return num1 + num2

# Function to subtract two numbers
def subtract_numbers(num1, num2):
    return num1 - num2

# Main function to execute the program
def main():
    print("Choose an operation:")
    print("1: Square a number")
    print("2: Add two numbers")
    print("3: Subtract two numbers")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        num = float(input("Enter the number to square: "))
        result = square(num)
        print(f"The square of {num} is: {result}")
    elif choice == "2":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = add_numbers(num1, num2)
        print(f"The sum of {num1} and {num2} is: {result}")
    elif choice == "3":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = subtract_numbers(num1, num2)
        print(f"The difference between {num1} and {num2} is: {result}")
    else:
        print("Invalid choice. Please try again.")

# Execute the main function
if __name__ == "__main__":
    main()
