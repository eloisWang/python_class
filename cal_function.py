# code for calculator

# add
# mul
# sub
# div
operation_keywords = "ADD MUL SUB DIV"

def add(a, b):
    return a + b


def mul(a, b):
    return a * b


def sub(a, b):
    return a - b


def div(a, b):
    return a/b


def operation_function(operation_type,a,b):


    if operation_type.upper() == "ADD":
        print(f"Output for {a} + {b} =", add(a, b))
    elif operation_type.upper() == "MUL":
        print(f"Output for {a} * {b} =", mul(a, b))
    elif operation_type.upper() == "SUB":
        print(f"Output for {a} - {b} =", sub(a, b))
    elif operation_type.upper() == "DIV":
        print(f"Output for {a} / {b} =", div(a, b))
    else:
        print(f"You entered wrong operation, please enter {operation_keywords}")




while True:
    try:
        operation_type = input(f"What calculation you want to perform? {operation_keywords}:")

        a = int(input("Enter a value:"))
        b = int(input("Enter b value:"))

        operation_function(operation_type,a,b)
        ask_continue = input(f"Do you want to continue? y/n")
        if ask_continue == "y" :
            continue
        else:
            break

    except:
        print("please enter number")



print("Finish")
