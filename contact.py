class CustomerService:
    def __init__(self,email,phone_number):
        self.email == email
        self.phone_number = phone_number
        
        def contact_us(self,section):
            if section =='email': 
                print(f'kindly your email to {self.email} for any support')
                
            elif section =='phone_number': 
                print(f'Kindly reach out {self.phone_number} for any support')

            else:
                print('You selected an invalid section,please try again')