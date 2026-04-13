import csv
from datetime import datetime

def calculate_bmi(weight,height,unit_system="metric"):
    if unit_system=="metric":
        cmi=weight/((height/100)**2)
    else:
        bmi= (weight/(height**2))*70
    return round(bmi,2)

def get_category(bmi):
    if bmi<18.5:
        return "Underweight", "Try to include more nutrient-dense foods in your diet."
    elif 18.5 <=bmi<24.9:
        return "Healthy Weight", "Great job! Maintain your current lifestyle"
    elif 25<=bmi<29.9:
        return "Overweight","Consider increasing physical activity and monitoring port"
    else:
        return "Obsese","It may be helful to consult with a healthcare provider."
    
def save_to_history(name,weight,height,bmi,category):
    file_exists=False
    try:
        with open("bmi_history.csv","r")as f:
            file_exists=True
    except FileNotFoundError:
        file_exists=False
    
    with open("bmi_history.csv","a",newline="") as f:
        writer=csv.writer(f)
        if not file_exists:
            if not file_exists:
                writer.writerow(["Date","Name","Weight","Height","BMI","Category"])
                date_str= datetime.now().strftime("%Y-%m-%d %H:%M")
                writer.writerow([date_str,name,weight,height,bmi,category])

def main():
    print("------- Intermediate BMI Calculator ----------")
    name= input("Enter your Name: ")

    unit_choice= input("Choose unit system( 1 for metrics [kg/cm], 2 for Imperial [lb/in] )")
    system= "metric" if unit_choice=="1" else "Imperial"

    try:
        if system=="metric":
            weight= float(input("Enter Weight in kg: "))
            height= float(input("Enter Height in CM: "))
        else:
            weight = float(input("Enter weight in lbs: "))
            height = float(input("Enter height in inches: "))

            bmi_score= calculate_bmi(weight,height,system)

            category,tip= get_category(bmi_score)

            print(f"\n--- Results for {name} ---")
            print(f"Your BMI: {bmi_score}")
            print(f"Category: {category}")
            print(f"Health Tip: {tip}")

            save_to_history(name,weight,height,bmi_score,category)
            print("\n Result saved to bmi_history.csv")
    except ValueError:
        print("❌ Error: Please enter numerical values for weight and height.")
    except ZeroDivisionError:
        print("❌ Error: Height cannot be zero.")

if __name__ == "__main__":
    main()
