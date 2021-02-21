def calculator():

    print('Simple Calculator App')

    # Calculator Operations
    add = lambda a, b : a + b
    subtract = lambda a, b: a - b
    multiply = lambda a, b: a * b
    divide = lambda a, b: a / b

    # Dictionary of operations
    ops = {
        "1": ["+", add],
        "2": ["-", subtract],
        "3": ["*", multiply],
        "4": ["/", divide]
    }


    def choice():
        op_choice = 0
        while int(op_choice) not in [1,2,3,4]:
            op_choice = input("""Choose your operation: (1-4)
1. Add
2. Subtract
3. Multiply
4. Divide\n""")
        return op_choice


    def number_input():
        a, b = 'a', 'b' # Placeholders for while loop
        while not (str(a).replace('.','',1).replace('-','',1).isdigit() and
                   str(b).replace('.','',1).replace('-','',1).isdigit()):
            try:
                a = float(input("Enter first number to process: "))
                b = float(input("Enter second number to process: "))
            except ValueError:
                continue
        return [a,b]
        

    def processor():
        op = choice()
        num = number_input()
        print(f"{num[0]} {ops[op][0]} {num[1]} = {ops[op][1](num[0], num[1])}")


    end = ''
    while end.lower() != 'n':
        processor()
        end = input("Calculate another problem? (Y/N) ")


if __name__ == "__main__":
    calculator()
        
