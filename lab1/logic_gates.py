def logic_identifier(x, y, z):
    #logic based on the last short quiz that sir gave
    return not(not(x) and y and z) and (not(x) or y or not(z))

def get_input(prompt):
    while True:
        try:
            value = input(prompt)
            return bool(int(value))
        except ValueError:
            print("Invalid input. Please enter 0f or 1.")

x = get_input("Enter x (0 or 1): ")
y = get_input("Enter y (0 or 1): ")
z = get_input("Enter z (0 or 1): ")

result = logic_identifier(x, y, z)
print(f"Result of logic_identifier({x}, {y}, {z}): {result}")
