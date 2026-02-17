def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2


operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}


while True:
    import art
    print(art.logo)
    first_num = float(input("Enter a first number: "))

    is_continue_calculating = True
    while is_continue_calculating:
        operator = input("+\n-\n*\n/\npick a operator: ")
        second_num = float(input("Enter a first number: "))
        answer = operations[operator](first_num,second_num)
        print(f"{first_num} {operator} {second_num} = {answer}") # print(answer)
        should_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()
        if should_continue == "y":
            first_num = answer
        else: # elif should_continue == "n":
            is_continue_calculating = False
            print("\n"*30)
