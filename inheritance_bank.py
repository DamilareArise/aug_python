from config.bank_config import BankConfig

class UbaConfig(BankConfig):
    
    def __init__(self, name):
        super().__init__(name) 
        
    def home(self):
        print(f'''
            Welcome to {self.getBankName()}
        1. Create account
        2. Log in
        #. Exit   
        ''') 
        
        choice = input('Choice: ')
        if choice == '1':
            self.register()
        elif choice == '2':
            self.signin()
        elif choice == '#':
            exit()
        else:
            print('Invalid input')
            self.home()
    
    def register(self):
        fullname = input('Fullname: ')
        email = input('Email: ')
        password1 = input('Password: ')
        password2 = input('Confirm Password: ')
        
        result = self.createAccount(fullname, email, password1, password2)
        
        message = result['message']
        
        if result['status']:
            print(message)
            self.signin()
            
        else:
            print(message)
            self.home()
            

       
    def signin(self):
        print('Login')
        email = input('Email: ')
        password = input('Password: ')   

        result = self.login(email, password)
        message = result['message']
        if result['status']:
            print(message)
            user = result['data']
            self.dashboard(user)
            
        else:
            print(message)
            self.signin()
    
    
    def dashboard(self, user:dict):
        print(f"""
        Welcome back {user['fullname']}
        account number: {user['account_no']}
        account balance: {user['balance']}
        
        1. Deposit
        2. Withdraw
        3. Transfer
        4. Back to home
        """)
        
        choice = input('Choice: ')
        if choice == '1':
            self.__deposit(user['email'])
        elif choice == '2':
            self.withdraw()
            
        elif choice == '4':
            self.home()
        else:
            print('Invalid input')
            self.dashboard(user) 
            
    def __deposit(self, email):
        print('Deposit')
        amount = float(input('Amount: '))
        result = self.performDeposit(email, amount)
        message = result['message']
        if result['status']:
            print(message)
            user = result['data']
            self.dashboard(user)
        else:
            print(message)
            self.home()
    
    def withdraw():
        pass
    
    
       
    


uba = UbaConfig('UBA')
