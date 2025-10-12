from random import randint 
import mysql.connector as sql


class BankConfig:
    __bank_name = None
    __host='127.0.0.1'
    __port='3306'
    __user='root'
    __password=''
    __database=None
    __conn=None
    __cursor=None
    
    def __init__(self, name, db_name, db_pass):
        self.__bank_name = name
        self.__database = db_name
        self.__password = db_pass
        
        # create connection
        self.__conn = sql.connect(
            host=self.__host,
            port=self.__port,
            user=self.__user,
            password=self.__password,
            database=self.__database
        )
        self.__conn.autocommit = True
        self.__cursor = self.__conn.cursor()
        
    def createAccount(self, fullname, email, pass1, pass2):
        if pass1 != pass2:
            return {
                'status': False,
                'message': 'Password do not match'
            }
        else:
            account_no = randint(1000000000, 1099999999)
            
            query = 'INSERT INTO customer_table(fullname, email, password, account_no) VALUES(%s, %s, %s, %s)'
            values = (fullname, email, pass1, account_no)
            self.__cursor.execute(query, values)
        
            return {
                'status': True,
                'message': 'Registration successfull'
            }
        
    
    def login(self, email, password):
        query = "SELECT * FROM customer_table WHERE email=%s AND password=%s"
        values = (email, password)
        self.__cursor.execute(query, values)
        user = self.__cursor.fetchone()
        if user: 
            return {
                'status': True,
                'message': 'Login successfull',
                "data": user
            }
        else:       
            return {
                'status': False,
                'message': 'Invalid Email or Password'
            }   
    
    def fetchUser(self, email):
        query = 'SELECT * FROM customer_table WHERE email=%s'
        value = (email,)
        self.__cursor.execute(query, value)
        user = self.__cursor.fetchone()
        return user
    
    def updateBalance(self, email, balance):
        query = 'UPDATE customer_table SET account_balance=%s WHERE email=%s'
        values = (balance, email)
        self.__cursor.execute(query, values)
        return True
    
    def performDeposit(self, email, amount:float):
        if amount <= 0:
            return {
                'status': False,
                "message": "Invalid amount"
            }
            
        user = self.fetchUser(email)
        if user:
            balance = user[5] 
            new_balance = float(balance) + amount
            self.updateBalance(email, new_balance)
            
            user = self.fetchUser(email)
        
            return {
                'status': True,
                'message': f'{amount} deposited successfully',
                'data': user
            }
        
        return {
            'status': False,
            'message': f'User not found',
        }
          
    def performWithdraw(self, email, amount):
        if amount <= 0:
            return {
                'status': False,
                "message": "Invalid amount"
            }
        
        user = self.fetchUser(email)
        if user:
            balance = user[5]
            if balance < amount:
                return {
                    'status': False,
                    'message': f'Insufficient Fund',
                }
                    
            new_balance = float(balance) - amount
            self.updateBalance(email, new_balance)
            
            user = self.fetchUser(email)
        
            return {
                'status': True,
                'message': f'{amount} Withdrawn successfully',
                'data': user
            }
        
        return {
            'status': False,
            'message': f'User not found',
        }
             
        
    def getBankName(self):
        return self.__bank_name