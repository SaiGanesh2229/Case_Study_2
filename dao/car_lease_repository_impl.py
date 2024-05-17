import pyodbc
from entity.vehicle import Vehicle
from entity.customer import Customer
from entity.lease import Lease
from entity.payment import Payment
from exceptions.car_not_found import CarNotFoundException
from exceptions.lease_not_found import LeaseNotFoundException
from exceptions.customer_not_found import CustomerNotFoundException
from util.db_conn_util import DBConnUtil


class CarLeaseRepositoryImpl:

    def __init__(self):
        self.connection = DBConnUtil.get_connection()

    # Car Management
    def add_car(self, car):
        cursor = self.connection.cursor()
        query = """
        INSERT INTO Vehicle (make, model, year, dailyRate, status, passengerCapacity, engineCapacity)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        cursor.execute(
            query,
            car.make,
            car.model,
            car.year,
            car.daily_rate,
            car.status,
            car.passenger_capacity,
            car.engine_capacity,
        )
        self.connection.commit()

    def update_car_status(self, car_id, new_status):
        cursor = self.connection.cursor()
        query = "UPDATE Vehicle SET status = ? WHERE vehicleID = ?"
        cursor.execute(query, new_status, car_id)
        if cursor.rowcount == 0:
            raise CarNotFoundException(f"Car with ID {car_id} not found")
        self.connection.commit()

    def find_car_by_id(self, car_id):
        cursor = self.connection.cursor()
        query = "SELECT * FROM Vehicle WHERE vehicleID = ?"
        cursor.execute(query, car_id)
        car = cursor.fetchone()
        if car is None:
            raise CarNotFoundException(f"Car with ID {car_id} not found")
        return Vehicle(*car)

    def list_available_cars(self):
        cursor = self.connection.cursor()
        query = "SELECT * FROM Vehicle WHERE status = 'available'"
        cursor.execute(query)
        cars = cursor.fetchall()
        return [Vehicle(*car) for car in cars]

    def list_rented_cars(self):
        cursor = self.connection.cursor()
        query = "SELECT * FROM Vehicle WHERE status = 'notAvailable'"
        cursor.execute(query)
        cars = cursor.fetchall()
        return [Vehicle(*car) for car in cars]

    # Customer Management
    def add_customer(self, customer):
        cursor = self.connection.cursor()
        query = """
        INSERT INTO Customer (firstName, lastName, email, phoneNumber)
        VALUES (?, ?, ?, ?)
        """
        cursor.execute(
            query,
            customer.first_name,
            customer.last_name,
            customer.email,
            customer.phone_number,
        )
        self.connection.commit()

    def update_customer(self, customer_id, first_name, last_name, email, phone_number):
        cursor = self.connection.cursor()
        query = """
        UPDATE Customer SET firstName = ?, lastName = ?, email = ?, phoneNumber = ? WHERE customerID = ?
        """
        cursor.execute(query, first_name, last_name, email, phone_number, customer_id)
        if cursor.rowcount == 0:
            raise CustomerNotFoundException(f"Customer with ID {customer_id} not found")
        self.connection.commit()

    def find_customer_by_id(self, customer_id):
        cursor = self.connection.cursor()
        query = "SELECT * FROM Customer WHERE customerID = ?"
        cursor.execute(query, customer_id)
        customer = cursor.fetchone()
        if customer is None:
            raise CustomerNotFoundException(f"Customer with ID {customer_id} not found")
        return Customer(*customer)

    def list_customers(self):
        cursor = self.connection.cursor()
        query = "SELECT * FROM Customer"
        cursor.execute(query)
        customers = cursor.fetchall()
        return [Customer(*customer) for customer in customers]

    # Lease Management
    def create_lease(self, customer_id, car_id, start_date, end_date, lease_type):
        cursor = self.connection.cursor()
        query = """
        INSERT INTO Lease (customerID, vehicleID, startDate, endDate, leaseType)
        VALUES (?, ?, ?, ?, ?)
        """
        cursor.execute(query, customer_id, car_id, start_date, end_date, lease_type)
        self.connection.commit()

    def return_car(self, lease_id):
        cursor = self.connection.cursor()
        query = "UPDATE Lease SET returnDate = GETDATE() WHERE leaseID = ?"
        cursor.execute(query, lease_id)
        if cursor.rowcount == 0:
            raise LeaseNotFoundException(f"Lease with ID {lease_id} not found")
        self.connection.commit()

    def list_active_leases(self):
        cursor = self.connection.cursor()
        query = "SELECT * FROM Lease WHERE returnDate IS NULL"
        cursor.execute(query)
        leases = cursor.fetchall()
        return [Lease(*lease) for lease in leases]

    def list_lease_history(self):
        cursor = self.connection.cursor()
        query = "SELECT * FROM Lease WHERE returnDate IS NOT NULL"
        cursor.execute(query)
        leases = cursor.fetchall()
        return [Lease(*lease) for lease in leases]

    # Payment Handling
    def record_payment(self, lease_id, amount):
        cursor = self.connection.cursor()
        query = """
        INSERT INTO Payment (leaseID, amount, paymentDate)
        VALUES (?, ?, GETDATE())
        """
        cursor.execute(query, lease_id, amount)
        if cursor.rowcount == 0:
            raise LeaseNotFoundException(f"Lease with ID {lease_id} not found")
        self.connection.commit()

    def retrieve_payment_history(self, customer_id):
        cursor = self.connection.cursor()
        query = """
        SELECT * FROM Payment WHERE leaseID IN (SELECT leaseID FROM Lease WHERE customerID = ?)
        """
        cursor.execute(query, customer_id)
        payments = cursor.fetchall()
        return [Payment(*payment) for payment in payments]

    def calculate_total_revenue(self):
        cursor = self.connection.cursor()
        query = "SELECT SUM(amount) FROM Payment"
        cursor.execute(query)
        total_revenue = cursor.fetchone()[0]
        return total_revenue
