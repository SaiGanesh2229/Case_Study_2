create database CarRentalSystem;
use CarRentalSystem;
CREATE TABLE Vehicle (
    vehicleID INTEGER PRIMARY KEY,
    make TEXT NOT NULL,
    model TEXT NOT NULL,
    year INTEGER NOT NULL,
    dailyRate REAL NOT NULL,
    status varchar NOT NULL CHECK (status IN ('available', 'notAvailable')),
    passengerCapacity INTEGER NOT NULL,
    engineCapacity REAL NOT NULL
);

CREATE TABLE Customer (
    customerID INTEGER PRIMARY KEY IDENTITY(1,1),
    firstName VARCHAR(50) NOT NULL,
    lastName VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phoneNumber VARCHAR(20) NOT NULL
);


CREATE TABLE Lease (
    leaseID INTEGER PRIMARY KEY,
    vehicleID INTEGER NOT NULL,
    customerID INTEGER NOT NULL,
    startDate TEXT NOT NULL,
    endDate TEXT NOT NULL,
    type varchar NOT NULL CHECK (type IN ('DailyLease', 'MonthlyLease')),
    FOREIGN KEY (vehicleID) REFERENCES Vehicle(vehicleID),
    FOREIGN KEY (customerID) REFERENCES Customer(customerID)
);

CREATE TABLE Payment (
    paymentID INTEGER PRIMARY KEY,
    leaseID INTEGER NOT NULL,
    paymentDate TEXT NOT NULL,
    amount REAL NOT NULL,
    FOREIGN KEY (leaseID) REFERENCES Lease(leaseID)
);

select * from Customer;
select * from Vehicle;