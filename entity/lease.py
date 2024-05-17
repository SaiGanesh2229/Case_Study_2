class Lease:
    def __init__(
        self,
        customer_id,
        vehicle_id,
        start_date,
        end_date,
        lease_type,
        lease_id=None,
        return_date=None,
    ):
        self.lease_id = lease_id
        self.customer_id = customer_id
        self.vehicle_id = vehicle_id
        self.start_date = start_date
        self.end_date = end_date
        self.lease_type = lease_type
        self.return_date = return_date

    def __repr__(self):
        return f"Lease({self.lease_id}, {self.customer_id}, {self.vehicle_id}, {self.start_date}, {self.end_date}, {self.lease_type}, {self.return_date})"
