import sys
from bank_account import BankAccount

def main():

    account = BankAccount()

    if len(sys.argv) < 2:
        print("Usage: python3 main-o.py <command> [amount]")
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "deposit":
        if len(sys.argv) != 3:
            print("Error: deposit requires an amount")
            sys.exit(1)
        amount = float(sys.argv[2])
        if account.deposit(amount):
            print(f"Deposited: ${amount}")
        else:
            print ("Invalid deposit amount")

    elif command == "withdraw":
        if len(sys.argv) != 3:
            print("Error: withdraw requires an amount")
            sys.exit(1)
        amount = float(sys.argv[2])
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds or invalid amount")

    elif command == "balance":
        account.display_balance()

    else:
        print("Invalid command.")


if __name__ == "__main__":
    main()