# Move balance outside so all functions can see it
balance = 1000000 
PIN = 1234

def check_balance():
    # Accessing the global balance
    print(f"Your Current Balance is: {balance} Rupees only")

def deposit():
    global balance
    try:
        damount = int(input("Enter your Deposit amount: "))
        if damount > 0:
            balance += damount
            print("Successfully Deposited")
        else:
            print("Amount must be positive!")
    except ValueError:
        print("Invalid input! Please enter a number.")

def withdraw():
    global balance
    try:
        amount = int(input("Enter the Withdrawal amount: "))
        if amount <= balance:
            balance -= amount
            print("Transaction Successful")
        else:
            print("Insufficient Balance")
    except ValueError:
        print("Invalid input! Please enter a number.")

def main():
    print('--- Welcome to ATM Simulator ---')
    print('Insert your Card')
    
    try:
        confirm_pin = int(input("Enter Your Pin: "))
        
        if PIN == confirm_pin:
            while True: # Added a loop to make it like a real ATM
                print("\n1. Balance Inquiry")
                print("2. Money Withdrawal")
                print("3. Money Deposit")
                print("4. Exit")
                
                option = int(input("Select an option (1/2/3/4): "))

                if option == 1:
                    check_balance()
                elif option == 2:
                    withdraw()
                elif option == 3:
                    deposit()
                elif option == 4:
                    print("Thank You for using our ATM.")
                    break
                else:
                    print("Invalid Option")
        else:
            print("Invalid PIN")
            
    except ValueError:
        print("Error: Please enter numbers only.")

if __name__ == "__main__":
    main()