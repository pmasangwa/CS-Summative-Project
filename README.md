# Vehicle Rental Management System

## Team Members

1. Kibet Mary
2. Philimon Masangwa
3. Saraphina Baranabas
4. Angela Loshoki


## Project Description

The system is designed to help a vehicle rental company manage vehicles, customers, and rentals. Users can add and view vehicles, register customers, rent vehicles, return vehicles, calculate rental costs, and view active rentals.

The application demonstrates Object-Oriented Programming, functions, conditional statements, loops, file handling, exception handling, input validation, systematic testing, and GitHub version control.

## Main Features

The application provides the following functionality:

- Add a vehicle
- Display all vehicles
- Search for a vehicle using its ID or registration number
- Register a customer
- Display registered customers
- Rent a vehicle to a customer
- Return a rented vehicle
- Prevent an unavailable vehicle from being rented
- Calculate the rental cost
- Display active rentals
- Save vehicle information to a file
- Save customer information to a file
- Save rental information to a file
- Load previously saved information when the application starts
- Validate user input
- Handle common input and file-related errors


## Classes

The application uses three main classes:

### 1. Vehicle

The `Vehicle` class represents a vehicle available for rental.

It stores information about each vehicle, including its identification and availability.

The class contains methods for managing and displaying vehicle information.

### 2. Customer

The `Customer` class represents a customer registered with the rental company.

It stores customer information and provides methods for managing customer records.

### 3. Rental

The `Rental` class represents a rental transaction between a customer and a vehicle.

It stores information such as:

- Rental ID
- Vehicle ID
- Customer ID
- Number of rental days
- Total rental cost
- Rental status

The class provides methods for:

- Calculating rental cost
- Displaying rental details
- Converting rental information into dictionary format
- Tracking whether a rental is active

## Project Structure

### main.py

Contains the main program and menu system.

It coordinates the different classes and manages interactions between vehicles, customers, and rentals.

### vehicle.py

Contains the Vehicle class and vehicle-related functionality.

### customer.py

Contains the Customer class and customer-related functionality.

### rental.py

Contains the Rental class and rental-related functionality.

### JSON Files

The application uses JSON files to store information so that data can be loaded again when the program is restarted.

- vehicles.json - stores vehicle information
- customers.json - stores customer information
- rentals.json - stores rental information

## Object-Oriented Programming

The application uses Object-Oriented Programming to separate the responsibilities of the system.

The main classes are:

- Vehicle - manages vehicle information
- Customer - manages customer information
- Rental - manages rental information and connects a vehicle with a customer

Each class contains its own attributes and methods rather than placing the entire application inside one large function or class.
## File Handling

The application uses JSON files for persistent data storage.

The system can:

1. Read existing vehicle data
2. Read existing customer data
3. Read existing rental data
4. Add new records
5. Update records
6. Write updated information back to the files
7. Load saved information when the program starts

This allows information to remain available after the application is closed and restarted.

## Input Validation

The application validates user input to prevent invalid information from being stored.

Examples of validation include:

- Checking that required information is entered
- Validating numerical input
- Preventing invalid IDs
- Preventing an unavailable vehicle from being rented
- Preventing invalid rental information
- Handling invalid menu selections

When invalid information is entered, the application provides an appropriate message to the user.

## Exception Handling

The application uses Python exception handling to prevent unnecessary crashes.

Exception handling is used for situations such as:

- Entering letters when a number is required
- Invalid numerical input
- Missing files
- Invalid menu selections
- Other invalid user input

Specific exceptions are handled where appropriate.

## How to Run the Application
Requirements
1. Python 3.x
2. Git, if cloning the repository

No external Python libraries are required.

#### Clone the Repository

`git clone https://github.com/pmasangwa/CS-Summative-Project.git`
#### Open the Project
`cd CS-Summative-Project`

#### Run the Application
`python main.py`

### The Application Workflow

A typical rental process is:

1. Start the application
2. View or add vehicles
3. Register a customer
4. Select an available vehicle
5. Create a rental
6. Calculate the rental cost
7. Vehicle becomes unavailable
8. Return the vehicle
9. Rental becomes inactive
10. Vehicle becomes available again and can be rented out

The system prevents a vehicle that is already unavailable from being rented.

### GitHub Version Control

Git and GitHub are used to manage the development of the project.

The repository contains:

- Python source files
- JSON data files
- Project documentation
- Test documentation
- README file

### Team contributions
#### Mary:
-Vehicle class functionality
#### Philimon:
-Rental class implementation
#### Sarah:
-Customer class functionality
#### Angela:
-Main py implementation

### Technologies Used
- Python
- Object-Oriented Programming (OOP)
- JSON
- Git
- GitHub
