from flask import Flask, request
from bank import Bank, BankAccount
# create a Flask app
app = Flask(__name__)

# create a Bank instance
bank = Bank()

@app.route("/register", methods=["POST"])
def register():
    # get the user data from the request
    data = request.get_json()
    name = data["name"]
    phone = data["phone"]
    password = data["password"]
    initial_balance = data["initial_balance"]

    # create a BankAccount for the user
    account = BankAccount(name, phone, password, initial_balance)

    # add the BankAccount to the bank
    bank.add_account(account)

    return "Account created successfully!"

@app.route("/login", methods=["POST"])
def login():
    # get the user data from the request
    data = request.get_json()
    phone = data["phone"]
    password = data["password"]

    # get the BankAccount for the user
    account = bank.get_account(phone)

    # check the password
    if account.check_password(password):
        return "Login successful!"
    else:
        return "Invalid password!"

@app.route("/withdraw", methods=["POST"])
def withdraw():
    # get the user data from the request
    data = request.get_json()
    phone = data["phone"]
    amount = data["amount"]

    # get the BankAccount for the user
    account = bank.get_account(phone)

    # withdraw money from the account
    account.withdraw(amount)

    # add the request to the queue
    bank.requests.put((account, "withdraw", amount, account.initial_balance))

    return "Withdrawal successful!"

@app.route("/deposit", methods=["POST"])
def deposit():
    # get the user data from the request
    data = request.get_json()
    phone = data["phone"]
    amount = data["amount"]

    # get the BankAccount for the user
    account = bank.get_account(phone)

    # deposit money into the account
    account.deposit(amount)

    # add the request to the queue
    bank.requests.put((account, "deposit", amount, account.initial_balance))

    return "Deposit successful!"

if __name__ == "__main__":
    # start processing the requests in the queue
    bank.process_requests()

    # run the Flask app
    app.run()
