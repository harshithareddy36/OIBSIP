def get_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Error: enter a number greater than 0.")
            else:
                return value
        except ValueError:
            print("Error: please enter numbers only.")

def classify(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

print("=== BMI Calculator ===")
weight = get_number("Enter weight in kg: ")
height = get_number("Enter height in meters (e.g. 1.65): ")

bmi = weight / (height ** 2)
print(f"Your BMI is {bmi:.2f}")
print(f"Category: {classify(bmi)}")