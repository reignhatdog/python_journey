num1 = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if op == "+":
    print("the result is:", num1 + num2)
elif op == "-":
    print("the result is:", num1 - num2)
elif op == "*":
    print("the result is:", num1 * num2)
elif op == "/":
    if num2 != 0: 
        print("The result is:", num1 / num2)



   