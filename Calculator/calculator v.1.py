print("Simple Calculator v.1")

num_1 = float(input("First number: "))
num_2 = float(input("Second number: "))
op = input("operation? (+, -, *, /): ")
if op == "+":
    print("Result:", num_1 + num_2)
elif op == "-":
    print("Result:", num_1 - num_2)
elif op == "*":
    print("Result:", num_1 * num_2)
elif op == "/":
    print("Result:", num_1 / num_2)
else:
    print("you made a mistake!")