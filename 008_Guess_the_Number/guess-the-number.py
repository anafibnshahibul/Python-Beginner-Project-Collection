import random

def start_game():
    print("--- 🎯 Welcome to Number Guessing Game! 🎯 ---")
    
    # Selection of difficulty
    print("\nSelect Difficulty:")
    print("1. Easy (1-50)\n2. Medium (1-100)\n3. Hard (1-500)")
    choice = input("Enter choice (1/2/3): ")

    if choice == '1':
        upper_limit = 50
    elif choice == '3':
        upper_limit = 500
    else:
        upper_limit = 100

    secret_number = random.randint(1, upper_limit)
    attempts = 0
    score = 100

    print(f"\nI'm thinking of a number between 1 and {upper_limit}.")

    while True:
        try:
            guess = int(input("What's your guess? "))
            attempts += 1
            
            if guess < secret_number:
                print("Too low! ⬆️ Try a higher number.")
                score -= 5
            elif guess > secret_number:
                print("Too high! ⬇️ Try a lower number.")
                score -= 5
            else:
                print(f"\n🎉 BOOM! You found it in {attempts} tries!")
                print(f"Your final score is: {max(score, 0)}")
                break

            # Hint for very close guesses
            if abs(guess - secret_number) <= 5 and guess != secret_number:
                print("🔥 You are very close!")

        except ValueError:
            print("❌ Invalid input! Please enter a numeric value.")

if __name__ == "__main__":
    start_game()