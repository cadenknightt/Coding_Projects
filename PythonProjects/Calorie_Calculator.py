# Main Calorie Calcualtion function.
def calculate_calorie_goal():
     print("\nWelcome to the Calorie Goal Calculator!\n")
     print("I will give you some prompts to fill in and you will\nbe given the essential information for your fitness journey!\n")

     # User enters Gender.
     while True:
          try:
               gender = input("Enter your gender (m/f): ")
               if gender.lower() not in ["male","m"] and gender.lower() not in ["female","f"]:
                    print("Gender must be Male or Female.\n")
                    continue
               break
          except ValueError:
               print("Try again.\n")
          break

     # User enters Age if 8 or older.
     while True:
          try:
               age = int(input("Enter your age: "))
               if age <= 8:
                    print("Age must be 8 or older.\n")
                    continue
               break
          except ValueError:
               print("Try again.\n")
          break
     
     # Asks user which measurement system they use for easier data entry.
     while True:
          try:
               system = input("Imperial or Metric system (i/m): ").lower()
               if system not in ["imperial","i","metric","m"]:
                    print("Please enter imperial or metric.\n")
                    continue
               break
          except ValueError:
               print("Try again.\n")
          break     
          
     # Enter height and weight that is aligned with selected measurement system.
     while True:
          if system in ["imperial","i"]:
               print("\nPlease enter feet, inches, and weight separately.\n")
               try:
                    feet = int(input("Feet: "))
                    inches = int(input("Inches: "))
                    lbs = float(input("Weight (ex: 160.2): "))
                    if feet < 3 and feet > 8:
                         print("Feet must fall within 3 and 8.\n")
                         continue
                    elif inches < 0 and inches > 11:
                         print("Inches must be between 0 and 11.\n")
                         continue
                    elif lbs <= 0:
                         print("Weight must be greater than 0.\n")
                         continue
                    break
               except ValueError:
                    print("Value must be a whole number.\n")
          elif system in ["metric","m"]:
               print("\nPlease enter centimeters (height) and kilograms (weight) separately.\n")
               try:
                    centimeters = float(int("Centimeters (ex: 184.2): "))
                    kilograms = float(input("Kilograms (ex: 76.7): "))
                    if centimeters < 90:
                         print("Centimeters must be greater than 90.\n")
                         continue
                    elif kilograms < 0:
                         print("Kilograms must be greater than 0.\n")
                         continue
                    break
               except ValueError:
                    print("Value must be a decimal.\n")
               break
          else:
               break
          break

     # Allows user to specify workout goal
     while True:
          print("""
     GOAL           |            DESCRIPTION
     -----------------------------------------------------------
     Intense Cut    |       Risk muscle loss, extreme fat loss.
     Slow Cut       |       Preserve muscle, while losing fat.
     Recomp         |       Build muscle, while losing fat.
     Lean Bulk      |       Slow muscle gain, limited fat gain.
     Dirty Bulk     |       Quick muslce and fat gain.\n
          """)
          goal = input("Enter your goal here (ic/sc/r/lb/db): ").lower()

          if goal not in ["intense cut","ic", "slow cut","sc", "recomp","r", "lean bulk","lb", "dirty bulk","db"]:
               print("Please provide a plan from the list.\n")

          if goal in ["intense cut", "ic"]:
               try:
                    print("\nProvide a calorie deficit for your Intense Cut.")
                    intakenum = int(input("Enter a number between -700 and -1000: "))
                    if intakenum < -1000:
                         print("Number must be greater than -1000.\n")
                         continue
                    elif intakenum > -700:
                         print("Number must be less than -700.\n")
                         continue
                    break
               except:
                    print("Enter a valid number.\n")
               break
          elif goal in ["slow cut", "sc"]:
               try:
                    print("\nProvide a calorie deficit for your Slow Cut.")
                    intakenum = int(input("Enter a number between -600 and -300: "))
                    if intakenum < -1000:
                         print("Number must be greater than -600.\n")
                         continue
                    elif intakenum > -700:
                         print("Number must be less than -300.\n")
                         continue
                    break
               except:
                    print("Enter a valid number.\n")
               break
          elif goal in ["recomp", "r"]:
               try:
                    print("\nProvide a calorie deficit for your Recomp.")
                    intakenum = int(input("Enter a number between -200 and 0: "))
                    if intakenum < -200:
                         print("Number must be greater than -200.\n")
                         continue
                    elif intakenum > 0:
                         print("Number must be less than 0.\n")
                         continue
               except:
                    print("Enter a valid number.\n")
               break
          elif goal in ["lean bulk", "lb"]:
               try:
                    print("\nProvide a calorie surplus for your Lean Bulk.")
                    intakenum = int(input("Enter a number between 200 and 450: "))
                    if intakenum < 200:
                         print("Number must be greater than 200.\n")
                         continue
                    elif intakenum > 450:
                         print("Number must be less than 450.\n")
                         continue
               except:
                    print("Enter a valid number.\n")
               break
          elif goal in ["dirty bulk", "db"]:
               try:
                    print("\nProvide a calorie surplus for your Dirty Bulk.")
                    intakenum = int(input("Enter a number between 500 and 750: "))
                    if intakenum < 500:
                         print("Number must be greater than 500.\n")
                         continue
                    elif intakenum > 750:
                         print("Number must be less than 750.\n")
                         continue
               except:
                    print("Enter a valid number.\n")
               break
          else:
               print("Please enter one of the goals.\n")
          break

     while True:
          # Calculate weight and height based on user's system measurement preference earlier.
          if system in ["imperial","i"]:
               weight_kg = (lbs/2.20462)
               height_cm = (feet*30.48) + (inches*2.54)
          elif system in ["metric","m"]:
               weight_kg = weight_kg
               height_cm = height_cm
          else:
               raise ValueError("System must be 'Imperial' or 'Metric'.\n")
          break

     # Calcualtes Basic Metabolism Rate based on the gender the user selected.
     while True:
          if gender in ["male","m"]:
               bmr = (10*weight_kg) + (6.25*height_cm) - (5*age) + 5
          elif gender in ["female","f"]:
               bmr = (10*weight_kg) + (6.25*height_cm) - (5*age) - 161
          else:
               raise ValueError("Gender must be 'Male' or 'Female'.\n")
          break

     # Allows user to specify activity level.
     while True:
          print("""
     ACTIVITY LEVEL   |       DESCRIPTION
     -----------------------------------------------------------
     Sedentary        |       No lifting
     Light            |       Exercise 1-3x per week.
     Moderate         |       Exercise 3-5x per week.
     High             |       Exercise 6-7x per week.
     Intense          |       Extreme exercise 7x per week.
          """)
          activity = input("Enter your activity level (s/l/m/h/i): ").lower()

          # Code checks users input and if not one of the options, gives a error.  
          if activity not in ["sedentary", "s", "light", "l", "moderate", "m", "high", "h", "intense", "i"]:
               print("Please provide one of the options in the 'ACTIVITY LEVEL' column.\n")
          
          # Code defines multipliers for the activity levels.
          activity_factors = {
               "sedentary": 1.15,
               "s": 1.15,
               "light": 1.36,
               "l": 1.36,
               "moderate": 1.52,
               "m": 1.52,
               "high": 1.71,
               "h": 1.71,
               "intense": 1.87,
               "i": 1.87
               }
          
          # Code checks if activity level is not in the activity_factors list, gives error if not.
          if activity not in activity_factors:
               raise ValueError("Invalid activity level.\n")
          
          # Calculates the Total Daily Expenditure for user.
          tdee = bmr * activity_factors[activity]
          # Calculates the total calories a user needs for their fitness goal.
          calories = tdee + intakenum
          # Code prints a list showing all the requirements for their fitness goal.
          print(f"\n\nDAILY REQUIREMENTS:\nCalories: {calories:,.0f} kcal")
          break

# Runs the calcualtion program and ends with prompt allowing user to continue or not.   
while True:
          calculate_again = input("\nWould you like to calculate again? (y/n): ").strip().lower()
          if calculate_again in ["yes", "y"]:
               calculate_calorie_goal()
          elif calculate_again in ["no", "n"]:
               print("Thanks for playing!\n")
               break
          else:
               print("Please enter 'y' for yes or 'n' for no.\n")

if __name__ == "__main__":
     calculate_calorie_goal()
