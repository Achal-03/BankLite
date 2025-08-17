from bank import Bank

def main():
    bank = Bank()
    bank.load_from_file()
    while True:
        print("\n--- BankLite Console ---")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. View Balance")
        print("5. View Transaction History")
        print("6. Save Data")
        print("7. Load Data")
        print("8. Exit")
        choice = input("Select an option: ")
        if choice == '1':
            name = input("Enter account holder name: ")
            try:
                start_balance = float(input("Enter starting balance: "))
                if start_balance < 0:
                    print("Starting balance cannot be negative.")
                    continue
            except ValueError:
                print("Invalid amount.")
                continue
            acc = bank.create_account(name, start_balance)
            print(f"Account created! ID: {acc.id}, Name: {acc.name}, Balance: {acc.balance}")
        elif choice == '2':
            try:
                acc_id = int(input("Enter account ID: "))
                amount = float(input("Enter deposit amount: "))
                bank.deposit_to_account(acc_id, amount)
                print("Deposit successful.")
            except Exception as e:
                print(f"Error: {e}")
        elif choice == '3':
            try:
                acc_id = int(input("Enter account ID: "))
                amount = float(input("Enter withdrawal amount: "))
                bank.withdraw_from_account(acc_id, amount)
                print("Withdrawal successful.")
            except Exception as e:
                print(f"Error: {e}")
        elif choice == '4':
            try:
                acc_id = int(input("Enter account ID: "))
                details = bank.show_account_details(acc_id)
                print(f"Account ID: {details['id']}")
                print(f"Name: {details['name']}")
                print(f"Balance: {details['balance']}")
            except Exception as e:
                print(f"Error: {e}")
        elif choice == '5':
            try:
                acc_id = int(input("Enter account ID: "))
                details = bank.show_account_details(acc_id)
                print("Transaction History:")
                for t in details['transactions']:
                    print(f"- {t}")
            except Exception as e:
                print(f"Error: {e}")
        elif choice == '6':
            bank.save_to_file()
            print("Data saved to bank.json.")
        elif choice == '7':
            bank.load_from_file()
            print("Data loaded from bank.json.")
        elif choice == '8':
            bank.save_to_file()
            print("Exiting. Data saved.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main() 