# Taking user input and converting it
user_input = input("Enter a number: ")  # Example input: 5.5
float_num = float(user_input)  # Convert string input to float
int_num = int(float_num)        # Convert float to integer (will truncate)

print("As a float:", float_num)  # Output: 5.5
print("As an integer:", int_num)  # Output: 5
