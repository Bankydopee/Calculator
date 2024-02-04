def add():
    num1 = 5
    num2 = 5
    sum = num1 + num2
    print(sum, "is gretater than five")

#add()
# Calculator Operators

def Calculator():
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))
    operator = input("Enter an operator: ")

    if operator == "+":
        sum = num1 + num2
        print(sum)
    elif operator == "-":
        difference = num1 - num2
        print(difference)
    elif operator == "*":
        product = num1 * num2
        print(product)
    elif operator == "/":
        division = num1 / num2
        print(division)
        
Calculator()

def velocity():
    distance = int(input("Enter distance: "))
    time = int(input("Enter time: "))
    velocity = distance / time
    print(velocity, "is the velocity")

velocity()