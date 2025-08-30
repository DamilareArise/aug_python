# print("Hello World.")

# Core concepts about 
# 1. It is a high level pragramming language
# 2. it is versatile
# 3. it is open source
# 4. it is object oriented

# Commenting
# 1. For documentation
# 2. For debugging

# block comment
# line comment
"""
    I am a student of SQI in the department 
    of AI
"""

# print("""
      
#     Welcome to class Damilare
#     1. sign in
#     2. sign up
      
#     """)


# Indentation
# print("Hello")

# def run():
#     print('I am running')

# run()



# python varaibles
# variables are symbolic names that acts as containers for storing values
# i. variable name
# ii. assignment operation (funnel)
# iii. value
box = "cloths"
box = "Water"
# print(box)

# Rules guiding python variable declarations
# 1. You don't start a variable name with any symbols aside _ or alphabet
# 2. You don't include spaces during variable declaration. You use either camel casing, pascal casing or snake casing 
# 3. You don't use python's special keywords
# 4. your varaible name should be descriptive enough 


first_name = 'Damilare' # snake casing
FirstName = 'Damilare' # pascal casing
firstName = 'Damilare' # Camel casing

# types of variable declaration
# 1. single variable single value
first_name = 'Damilare'

# 2. single variable multiple values
students = 'raji', 'precious', 'emmanuel'
# print(students)

# 3. multiple variable single value 
x = y = z = 10
# print(z)
# z = z + 2
# print(x)

# 4. multiple variables multiple values
# x, y, z = 10, 11, 12
# print(z)


# Dynamic variable
# name = input('Your name: ')
# age = input('Age: ')
# dept = input("Department: ")
# print(name)

# Concatenation -> joining two strings together
# print("I am " + "Happy " + "100")

# print("Welcome",100)
# print("My name is "+name+" I am "+age+"Years old. I am in the department of "+dept+". Thank you")

# f-string 
# print(f"My name {name}, I am {age}years old. I am in the department of {dept}. Thank you.")

# python datatypes
# python operators
# conditional statement

# Build a simple alata calculator

'''
DATA TYPES

1. number type;
    i. integers - int() e.g 34, 54, 600
    ii. float - float() e.g 2.94 
    iii. Complex - complex() e.g 2 + 3j

2. Text types; string - str()
3. Sequence types; 
    1. List - list() e.g [2, 3, 4]
    ii. Tuple - tuple() e.g (2, 3, 4)
    iii. Range - range()
4. Mapping type; dictionary - dict()
5. Boolean type; bool() e.g True and 
6. Set type; set() e.g {1, 4, 5}
7. None type;
8. Binary Type; 
    1. byte
    2. bytearray
'''
# int
# float
# complex
# type - class 
# print - functions
# name

# mynum = 20.9 + 2j
# var = ('Precious', 'Emmanuel', 'Awwal')
# values = list(range(1, 11, 2))
# var.
# print(type(var))
# print(values)

# student = {
#     "name": "Ade ojo",
#     "age": 20,
#     "state": "Osun State"
# }
# print(student['age'])

# isMarried = int(False)
# print(type(isMarried))
# print(isMarried)

# a = "Marad" 
# print(int(a))

# setA = {'Precious', 'Emmanuel', 'Awwal'}
# setA = {1, 4, 3, 5, 6, 7, 2}
# print(setA)

var = None
# print(type(var))

# name = b'ade'
# print(name[0])

"""
PYTHON OPERATORS

1. Arithmetic operator: +, -, /, *, **, //, %
2. Assignment operator: =, +=, -=, /=, *= e.t.c
3. Logical operator; and, or, not
4. Comparison operator; ==, !=, >, <, >=, <=
5. Membership operator; in, not in
6. Identity operator; is, is not
7. bitwise operator; 
    & - and
    | - or
    ^ - xor
    ~ - not

"""
# print(5 % 2)
# val = 5
# val += 1  # val = val + 1
# print(val)

"""

A______B______AND______OR______XOR____ NOT A
0      0        0       0        0       1
0      1        0       1        1       1
1      0        0       1        1       0
1      1        1       1        0       0
"""

rice = True
beans = False

# print(rice and beans)
# print(rice or beans)
# print(not rice)

# val = 5
# val2 = '5'
# print(val == 5)
# print(val != 5)
# print(val >= 5)

# print(val is val2)

students  = ['ayo', 'marad', 'precious', 'emmanuel', 'awwal']
# print('ayo' in students)
# print('ade' not in students)


val = 10
val2 = 2 
# print(bin(val))
# print(bin(val2))
# res = val | val2
# print(f"result = {res} in binary {bin(res)}")

# print(bin(~val))



# 1 0 1 0
# 0 0 1 0
# 1 0 1 0

rice = False
beans = False

if rice and beans:
    print('I got what you asked for')
    
# elif rice:
#     print('I will buy rice becuase there is no rice and beans')
    
# elif beans:
#     print('I bought beans becuase there is no rice.')
    
# elif rice or beans:
#     print('I got just one of the demand')

elif rice or beans:
    if rice:
        print('I got just rice')
    else:
        print('I got just beans')
    
else:
    print('Market dry oo')
    
    
# an USSD application
code = input('Enter ussd code: ')
if code == '*312#':
    print('''
        1. Data plan
        2. Check balance
        #. Exit 
    ''')
    choice = input('Choice: ')
    if choice == '1':
        print('Data plan')
    elif choice == '2':
        print('Check balance')
    elif choice == '#':
        print('Goodbye!')
    else:
        print('Invalid Option')
else:
    print('Invalid ussd code. Try again!')


# ASSIGNMENT
# 1. Complete the ussd app.
# 2. Build a grading system


# class work
# build an app that differentiate between odd and even numbers 