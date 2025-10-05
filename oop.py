# words = input('Sentence: ').strip()
# print(len(words.split()))


def count_word(sentence):
    count = len(sentence.split())
    return count


# print(count_word('How are you feeling about python'))

# OOP - object oriented programming. 
# class - A blueprint of the object
# self - a reference to the class
# constructor - it is a function in class that runs automatically when the instance of the class is made

class Car:
    # properties
    brand = 'Toyota'
    model = 'corolla'
    color = 'black'
    
    # functions
    def start_engine(self):
        print(f'{self.brand} is starting..')
        
        
    
mycar = Car()
emmaCar = Car()
preciousCar = Car()

# print(type(mycar))
mycar.brand = 'Audi'
# print(emmaCar.brand)
# print(mycar.brand)

# mycar.start_engine()

# name = str('dami')  # creating a new instance of a class str
# students = []

# print(type(name))




class Calc:
    brand = None 
    color = None
    
    def __init__(self, my_brand, my_color):
        # print('Welcome')
        self.brand = my_brand
        self.color = my_color
    
    def on(self):
        print(f'''
        {self.brand} Calculator
        
        1. Addition
        2. Subtraction
        #. Exit
        ''')
        
        choice = input('Choice: ')
        if choice == '1':
            self.addition()
        elif choice == '2':
            self.subtract()
        elif choice == '#':
            print('Good bye!')
            exit()
            
    def addition(self):
        val1 = int(input('Value 1: '))
        val2 = int(input('Value 2: '))
        print(F'Answer = {val1 + val2}')
        self.on()
        
    def subtract(self):
        val1 = int(input('Value 1: '))
        val2 = int(input('Value 2: '))
        print(F'Answer = {val1 - val2}')
        self.on()
        
        
        
# my_calc = Calc('Cascio', 'blue')
# my_calc.on()

# awaals = Calc('Porpo', 'white')
# awaals.on()
# awaals.color = 'white'


class TodoConfig:
    database = []
    
    def __init__(self):
        self.home()
    
    def home(self):
        print(''' 
        1. Add Todo
        2. Edit Todo
        3. Delete Todo
        4. View Todos
        5. Clear Todos
        #. Exit
        ''')
        choice = input('Choice: ').strip()
        if choice == '1':
            self.addTodo()
        elif choice == '2':
            self.editTodo()
        elif choice == '3':
            self.deleteTodo()
        elif choice == '4':
            self.viewTodos()
        elif choice == '5':
            self.clearTodos()
        elif choice == '#':
            exit()
        else:
            print('Invalid Input')
            self.home()
            
    def addTodo(self):
        todo = input('Todo: ').strip().capitalize() 
        self.database.append(todo)
        print('Todo added successfully')
        self.decide()
        
    def editTodo(self):
        pass
    
    def deleteTodo(self):
        pass
    
    def viewTodos(self):
        pass
    
    def clearTodos(self):
        pass
    
    def decide(self):
        user = input('Press enter to continue or 1 to exit: ').strip()
        if user == '1':
            exit()
        else:
            self.home()
    
    
# myTodo =  TodoConfig()
# myTodo.home()


# component of oop 
# 1. Encapsulation
    # i. private, public, static, protected
    

class Todo:
    __database = [] # private property
    name = 'MyTodo'  # public property

    def home(self):
        print(f'''
            Welcome to {self.name} App
        ''')
        
    # def displayName(self):
    #     return self.__name
        
    # def changeName(self, new_name):
    #     self.__name = new_name
        
    def showDB(self):
        return self.__database
    
    @staticmethod
    def square():
        print('Yeah yeah')

app = Todo()
# app.home()
# print(app.database)
# app.__name = 'HabeebTodo'
# app.home()
# print(app.displayName())
# app.changeName('HabeebTodo')
# app.home()
# app.square()


# 2. Inheritance

class Parent:
    __surname = 'Ojo'
    firstname = 'Ade'
    hobby = 'Read'
    
    def __init__(self):
        print(f'Hello. My name is {self.firstname} {self.__surname}. I love to {self.hobby}')
        
    def drive(self):
        print(f'{self.firstname} can drive a car')
        
# parent = Parent()
# parent.drive()

class Child(Parent):
    
    def __init__(self):
        self.firstname = 'Dapo'
        self.hobby = 'Code'
        print(self.hobby)
        # print(self.__surname)
    
        super().__init__()
        # Parent.__init__(self)
    

# child = Child()
# child.firstname = 'Dapo'
# child.drive()




class Parent:
    surname = None
    firstname = None
    hobby = None
    
    def __init__(self, lname, fname, hobby='Sleep'):
        self.surname = lname
        self.firstname = fname
        self.hobby = hobby
        
        self.intro()
    
    def intro(self):
        print(f'Hello. My name is {self.firstname} {self.surname}. I love to {self.hobby}')

# parent = Parent('Adigun', 'Ewatomi')


class Child(Parent):
    
    def __init__(self, lname, fname, hobby='Sleep'):
        super().__init__(lname, fname, hobby)


# child = Child('Adigun', 'Ewatomi', 'code')





class Bank:
    __balance = 0
    __bank_name = None
    
    def __init__(self, name):
        self.__bank_name = name
        
    def home(self):
        print(f'''
        Welcome to {self.__bank_name}
        
        1. deposit
        2. withdraw
        3. check balance
        #. exit
        ''')
        
        choice = input('Choice: ')
        if choice == '1':
            self.deposit()
        elif choice == '2':
            self.withdraw()
        elif choice == '3':
            self.check_balance()
        elif choice == '#':
            print('Bye...')
            exit()
        else:
            print('Invalid input. Try again')
            self.home()
            
    def check_balance(self):
        print(f'Your balance is ${self.__balance}')
        self.home()
            
    def deposit(self):
        amount = float(input('Amount: '))
        if amount < 1:
            print('Do you know what you are doing at all.. ')
        else: 
            self.__balance += amount
            print('Deposit successfull')
            
        self.home()
        
    def withdraw(self):
        amount = float(input('Amount: '))
        if amount < 1:
            print('Do you know what you are doing at all.. ')
        elif amount > self.__balance:
            print('Insufficient fund')
        else:
            self.__balance -= amount
            print('Withrawal successfull')
               
        self.home()
        
        
# bk = Bank('Jejelayegba')
# bk.check_balance()
# bk.home()


# Modularization
# 1. Script;  A file
# 2. Module; More than one script
# 3. Library; collection of modules and packages
# 4. Framework

from config.bank_config import BankConfig
# from bank import home as hm
# import bank
import random as rm
import time
import datetime as dt
import pyttsx3

# engine = pyttsx3.init()
# engine.say("I will speak this text")
# engine.runAndWait()

# bank.home()
# hm()
# print(rm.randint(1000000000, 1099999999))

# print('Loading...')
# time.sleep(2)
# print('Done')

# print(dt.datetime.now())


