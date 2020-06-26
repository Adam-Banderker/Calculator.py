#Create a calculate having different options such as Addition/Subtraction/multiplication/Division/Exit
#Define every option in functions

def add(x,y):
    return x + y
def sub(x,y):
    return x - y
def div(x,y):
    return x/y
def multi(x,y):
    return x * y
def exit(x):
    return x

#Display the options for user to select
print("Please select an option:")
print("1.Addition")
print("2.Subtraction")
print("3.Division")
print("4.Multiplication")
print("5.Exit")

# create varible that consist of user input
# if user input is between 1 - 4 the calculator will proceed to ask what the first and second number is
# otherwise if user input is 5 the calculator will close
while True:
    choice = input("Enter choice(1/2/3/4/5): ")
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", sub(num1, num2))
        elif choice == '3':
             print(num1, "/", num2, "=", div(num1, num2))
        elif choice == '4':
            print(num1, "*", num2, "=", multi(num1, num2))
    else:
        print(exit("The calculator has ended"))
        break
        
