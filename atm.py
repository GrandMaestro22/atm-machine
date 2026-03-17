class Bank:
    def __init__(self, pin):
        self.pin = pin
        self.balance = 1000.00

    def menus(self, pin2):
        print("\nWelcome to the ATM Machine Portal!")
        if self.pin != pin2:
            print("PINs do not match. Please try again.")
            return None  # Return None if auth fails
        
        print("PIN confirmed. Access granted.\n")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        return input("Please enter your choice: ")

    def options(self, choice):
        if choice == '1':
            self.checkBalance()
        elif choice == '2':
            self.depositMoney()
        elif choice == '3':
            self.withdrawMoney()
        elif choice == '4':
            print("Thank you for using the ATM. Goodbye!")
        else:
            print("Invalid choice.")

    def checkBalance(self):
        print(f"\nYour current balance is: ${self.balance}")

    def depositMoney(self):
        deposit_amount = int(input("Enter deposit amount: "))
        self.balance += deposit_amount
        print(f"Success! New balance: ${self.balance}")

    def withdrawMoney(self):
        verify = input("Enter PIN to withdraw: ")
        if verify == self.pin:
            amount = int(input("Enter withdrawal amount: "))
            if amount > self.balance:
                print("Insufficient funds.")
            else:
                self.balance -= amount
                print(f"Success! New balance: ${self.balance}")
        else:
            print("Incorrect PIN.")

def main():
    pin = input("Create your PIN: ")
    pin2 = input("Confirm your PIN: ")

    bank = Bank(pin)

    while True:
        # Capture the choice from the menus function
        choice = bank.menus(pin2)

        if not choice:  # Only proceed if PINs matched
            break

        bank.options(choice)

        if choice == '4':
            break

if __name__ == "__main__":
    main()
