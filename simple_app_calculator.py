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

# Define a function that gets a number from the user.
def get_number(number_label):
    # Ask the user to enter a number and convert it to float.
    user_number = float(input(f"Enter {number_label} number: "))

    # Return the number entered by the user.
    return user_number

# Define a function that performs the selected calculation.
def calculate_result(operation_choice, first_number, second_number):
    # Check if the user chose addition.
    if operation_choice == "1":

        # Add the two numbers.
        calculation_result = first_number + second_number

    # Check if the user chose subtraction.
    elif operation_choice == "2":

        # Subtract the second number from the first number.
        calculation_result = first_number - second_number

    # Check if the user chose multiplication.
    elif operation_choice == "3":

        # Multiply the two numbers.
        calculation_result = first_number * second_number

    # Check if the user chose division.
    elif operation_choice == "4":

        # Check if the second number is zero.
        if second_number == 0:

            # Raise an error because division by zero is not allowed.
            raise ZeroDivisionError("Cannot divide by zero.")

        # Divide the first number by the second number.
        calculation_result = first_number / second_number

    # Run this block if the user chose an invalid operation.
    else:

        # Raise an error because the operation choice is invalid.
        raise ValueError("Invalid operation choice.")

    # Return the final calculation result.
    return calculation_result

