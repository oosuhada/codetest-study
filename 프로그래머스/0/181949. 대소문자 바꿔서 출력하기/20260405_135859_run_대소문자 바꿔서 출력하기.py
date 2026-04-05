s = input()
result = ""

for char in s:
    if char.isupper():
        result += char.lower()
    else:
        result += char.upper()

print(result)