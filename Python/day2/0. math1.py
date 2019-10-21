def get_float(hint):
    result = None
    while result is None:
        try:
            result = float(input(hint))
        except ValueError:
            pass
    return result

x = get_float("x: ")

y = get_float("y: ")

z = x / y

print(f"x / y = {z}")
print(f"x / y = {z:.50f}")

print("is x + y - y == x?", x + y - y == x)
print("then what is x, eventually?", x + y - y)
