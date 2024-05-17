import unittest
import sys

sys.path.append(
    "C:/Users/sai ganesh/OneDrive/Desktop/Hexaware_Training_Project/Case_study"
)

from dao.car_lease_repository_impl import CarLeaseRepositoryImpl
from entity.vehicle import Vehicle
from entity.lease import Lease
from exceptions.car_not_found import CarNotFoundException
from exceptions.lease_not_found import LeaseNotFoundException
from exceptions.customer_not_found import CustomerNotFoundException


class TestCarLeaseRepository(unittest.TestCase):

    def setUp(self):
        # Create an instance of CarLeaseRepositoryImpl for testing
        self.repository = CarLeaseRepositoryImpl()

    def test_add_car(self):
        # Test if car is added successfully
        car = Vehicle(
            vehicle_id=1,
            make="Toyota",
            model="Camry",
            year=2022,
            daily_rate=50,
            status="available",
            passenger_capacity=5,
            engine_capacity=2000,
        )
        self.repository.add_car(car)
        added_car = self.repository.find_car_by_id(1)
        self.assertEqual(added_car.make, "Toyota")
        # You can add more assertions here

    def test_create_lease(self):
        # Test if lease is created successfully
        lease = self.repository.create_lease(
            customer_id=1, car_id=1, start_date="2024-05-01", end_date="2024-05-10"
        )
        self.assertIsInstance(lease, Lease)
        # You can add more assertions here

    def test_get_lease(self):
        # Test if lease is retrieved successfully
        lease_id = 1  # Assume lease ID exists in the database
        lease = self.repository.return_car(lease_id)
        self.assertIsInstance(lease, Lease)
        # You can add more assertions here

    def test_car_not_found_exception(self):
        # Test if CarNotFoundException is raised when car ID is not found
        with self.assertRaises(CarNotFoundException):
            self.repository.find_car_by_id(
                9999
            )  # Assuming car ID does not exist in the database

    def test_lease_not_found_exception(self):
        # Test if LeaseNotFoundException is raised when lease ID is not found
        with self.assertRaises(LeaseNotFoundException):
            self.repository.return_car(
                9999
            )  # Assuming lease ID does not exist in the database

    def test_customer_not_found_exception(self):
        # Test if CustomerNotFoundException is raised when customer ID is not found
        with self.assertRaises(CustomerNotFoundException):
            self.repository.find_customer_by_id(
                9999
            )  # Assuming customer ID does not exist in the database


if __name__ == "__main__":
    unittest.main()
