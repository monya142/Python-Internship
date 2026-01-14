
def show_intro():
    print("=" * 45)
    print("        WELCOME TO BMI CALCULATOR")
    print("=" * 45)
    print("This program calculates your BMI")
    print("BMI = weight (kg) / height (m)^2")
    print("-" * 45)


def get_weight():
    while True:
        try:
            weight = float(input("Enter your weight in kilograms: "))
            if weight <= 0:
                print("Weight must be greater than zero.")
            else:
                return weight
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_height():
    while True:
        try:
            height = float(input("Enter your height in meters: "))
            if height <= 0:
                print("Height must be greater than zero.")
            else:
                return height
        except ValueError:
            print("Invalid input. Please enter a number.")


def calculate_bmi(weight, height):
    return weight / (height ** 2)


def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def display_result(bmi, category):
    print("\n" + "-" * 45)
    print(f"Your BMI value is : {bmi:.2f}")
    print(f"BMI Category    : {category}")
    print("-" * 45)


def ask_repeat():
    choice = input("Do you want to calculate BMI again? (yes/no): ").lower()
    return choice == "yes"


def main():
    show_intro()

    while True:
        weight = get_weight()
        height = get_height()

        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)

        display_result(bmi, category)

        if not ask_repeat():
            print("\nThank you for using the BMI Calculator.")
            print("Stay healthy and take care!")
            break

if __name__ == "__main__":
    main()
