# Project Title : Daily Calorie Tracker CLI
# Course        : Programming for Problem Solving using Python
# Name          : Aarav Jaiswal
# Date          : 24th October 2025
# Assignment    : Mini Project - Building a Calorie Tracking Console App


import datetime

# ------------------- Task 1: Setup & Introduction -------------------
print("===============================================")
print("         Welcome to the Daily Calorie Tracker  ")
print("===============================================")
print("This tool helps you log your meals, track total calories,")
print("compare them with your daily limit, and optionally save")
print("your session for future reference.\n")

# ------------------- Task 2: Input & Data Collection -------------------
meal_names = []
calories = []

# Ask the user for the number of meals
num_meals = int(input("How many meals do you want to enter today? "))

for i in range(num_meals):
    print(f"\nEnter details for meal {i+1}:")
    meal = input("Meal name: ")
    cal = float(input("Calories for this meal: "))
    
    # Add to lists
    meal_names.append(meal)
    calories.append(cal)

# ------------------- Task 3: Calorie Calculations -------------------
total_calories = sum(calories)
average_calories = total_calories / num_meals
daily_limit = float(input("\nEnter your daily calorie limit: "))

# ------------------- Task 4: Exceed Limit Warning System -------------------
if total_calories > daily_limit:
    status = "⚠️  You have exceeded your daily calorie limit!"
else:
    status = "✅ You are within your daily calorie limit!"

# ------------------- Task 5: Neatly Formatted Output -------------------
print("\n\n=========== DAILY CALORIE SUMMARY ===========")
print("Meal Name\tCalories")
print("---------------------------------------------")

for i in range(num_meals):
    print(f"{meal_names[i]:<12}\t{calories[i]:>8.2f}")

print("---------------------------------------------")
print(f"Total:\t\t{total_calories:.2f}")
print(f"Average:\t{average_calories:.2f}")
print("---------------------------------------------")
print(status)
print("=============================================\n")

# ------------------- Task 6 (Bonus): Save Session Log -------------------
save_choice = input("Do you want to save this session log? (yes/no): ").strip().lower()

if save_choice == "yes":
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Save to file
    with open("calorie_log.txt", "a") as f:
        f.write(f"\n===== Calorie Tracker Log - {timestamp} =====\n")
        for i in range(num_meals):
            f.write(f"{meal_names[i]:<12}\t{calories[i]:>8.2f}\n")
        f.write("---------------------------------------------\n")
        f.write(f"Total:\t\t{total_calories:.2f}\n")
        f.write(f"Average:\t{average_calories:.2f}\n")
        f.write(f"Daily Limit:\t{daily_limit:.2f}\n")
        f.write(f"Status: {status}\n")
        f.write("=============================================\n")

    print("\n💾 Log saved successfully to 'calorie_log.txt'!")
else:
    print("\nNo problem! Log not saved.")

print("\nThank you for using the Daily Calorie Tracker!")
