import threading

class Bank:
    def __init__(self):
        self.accounts = {}
        self.requests = Queue()

    def process_request(self, request):
        # get the request details
        account, action, amount, new_balance = request

        # process the request
        if action == "withdraw":
            # withdraw money from the specified account
            current_balance = self.accounts[account]
            new_balance = current_balance - amount
            self.accounts[account] = new_balance

        elif action == "deposit":
            # deposit money into the specified account
            current_balance = self.accounts[account]
            new_balance = current_balance + amount
            self.accounts[account] = new_balance

    def process_requests(self):
        # process requests from the queue in parallel
        while not self.requests.empty():
            # get the next request from the queue
            request = self.requests.get()

            # create a new thread to process the request
            thread = threading.Thread(target=self.process_request, args=(request,))

            # start the thread
            thread.start()

    def withdraw(self, account, amount):
        # withdraw money from the specified account
        current_balance = self.accounts[account]
        new_balance = current_balance - amount
        self.accounts[account] = new_balance

        # add request to the queue
        self.requests.put((account, "withdraw", amount, new_balance))

    def deposit(self, account, amount):
        # deposit money into the specified account
        current_balance = self.accounts[account]
        new_balance = current_balance + amount
        self.accounts[account] = new_balance

        # add request to the queue
        self.requests.put((account, "deposit", amount, new_balance))

class BankAccount:
    def __init__(self, name, phone, password, initial_balance):
        self.name = name
        self.phone = phone
        self.initial_balance = initial_balance
        self.password = password

    def check_password(self, password):
        # compare the provided password with the stored password
        return password == self.password

    def withdraw(self, amount):
        # withdraw money from the account
        self.initial_balance -= amount

    def deposit(self, amount):
        # deposit money into the account
        self.initial_balance += amount


