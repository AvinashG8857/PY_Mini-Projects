from database import init_db
from tracker import add_expenses,generate_report

def main():
    init_db()

    while True:
        print("\n--- EXPENSE TRACKER -----")
        print("1.record an Expense")
        print("2. see Anlaysis & chart")
        print("3. Exit")

        choice= input("select the option (1-3) : ")
        if choice=="1":
            try:
                amount= float(input("How much Did you spend? "))
                cat= input("Category (Food| Rent| Fun| Others): ").capitalize()
                desc= input("Quick descriptions: ")

                add_expenses(amount, cat,desc)
                print("saved")
            except ValueError:
                print(":Error please enter a numeric amount")
        
        elif choice == "2":
            generate_report()

        elif choice == "3":
            print("Saving data and exiting. Bye!")
            break
        else:
            print("Invalid choice. Please pick 1,2,3")


if __name__ == "__main__":
    main()