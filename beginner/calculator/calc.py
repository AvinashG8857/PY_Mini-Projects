def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def divide(x,y):
    if y ==0:
        raise ValueError("Divsion by zero")
    return x/y

print("Select operator: ")
print("1. Add")
print("2. Subtract")
print("3.multiply")
print("4.Divide")

while True:
    choice = input("Enter Your choice : ")

    if choice == "q":
        break

    if choice in ("1","2","3","4"):
        try:
            num1 = float(input("Enter your number :"))
            # print(f"{num1}")
            num2 = float(input("Enter your number :"))
            # print(f"{num2}")
        except ValueError:
            continue

        if choice == "1":
            print(add(num1,num2))
        elif choice == "2":
            print(sub(num1,num2))
        elif choice == "3":
            print(mul(num1,num2))
        elif choice== "4":
            print(divide(num1,num2))
    else:
        print("Invalid choice !")