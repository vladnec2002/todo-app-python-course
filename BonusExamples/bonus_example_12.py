feet_inches = input("Enter your feet inches: ")

def convert(feet_inches):
    parts = feet_inches.split(" ")
    print(parts)
    feet = float(parts[0])
    inches = float(parts[1])

    meters = feet * 0.3048 + inches * 0.0254
    return meters

result = convert(feet_inches)
print(result)

if result < 1:
    print("Too small")
else:
    print("OK")