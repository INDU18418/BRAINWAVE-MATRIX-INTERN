# ATM Interface
import sys
import time
# Simulated user database
users = {
    "1234": {"name": "Alice", "balance": 1500.0},
    "5678": {"name": "Bob", "balance": 3000.0}
}
# === Authentication ===
def authenticate():
    print("===== Welcome to the ATM =====")
    attempts = 3
    while attempts > 0:
        pin = input("Enter your 4-digit PIN: ")
        if pin in users:
            print(f"\nAccess granted. Welcome, {users[pin]['name']}!\n")
            return pin
        else:
            attempts -= 1
            print(f"Invalid PIN. {attempts} attempt(s) remaining.\n")
    print("Too many incorrect attempts. Card retained.")
    sys.exit()
# === ATM Operations ===
def check_balance(user_data):
    print(f"\nYour current balance is: ${user_data['balance']:.2f}\n")
def deposit(user_data):
    try:
        amount = float(input("Enter amount to deposit: $"))
        if amount <= 0:
            print("Deposit must be a positive amount.\n")
        else:
            user_data['balance'] += amount
            print(f"${amount:.2f} deposited successfully.")
            check_balance(user_data)
    except ValueError:
        print("Invalid input. Please enter a number.\n")
def withdraw(user_data):
    try:
        amount = float(input("Enter amount to withdraw: $"))
        if amount <= 0:
            print("Withdrawal must be a positive amount.\n")
        elif amount > user_data['balance']:
            print("Insufficient funds.\n")
        else:
            user_data['balance'] -= amount
            print(f"${amount:.2f} withdrawn successfully.")
            check_balance(user_data)
    except ValueError:
        print("Invalid input. Please enter a number.\n")
# === ATM Menu ===
def atm_menu(user_pin):
    user_data = users[user_pin]
    while True:
        print("====== ATM Menu ======")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            check_balance(user_data)
        elif choice == "2":
            deposit(user_data)
        elif choice == "3":
            withdraw(user_data)
        elif choice == "4":
            print("Thank you for using our ATM. Goodbye!")
            break
        else:
            print("Invalid option. Please select from 1 to 4.\n")
# === Main ===
def main():
    user_pin = authenticate()
    atm_menu(user_pin)

if __name__ == "__main__":
    main()
