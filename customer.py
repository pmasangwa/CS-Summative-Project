# The Customer class represents a customer in the vehicle management system. Each customer object has its own personal details that will store information about the customer. 
# The customer class also does not contain the list of rented vehicles, as this information can be found in the rental class.
class Customer:
    def __init__(self, customer_id, customer_name, phone_number, email=None, driver_license=None):
        #Adding validation to customer_id, customer_name, and phone_number to ensure that an incomplete customer records are not
        #stored in the system. email and driver_license are optional since main.py's registration flow does not currently collect them.
        if not customer_id:
            raise ValueError("Customer ID cannot be empty.")
        if not customer_name:
            raise ValueError("Customer name cannot be empty.")
        if not phone_number:
            raise ValueError("Phone number cannot be empty.")

        self.customer_id = customer_id
        self.customer_name = customer_name
        self.phone_number = phone_number      # Phone number and email are kept separate so that each can be validated and displayed independently. 
        self.email = email
        self.driver_license = driver_license

    # Display the customer information in a format that will be easy to read by the user.
    def display_details(self):
        print(f"Customer ID: {self.customer_id}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Phone Number: {self.phone_number}")
        print(f"Email Address: {self.email}")
        print(f"Driver License: {self.driver_license}")

    def to_dictionary(self):
        return {
            "customer_id": self.customer_id,
            "customer_name": self.customer_name,
            "phone_number": self.phone_number,
            "email": self.email,
            "driver_license": self.driver_license
        }
    def update_details(self, new_name=None,new_phone_number=None, new_email=None, new_driver_license=None):
        if new_name:
            self.customer_name = new_name
        if new_email:
            self.email = new_email
        if new_driver_license:
            self.driver_license = new_driver_license
        if new_phone_number:
            self.phone_number =new_phone_number