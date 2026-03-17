# ATM Machine (Python)

Simple command-line ATM simulation built with Python.

## Features
- Create and confirm a PIN before using the ATM
- Check current account balance
- Deposit money into the account
- Withdraw money with PIN verification
- Repeat transactions until the user exits

## Project Structure
- `atm.py`: Main application file with the `Bank` class and program entry point

## Requirements
- Python 3.8+

## Run the App
From the project folder, run:

```bash
python atm.py
```

On some Windows setups, use:

```bash
py atm.py
```

## How It Works
1. User creates a PIN and confirms it.
2. A `Bank` object is created with:
   - Initial balance: `1000.00`
   - Saved PIN for verification
3. The menu is shown in a loop:
   - `1` Check Balance
   - `2` Deposit Money
   - `3` Withdraw Money
   - `4` Exit
4. Withdrawals require entering the correct PIN again.

## Class Overview
### `Bank`
- `__init__(pin)`: Stores PIN and starting balance
- `menus(pin2)`: Confirms setup PIN and returns user menu choice
- `options(choice)`: Routes selected menu action
- `checkBalance()`: Displays current balance
- `depositMoney()`: Adds user-entered amount to balance
- `withdrawMoney()`: Verifies PIN and subtracts withdrawal amount if valid

## Notes
- Data is stored in memory only and resets each run.
- This is a learning project and does not include database storage, encryption, or advanced validation.

## Possible Improvements
- Validate input to prevent non-numeric amount errors
- Prevent negative deposits/withdrawals
- Hide PIN input with `getpass`
- Save account data to a file or database
