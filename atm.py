def menus(pin, pin2):
    print("\nWelcome to the ATM Machine Portal!")
    if pin != pin2:
        print("PINs do not match. Please try again.")
        return None  # Return None if auth fails
    
    print("PIN confirmed. Access granted.\n")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    
    return input("Please enter your choice: ")

def options(choice, pin):
    if choice == '1':
        checkBalance()
    elif choice == '2':
        depositMoney()
    elif choice == '3':
        withdrawMoney(pin) # Pass pin here
    elif choice == '4':
        print("Thank you for using the ATM. Goodbye!")
    else:
        print("Invalid choice.")

def checkBalance():
    print("\nYour current balance is: $1,000.00")

def depositMoney():
    deposit_amount = int(input("Enter deposit amount: "))
    print(f"Success! New balance: ${1000 + deposit_amount}")

def withdrawMoney(pin):
    verify = input("Enter PIN to withdraw: ")
    if verify == pin:
        amount = int(input("Enter withdrawal amount: "))
        if amount > 1000:
            print("Insufficient funds.")
        else:
            print(f"Success! New balance: ${1000 - amount}")
    else:
        print("Incorrect PIN.")

def main():
    pin = input("Create your PIN: ")
    pin2 = input("Confirm your PIN: ")
    
    # Capture the choice from the menus function
    choice = menus(pin, pin2)
    
    if choice: # Only proceed if PINs matched
        options(choice, pin)

if __name__ == "__main__":
    main()
