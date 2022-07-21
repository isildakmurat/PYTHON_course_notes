print("Simple Calculator v.2")

num_1 = float(input("First number: "))  #ilk numarayı gir
num_2 = float(input("Second number: ")) #ikinci numarayı gir
op = input("Which Operation? (+, -, *, /): ") #işlemi gir
if op == "+":
    print("Result:", num_1, "+", num_2, "=", num_1 + num_2)
elif op == "-":
    print("Result:", num_1, "-", num_2, "=", num_1 - num_2)
elif op == "*":
    print("Result:", num_1, "*", num_2, "=", num_1 * num_2)
elif op == "/":
    print("Result:", num_1, "/", num_2, "=", num_1 / num_2)
else:
    print("you made a mistake!")