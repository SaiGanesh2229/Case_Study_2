class Customer:
    def __init__(self, first_name, last_name, email, phone_number, customer_id=None):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number

    def __repr__(self):
        return f"Customer({self.customer_id}, {self.first_name}, {self.last_name}, {self.email}, {self.phone_number})"
