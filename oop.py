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
    
    
myTodo =  TodoConfig()
# myTodo.home()


# component of oop 
# 1. Encapsulation
# 2. Inheritance