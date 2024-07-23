try:
    name = str(input('Name: '))
    if not name:
        raise ValueError("Name cannot be empty")
except ValueError as ve:
    print("Error:", ve)
    exit()

try:
    age = int(input('Age: '))
    if age <= 0:
        raise ValueError("Age must be a positive integer")
except ValueError as ve:
    print("Error:", ve)
    exit()

print("Name:", name)
print("Age:", age)
