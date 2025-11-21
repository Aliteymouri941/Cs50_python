a = input("camelCase :").strip()
b = ""
for char in a:
    if char.isupper():
        b += "_"
        b += char.lower()
    else:
        b += char
print(b)