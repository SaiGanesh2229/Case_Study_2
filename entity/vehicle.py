class Vehicle:
    def __init__(
        self,
        make,
        model,
        year,
        daily_rate,
        status,
        passenger_capacity,
        engine_capacity,
        vehicle_id=None,
    ):
        self.vehicle_id = vehicle_id
        self.make = make
        self.model = model
        self.year = year
        self.daily_rate = daily_rate
        self.status = status
        self.passenger_capacity = passenger_capacity
        self.engine_capacity = engine_capacity

    def __repr__(self):
        return f"Vehicle({self.vehicle_id}, {self.make}, {self.model}, {self.year}, {self.daily_rate}, {self.status}, {self.passenger_capacity}, {self.engine_capacity})"
