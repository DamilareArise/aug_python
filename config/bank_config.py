from random import randint 

def shout():
    return 'Shouting'


class BankConfig:
    __database = []
    __bank_name = None
    
    def __init__(self, name):
        self.__bank_name = name
        
    def createAccount(self, fullname, email, pass1, pass2):
        if pass1 != pass2:
            return {
                'status': False,
                'message': 'Password do not match'
            }
        else:
            account_no = randint(1000000000, 1099999999)
            
            user = {
                'fullname': fullname,
                'email': email,
                'password': pass1,
                'account_no': account_no,
                'balance': 0.0
            }
            self.__database.append(user)
            return {
                'status': True,
                'message': 'Registration successfull'
            }
        
    
    def login(self, email, password):
        
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
        
    
    def performDeposit(self, email, amount:float):
        for user in self.__database:
            if user['email'] == email:
                user['balance'] += amount
                return {
                    'status': True,
                    'message': f'{amount} deposited successfully',
                    'data': user
                }
        
        return {
            'status': False,
            'message': f'User not found',
        }
                   
             
        
    def getBankName(self):
        return self.__bank_name