
class BankError(Exception):
    pass

class AccountNotExistsError(BankError):
    pass

class NotEnoughMoneyError(BankError):
    pass

class NegativeAmountError(BankError):
    pass


class Customer:
    last_id = 0

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        Customer.last_id += 1
        self.id = Customer.last_id

    def __repr__(self):
        return 'Customer[{},{},{},{}]'.format(self.id, self.first_name, self.last_name, self.email)


class Account:
    last_id = 0

    def __init__(self, customer):
        Account.last_id += 1
        self.id = Account.last_id
        self.customer = customer
        self._balance = 0

    def deposit(self, amount):
        # TODO - add validation to prevent misuse
        if amount < 0:
            raise NegativeAmountError('{0} amount provided to deposit: {1}'.format(self.id, amount))
        self._balance += amount

    def charge(self, amount):
        #TODO - add validation to prevent misuse
        if amount < 0:
            raise NegativeAmountError('{0} amount provided to deposit: {1}'.format(self.id, amount))
        if amount > self._balance:
            raise NotEnoughMoneyError('{0} amount provided to deposit: {1}'.format(self.id, amount))
        self._balance -= amount
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print('New deposit updated as: ' + str(self._balance))
        else:
            raise NegativeAmountError('The amount is negative')

    def charge(self, amount):
        if amount > self._balance:
            raise NotEnoughMoneyError(
                "You don't have enough Balance. Your Current Balance is " + str(self._balance)
                , self._balance)
        if amount <= 0:
            raise NegativeAmountError("The amount is negative. Please input the positive amount")
        else:
            self._balance -= amount
            print("Charge amount is: " + str(amount))
            print("New Balance updated as: " + str(self._balance))

    def __repr__(self):
        return '{}[{},{},{}]'.format(self.__class__.__name__, self.id, self.customer.last_name, self._balance)


class SavingsAccount(Account):
    interest_rate = 0.02

    def calc_interest(self):
        self._balance += self.interest_rate * self._balance


class CheckingAccount(Account):
    pass


class Bank:
    def __init__(self):
        self.cust_list = []
        self.acc_list = []

    def new_customer(self, first_name, last_name, email):
        #TODO - create a new customer, add it to a list of customers
        c = Customer(first_name, last_name, email)
        self.cust_list.append(c)
        return c

    def new_account(self, customer, is_savings=True):
        #TODO - create a new account and add it to the list of accounts
        # if is_savings:
        #     a = SavingsAccount(customer)
        # else:
        #     a = CheckingAccount(customer)
        a = SavingsAccount(customer) if is_savings else CheckingAccount(customer)
        self.acc_list.append(a)
        return a

    def transfer(self, from_account_id, to_account_id, amount):
        from_acc = self.acc_list[from_account_id-1]
        to_acc = self.acc_list[to_account_id-1]
        from_acc.charge(amount)
        to_acc.deposit(amount)

    def __repr__(self):
        return 'Bank\n{}\n{}'.format(self.cust_list, self.acc_list)

b = Bank()

c1 = b.new_customer('John', 'Brown', 'john@brown.com')
c2 = b.new_customer('Anna', 'Smith', 'anne@smith.com')

a1 = b.new_account(c1, is_savings=True)
a2 = b.new_account(c1, is_savings=False)
try:
    a1.deposit(100)
    a2.deposit(50)

    print(b)
    b.transfer(a1.id, a2.id, 100)
except BankError as be:
    print('Got error: {}'.format(be))
print(b)