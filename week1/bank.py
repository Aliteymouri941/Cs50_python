a = input("Greeting: ").strip().lower()

if a.startswith("hello"):
    b=0
elif a.startswith("h"):
    b=20
else:
    b=100
print(f"${b}")