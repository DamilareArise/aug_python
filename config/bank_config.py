from random import randint 

def shout():
    return 'Shouting'


class BankConfig:
    __database = []
    __bank_name = None
    
    def __init__(self, name):
        self.__bank_name = name
        
    def createAccount(self, fullname, email, password):
        account_no = randint(1000000000, 1099999999)
        user = {
            'fullname': fullname,
            'email': email,
            'password': password,
            'account_no': account_no,
            'balance': 0.0
        }
        self.__database.append(user)
        return {
            'status': True,
            'message': 'Registration successfull'
        }
        
    
    def Login(self, email, password):
        
        for user in self.__database:
            if user['email'] == email and user['password'] == password:
                return {
                    'status': True,
                    'message': 'Login successfull',
                    "data": user
                }
                
        return {
            'status': False,
            'message': 'Invalid Email or Password'
        }        
        