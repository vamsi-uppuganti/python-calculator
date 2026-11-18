
def calculator():

    print("*********************")
    print("Python Calculator")
    print("*********************")

    while True:

        operation = input(
            "Choose an operation (+, -, *, /, exit): "
        )

        if operation == "exit":
            print("Thank you for using calculator!")
            break

        number = input("Enter numbers with spaces: ")

        try:
            args = [float(x) for x in number.split()]

            if len(args) < 2:
                print("Please enter at least two numbers")
                continue

            if operation == "+":
                result = sum(args)

            elif operation == "-":
                result = args[0]
                for i in args[1:]:
                    result -= i

            elif operation == "*":
                result = args[0]
                for i in args[1:]:
                    result *= i

            elif operation == "/":
                result = args[0]
                for i in args[1:]:
                    if i == 0:
                        raise ZeroDivisionError
                    result /= i

            else:
                print("Invalid operation")
                continue

            print("Result:", result)

        except ValueError:
            print("Please enter valid numbers!")

        except ZeroDivisionError:
            print("Cannot divide by zero!")


calculator()
