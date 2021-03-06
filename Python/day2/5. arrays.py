def get_int(hint):
    result = None
    while result is None:
        try:
            result = int(input(hint))
        except ValueError:
            pass
    return result

numbers = []

# Prompt for numbers (until EOF)
while True:

    # Prompt for number
    number = get_int("number: ")

    # Check for EOF
    if not number:
        break

    # Check whether number is already in list
    if number not in numbers:

        # Add number to list
        numbers.append(number)

# Print numbers
print()
for number in numbers:
    print(number)