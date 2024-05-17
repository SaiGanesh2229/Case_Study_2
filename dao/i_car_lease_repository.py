from abc import ABC, abstractmethod
from typing import List
from entity.vehicle import Vehicle
from entity.customer import Customer
from entity.lease import Lease


class ICarLeaseRepository(ABC):

    # Car Management
    @abstractmethod
    def add_car(self, car: Vehicle) -> None:
        pass

    @abstractmethod
    def remove_car(self, car_id: int) -> None:
        pass

    @abstractmethod
    def list_available_cars(self) -> List[Vehicle]:
        pass

    @abstractmethod
    def list_rented_cars(self) -> List[Vehicle]:
        pass

    @abstractmethod
    def find_car_by_id(self, car_id: int) -> Vehicle:
        pass

    # Customer Management
    @abstractmethod
    def add_customer(self, customer: Customer) -> None:
        pass

    @abstractmethod
    def remove_customer(self, customer_id: int) -> None:
        pass

    @abstractmethod
    def list_customers(self) -> List[Customer]:
        pass

    @abstractmethod
    def find_customer_by_id(self, customer_id: int) -> Customer:
        pass

    # Lease Management
    @abstractmethod
    def create_lease(
        self, customer_id: int, car_id: int, start_date: str, end_date: str
    ) -> Lease:
        pass

    @abstractmethod
    def return_car(self, lease_id: int) -> Lease:
        pass

    @abstractmethod
    def list_active_leases(self) -> List[Lease]:
        pass

    @abstractmethod
    def list_lease_history(self) -> List[Lease]:
        pass

    # Payment Handling
    @abstractmethod
    def record_payment(self, lease: Lease, amount: float) -> None:
        pass
