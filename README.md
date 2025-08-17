BankLite – Console Banking System

Overview
BankLite is a simple console-based banking system implemented in Python. It allows users to create accounts, deposit and withdraw funds, check balances, view transaction history, and save/load data to/from a JSON file. The system uses object-oriented programming principles for clear structure and extensibility.

Features
- Create new bank accounts
- Deposit and withdraw money
- View account balance
- View transaction history
- Save and load all data to/from `bank.json`
- Input and balance validation for safe transactions

How to Run
1. Make sure you have Python 3 installed.
2. Open a terminal or command prompt.
3. Navigate to the `python` directory:
   ```
   cd python
   ```
4. Run the main program:
   ```
   python main.py
   ```

File Structure
- `account.py`: Contains the `Account` class.
- `bank.py`: Contains the `Bank` class and handles all account management.
- `main.py`: Console interface for user interaction.
- `bank.json`: Data file for saving/loading accounts and transactions.

Note:
- All data is stored in `bank.json` in the same folder.
- Transaction logs are readable and stored as strings in each account.
- The system is designed for easy extension (e.g., adding new account types). 
