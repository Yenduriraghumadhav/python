for num in range(9):
    print("number in loop ",num)
    if num % 2 > 0:
        print("odd",num)
        continue  # Skip even numbers
print("number after",num)