result = input("Expression:").strip()
x , operator , y = result.split(" ")
x = int(x)
y = int(y)
if operator == "+":
    container=x+y
elif operator == "-":
    container=x-y
elif operator == "/":
    container=x/y
elif operator == "*":
    container=x*y
else:
    print("something ist wrong")
    exit()
print(f"{container:.1f}")
