class Payment:
    def __init__(self, lease_id, amount, payment_date, payment_id=None):
        self.payment_id = payment_id
        self.lease_id = lease_id
        self.amount = amount
        self.payment_date = payment_date

    def __repr__(self):
        return f"Payment({self.payment_id}, {self.lease_id}, {self.amount}, {self.payment_date})"
