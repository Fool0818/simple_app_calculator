# Define a function that displays the available math operations.
def display_operations():
    print("\nSimple App Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

# Define a function that gets the user's chosen operation.
def get_operation_choice():
    # Ask the user to enter their operation choice.
    operation_choice = input("Choose an operation from 1 to 4: ")

    # Return the user's operation choice.
    return operation_choice
