def is_leap_year(year):
    """Encapsulates the leap year logic into a reusable function."""
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def main():
    print("=== Welcome to Leap Year Checker ===")
    print("Settings: Type 'settings' to toggle Infinity Mode\n")
    
    infinity_mode = False

    while True:
        user_input = input(f"\nEnter a year to check{' (Infinity Mode ON)' if infinity_mode else ''}: ").strip().lower()

        # Handle Settings Toggle
        if user_input == "settings":
            choice = input("Enable Infinity Mode? (yes/no): ").strip().lower()
            infinity_mode = (choice == "yes")
            print(f"--- Infinity Mode {'Enabled' if infinity_mode else 'Disabled'} ---")
            continue

        # Input Validation
        try:
            year = int(user_input)
        except ValueError:
            print("Invalid input! Please enter a numeric year.")
            continue

        # Year Constraint
        if year >= 2027:
            print("Please enter a year before 2027.")
            continue

        # Perform Check
        if is_leap_year(year):
            print(f"Yes, {year} is a leap year!")
        else:
            print(f"No, {year} is not a leap year.")

        # Loop Control
        if not infinity_mode:
            next_check = input("Check another year? (yes/no): ").strip().lower()
            if next_check != "yes":
                print("Thank you for using the app. Goodbye!")
                break

if __name__ == "__main__":
    main()