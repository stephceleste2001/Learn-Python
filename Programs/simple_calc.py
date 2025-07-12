print("Select an operation to operation to perform:")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")
operation = int(input("Choose an operation: "))
result = 0

if (operation in [1,2,3,4,5]):
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if (operation == 1):
        result = num1 + num2
    elif(operation == 2):
        result = num1 - num2
    elif(operation == 3):
        result = num1 * num2
    elif(operation == 4):
        result = num1 // num2
    
    else:
        print("Invalid Operation entered")

print("The result of the operation is {}".format(result))