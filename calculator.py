#Add, Subtract, Multiply, divide
def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y == 0:
        return "devision error!"
    return x/y



print("Choose what to do")
print("\nAdd\nSubtract\nMultiply\nDivide") 
operator = str(input("Enter what to do: ")).strip().lower()
x = int(input("Enter first value: "))
y = int(input("Enter first value: "))

if operator == "add":
    value = add(x,y)
    print(value)
elif(operator == "subtract"):
    value = subtract(x,y) 
    print(value)
elif(operator == "multiply"):
    value = multiply(x,y)
    print(value)
elif(operator == "divide"):
    value = divide(x,y) 
    print(value) 
else:
    print("choose a valid operator!add")            