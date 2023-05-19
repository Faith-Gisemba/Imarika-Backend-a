class CustomerService:
    def __init__(self, email, phone_number):
        self.email = email
        self.phone_number = phone_number

    def contact_us(self, section):
        if section == 'email':
            print(f"Kindly send your email to {self.email} for any support.")
        elif section == 'phone_number':
            print(f"Kindly reach out to {self.phone_number} for any Support.")
        else:
            print("You selected an invalid section. Please try again.")

customer = CustomerService("techica@imarika.com", "1234567890")
customer.contact_us("email")

