from bank_model import Bank, Customer, Account, init_db, DBSession

db = DBSession().db_session()


def add_data():
    init_db()
    b = Bank('My First Bank')

    db.add(b)
    db.commit()
    c1 = b.new_customer('John', 'Brown', 'john@brown.com')
    c2 = b.new_customer('Anna', 'Smith', 'anne@smith.com')
    db.add(c1)
    db.add(c2)
    #
    a1 = b.new_account(c1, is_savings=True)
    a2 = b.new_account(c1, is_savings=False)
    #
    db.add(a1)
    db.add(a2)
    db.commit()

    print(b)


def get_customers():
    customers = db.query(Customer).filter(Customer.last_name=='Brown').all()
    for c in customers:
        print(c)
        print('Got accounts: {}'.format(c.accounts))


if __name__ == '__main__':
    #add_data()

    get_customers()