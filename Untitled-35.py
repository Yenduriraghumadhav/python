try:
    # Input from user
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a smaller number than num1: "))

    # Check if num1 is greater than num2
    if num1 > num2:
        # Define functions
        def addition(num1, num2):
            total = num1 + num2
            print(f"Addition of given numbers: {total}")

        def subtraction(num1, num2):
            print("Subtraction: ", num1 - num2)

        def multiplication(num1, num2):
            print("Multiplication: ", num1 * num2)

        def division(num1, num2):
            try:
                print("Division: ", num1 / num2)
            except ZeroDivisionError:
                print("Error: Division by zero is not allowed.")

        # Call functions
        addition(num1, num2)
        subtraction(num1, num2)
        multiplication(num1, num2)
        division(num1, num2)
    else:
        print("Error: num1 should be greater than num2. Please try again.")

except ValueError:
    print("Error: Please enter valid numbers.")
else:
    print("All operations were successful!")
finally:
    print("Program execution completed.")
