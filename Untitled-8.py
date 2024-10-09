
number_i = "abc"
# num = int(number_i)
try:
    num = int(number_i)
except ValueError:
    print("Cannot convert 'abc' to an integer.")  # Output: Cannot convert 'abc' to an integer.
