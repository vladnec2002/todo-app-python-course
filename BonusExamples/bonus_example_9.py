password = input('Enter your password: ')

result = {}

if len(password) >= 8:
    result["lenght"] = True
else:
    result["lenght"] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True

result["digits"] = digit

upper = False
for i in password:
    if i.isupper():
        upper = True

result["uppercase"] = upper

print(result)

if all(result.values()):
    print('Strong password')
else:
    print('Weak password')
