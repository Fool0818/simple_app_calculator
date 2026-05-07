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

# Define the main function of the calculator program.
def run_calculator():
    # Set the starting value so the program will run at least once.
    try_again_answer = "yes"

    # Repeat the calculator while the user wants to try again.
    while try_again_answer == "yes":

        # Use try block to catch possible runtime errors.
        try:

            # Display the available math operations.
            display_operations()

            # Get the operation choice from the user.
            operation_choice = get_operation_choice()

            # Get the first number from the user.
            first_number = get_number("first")

            # Get the second number from the user.
            second_number = get_number("second")

            # Calculate the result using the selected operation.
            calculation_result = calculate_result(
                operation_choice,
                first_number,
                second_number
            )

            # Display the result to the user.
            print(f"The result is: {calculation_result}")

            # Catch invalid number input or invalid operation choice.
        except ValueError as error_message:

            # Display the error message.
            print(f"Error: {error_message}")

        # Catch division by zero error.
        except ZeroDivisionError as error_message:

            # Display the error message.
            print(f"Error: {error_message}")

        # Catch any other unexpected error.
        except Exception as error_message:

            # Display the unexpected error message.
            print(f"Unexpected error: {error_message}")

        # Ask the user if they want to try again.
        try_again_answer = input(
            "Do you want to try again? Type yes or no: "
        ).lower()

        # Keep asking if the answer is not yes or no.
        while try_again_answer != "yes" and try_again_answer != "no":

            # Tell the user to enter only yes or no.
            print("Please type yes or no only.")

            # Ask the user again.
            try_again_answer = input(
                "Do you want to try again? Type yes or no: "
            ).lower()

    # Display thank you message before the program exits.
    print("Thank you!")


# Run the calculator program.
run_calculator()
