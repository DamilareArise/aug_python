from config.bank_config import BankConfig

class UbaConfig(BankConfig):
    
    def __init__(self, name, db_name, db_pass):
        super().__init__(name, db_name, db_pass) 
        
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
    
    
    def dashboard(self, user):
        print(f"""
        
        Welcome back {user[1]}
        account number: {user[4]}
        account balance: ${user[5]}
        
        1. Deposit
        2. Withdraw
        3. Transfer
        4. Change password
        #. Back to home
        """)
        
        choice = input('Choice: ')
        if choice == '1':
            self.__deposit(user[2])
        elif choice == '2':
            self.withdraw(user[2])
            
        elif choice == '#':
            self.home()
        else:
            print('Invalid input')
            self.dashboard(user) 
            
    def __deposit(self, email):
        print('Deposit')
        try:
            amount = float(input('Amount: '))
        except ValueError as v:
            print('Input a number not an alphabet')
            self.home()
            
        result = self.performDeposit(email, amount)
        message = result['message']
        if result['status']:
            print(message)
            user = result['data']
            self.dashboard(user)
        else:
            print(message)
            self.home()
    
    def withdraw(self, email):
        print('Withdraw')
        amount = float(input('Amount: '))
        result = self.performWithdraw(email, amount)
        message = result['message']
        if result['status']:
            print(message)
            user = result['data']
            self.dashboard(user)
        else:
            print(message)
            self.home()
    
    
    
    
       
    


uba = UbaConfig('UBA', 'august_db', 'password')
uba.home()
