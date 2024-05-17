from dao.car_lease_repository_impl import CarLeaseRepositoryImpl
from entity.vehicle import Vehicle
from entity.customer import Customer
from entity.lease import Lease
from entity.payment import Payment
from exceptions.car_not_found import CarNotFoundException
from exceptions.lease_not_found import LeaseNotFoundException
from exceptions.customer_not_found import CustomerNotFoundException


def main():
    repository = CarLeaseRepositoryImpl()

    while True:
        print("\nMenu:")
        print("1. Add Car")
        print("2. Update Car Availability")
        print("3. Retrieve Car Information")
        print("4. Add Customer")
        print("5. Update Customer Information")
        print("6. Retrieve Customer Details")
        print("7. Create Lease")
        print("8. Return Car")
        print("9. List Active Leases")
        print("10. List Lease History")
        print("11. Record Payment")
        print("12. Retrieve Payment History")
        print("13. Calculate Total Revenue")
        print("14. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            make = input("Enter Car Make: ")
            model = input("Enter Car Model: ")
            year = int(input("Enter Car Year: "))
            daily_rate = float(input("Enter Daily Rate: "))
            status = input("Enter Car Availability (available/notAvailable): ")
            passenger_capacity = int(input("Enter Passenger Capacity: "))
            engine_capacity = float(input("Enter Engine Capacity: "))
            if status.lower() not in ["available", "notavailable"]:
                print(
                    "Invalid status value! Please enter 'available' or 'notAvailable'."
                )
                continue
            car = Vehicle(
                make=make,
                model=model,
                year=year,
                daily_rate=daily_rate,
                status=status,
                passenger_capacity=passenger_capacity,
                engine_capacity=engine_capacity,
            )
            try:
                repository.add_car(car)
                print("Car added successfully!")
            except Exception as e:
                print(f"Error adding Car: {e}")

        elif choice == "2":
            car_id = int(input("Enter Car ID: "))
            new_status = input("Enter New Car Availability (available/notAvailable): ")
            try:
                repository.update_car_status(car_id, new_status)
                print("Car availability updated successfully!")
            except CarNotFoundException:
                print("Error: Car not found")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "3":
            car_id = int(input("Enter Car ID: "))
            try:
                car = repository.find_car_by_id(car_id)
                print(f"Car Details: {car}")
            except CarNotFoundException:
                print("Error: Car not found")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "4":
            first_name = input("Enter Customer First Name: ")
            last_name = input("Enter Customer Last Name: ")
            email = input("Enter Customer Email: ")
            phone_number = input("Enter Customer Phone Number: ")
            customer = Customer(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number,
            )
            try:
                repository.add_customer(customer)
                print("Customer added successfully!")
            except Exception as e:
                print(f"Error adding Customer: {e}")

        elif choice == "5":
            customer_id = int(input("Enter Customer ID: "))
            first_name = input("Enter Customer First Name: ")
            last_name = input("Enter Customer Last Name: ")
            email = input("Enter Customer Email: ")
            phone_number = input("Enter Customer Phone Number: ")
            try:
                repository.update_customer(
                    customer_id, first_name, last_name, email, phone_number
                )
                print("Customer information updated successfully!")
            except CustomerNotFoundException:
                print("Error: Customer not found")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "6":
            customer_id = int(input("Enter Customer ID: "))
            try:
                customer = repository.find_customer_by_id(customer_id)
                print(f"Customer Details: {customer}")
            except CustomerNotFoundException:
                print("Error: Customer not found")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "7":
            customer_id = int(input("Enter Customer ID: "))
            car_id = int(input("Enter Car ID: "))
            start_date = input("Enter Start Date (YYYY-MM-DD): ")
            end_date = input("Enter End Date (YYYY-MM-DD): ")
            lease_type = input("Enter Lease Type (Daily/Monthly): ")
            try:
                lease = repository.create_lease(
                    customer_id, car_id, start_date, end_date, lease_type
                )
                print(f"Lease created successfully: {lease}")
            except CarNotFoundException:
                print("Error: Car not found")
            except CustomerNotFoundException:
                print("Error: Customer not found")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "8":
            lease_id = int(input("Enter Lease ID: "))
            try:
                lease_info = repository.return_car(lease_id)
                print(f"Car returned successfully: {lease_info}")
            except LeaseNotFoundException:
                print("Error: Lease not found")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "9":
            try:
                active_leases = repository.list_active_leases()
                print("Active Leases:")
                for lease in active_leases:
                    print(lease)
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "10":
            try:
                lease_history = repository.list_lease_history()
                print("Lease History:")
                for lease in lease_history:
                    print(lease)
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "11":
            lease_id = int(input("Enter Lease ID: "))
            amount = float(input("Enter Payment Amount: "))
            try:
                repository.record_payment(lease_id, amount)
                print("Payment recorded successfully!")
            except LeaseNotFoundException:
                print("Error: Lease not found")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "12":
            customer_id = int(input("Enter Customer ID: "))
            try:
                payments = repository.retrieve_payment_history(customer_id)
                print("Payment History:")
                for payment in payments:
                    print(payment)
            except CustomerNotFoundException:
                print("Error: Customer not found")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "13":
            try:
                total_revenue = repository.calculate_total_revenue()
                print(f"Total Revenue: {total_revenue}")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "14":
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
