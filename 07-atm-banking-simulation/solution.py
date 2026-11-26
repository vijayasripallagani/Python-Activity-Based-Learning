"""
Case Study 7: ATM Menu-Driven Banking Simulation
Loops, conditionals, tuples and a transaction list.
"""

MIN_BALANCE = 1000.0
MAX_DEPOSIT = 100000.0
MAX_WITHDRAWAL = 10000.0

# Log entries are tuples: (transaction type, amount, balance after it)


def deposit(balance, amount, log):
    if amount <= 0 or amount > MAX_DEPOSIT:
        return balance, "Deposit must be between 0 and 100000."
    balance = balance + amount
    log.append(("DEPOSIT", amount, balance))
    return balance, "Deposited Rs %.2f" % amount


def withdraw(balance, amount, log):
    if amount <= 0 or amount > MAX_WITHDRAWAL:
        return balance, "Withdrawal must be between 0 and 10000."
    if amount % 100 != 0:
        return balance, "Withdrawal must be a multiple of 100."
    if balance - amount < MIN_BALANCE:
        return balance, "Minimum balance of Rs 1000 must be kept."
    balance = balance - amount
    log.append(("WITHDRAW", amount, balance))
    return balance, "Withdrew Rs %.2f" % amount


def read_amount(prompt):
    value = input(prompt)
    try:
        amount = float(value)
    except ValueError:
        return -1.0
    return amount


def main():
    balance = 5000.0
    log = []
    while True:
        print("\n1. Deposit   2. Withdraw   3. Balance   4. Statement   5. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            balance, message = deposit(balance, read_amount("Amount: "), log)
            print(message)
        elif choice == "2":
            balance, message = withdraw(balance, read_amount("Amount: "), log)
            print(message)
        elif choice == "3":
            print("Current balance: Rs %.2f" % balance)
        elif choice == "4":
            print("---- MINI STATEMENT ----")
            for kind, amount, after in log:
                print("%-8s Rs %9.2f   balance Rs %9.2f" % (kind, amount, after))
        elif choice == "5":
            break
        else:
            print("Please choose 1 to 5.")
    print("Session end: %d transaction(s), closing balance Rs %.2f" %
          (len(log), balance))


if __name__ == "__main__":
    main()
