
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

    def __repr__(self):
        return '{}[{},{},{}]'.format(self.__class__.__name__, self.id, self.customer.last_name, self._balance)


class SavingsAccount(Account):
    interest_rate = 0.02

    def calc_interest(self):
        self._balance += self.interest_rate * self._balance


class CheckingAccount(Account):
    pass


class Bank:
    cust_list = []
    acc_list = []
    def new_customer(self, first_name, last_name, email):
        #TODO - create a new customer, add it to a list of customers

    def new_account(self, customer, is_savings=True):
        #TODO - create a new account and add it to the list of accounts


b = Bank()

c1 = Customer('John', 'Brown', 'john@brown.com')
c2 = Customer('Anna', 'Smith', 'anne@smith.com')

a1 = CheckingAccount(c1)
a2 = SavingsAccount(c1)

print(c1)
print(c2)
print(a1)
print(a2)