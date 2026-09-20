```mermaid
classDiagram

    class RentalSystem {
        -List~Vehicle~ vehicles
        -List~Customer~ customers
        -List~Rental~ rentals

        +add_vehicle()
        +display_vehicles()
        +search_vehicle()
        +register_customer()
        +display_customers()
        +rent_vehicle()
        +return_vehicle()
        +display_active_rentals()
        +save_data()
        +load_data()
        +get_vehicle_by_id(v_id)
        +get_customer_by_id(c_id)
    }

    class Vehicle {
        +str vehicle_id
        +str registration
        +str make
        +str model
        +float daily_rate
        +bool is_available

        +rent_a_vehicle()
        +return_a_vehicle()
        +search_for_vehicle(term)
        +display_details()
        +to_dictionary()
    }

    class Customer {
        +str customer_id
        +str customer_name
        +str phone_number
        +str email
        +str driver_license

        +display_details()
        +to_dictionary()
    }

    class Rental {
        +str rental_id
        +str vehicle_id
        +str customer_id
        +int days
        +float total_cost
        +bool is_active

        +calculate_cost(daily_rate)
        +display_details()
        +to_dictionary()
    }

    RentalSystem "1" *-- "many" Vehicle : manages
    RentalSystem "1" *-- "many" Customer : manages
    RentalSystem "1" *-- "many" Rental : manages

    Rental "many" --> "1" Vehicle : uses
    Rental "many" --> "1" Customer : connects
```

## How the classes work together

**RentalSystem** is the main part of the program. It manages the vehicles, customers, and rental records. It also has helper methods that allow the system to find a specific vehicle or customer using their ID.

**Vehicle** represents a single vehicle in the system. It stores information such as the vehicle ID, registration number, make, model, daily rental price, and whether the vehicle is available.

**Customer** represents a person who rents a vehicle. It stores the customer's ID, name, phone number, email, and driver's license information.

**Rental** represents a rental transaction. It connects a customer with a vehicle and records details such as the number of rental days, total cost, and whether the rental is still active.

In simple terms, **RentalSystem manages everything, Vehicle stores vehicle information, Customer stores customer information, and Rental connects a customer to a vehicle when a rental takes place.**

