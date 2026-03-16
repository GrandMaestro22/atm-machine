# ATM Machine Portal

## Description
This Python program is a simple command-line ATM simulation. It asks the user to enter and confirm a PIN, then displays a menu with basic banking options such as checking a balance, depositing money, withdrawing money, or exiting the program.

## Features
- PIN confirmation before access is granted
- Balance inquiry
- Deposit money
- Withdraw money
- Exit the program

## How It Works
1. The user enters a PIN.
2. The user re-enters the PIN to confirm it.
3. If both PINs match, the program displays an ATM menu.
4. The user selects one of the available options:
   - `1` to check balance
   - `2` to deposit money
   - `3` to withdraw money
   - `4` to exit
5. The program runs the function that matches the selected option.

## Functions

### `menus(pin, pin2)`
- Welcomes the user
- Verifies that both PIN entries match
- Displays the ATM menu
- Returns the user's menu choice

### `options(choice)`
- Checks the user's menu selection
- Calls the correct function based on the selected option

### `checkBalance()`
- Displays instructions for checking balance
- Shows a fixed sample balance of `$1,000.00`

### `depositMoney()`
- Displays deposit instructions
- Prompts the user to enter an amount to deposit
- Adds the deposit to the sample balance of `$1000`

### `withdrawMoney(pin)`
- Displays withdrawal instructions
- Prompts the user to re-enter their PIN
- If the PIN is correct, asks for a withdrawal amount
- Prevents withdrawal if the amount is greater than `$1000`

### `main()`
- Starts the program
- Collects the PIN entries
- Displays the menu
- Processes the user's choice

## Requirements
- Python 3

## How to Run
```bash
python atm.py
```

## Notes
This program is a beginner-friendly ATM simulation. It uses a fixed starting balance of `$1000` and does not save account data permanently.

## Current Issues in the Code
- `menus()` is called a second time without the required arguments
- `withdrawMoney()` expects a `pin` argument, but `options()` calls it without one

## Summary
This project demonstrates:
- User input
- Functions
- Conditional statements
- Simple menu-driven program flow
