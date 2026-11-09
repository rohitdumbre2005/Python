class Customer:

    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def display_customer(self):
        print("Customer ID:", self.customer_id)
        print("Name:", self.name)
        print("Email:", self.email)