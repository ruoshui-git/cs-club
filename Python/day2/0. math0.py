def get_int(hint):
    result = None
    while result is None:
        try:
            result = int(input(hint))
        except ValueError:
            pass
    return result

print('enter two integers x and y')

x = get_int("x: ")
y = get_int("y: ")

print(f"x + y = {x + y}")
print(f"x - y = {x - y}")
print(f"x * y = {x * y}")
print(f"x / y = {x / y}")
print(f"x mod y = {x % y}")