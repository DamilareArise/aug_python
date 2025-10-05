
database = []
print('Welcome to myBank')
def home():
    print('''
       1. Create account
       2. Login
       #. exit   
    ''')
    choice = input('Choice: ').strip()
    if choice == '1':
        signup()
    elif choice == '2':
        login()
    elif choice == '#':
        exit()
    elif choice == '**':
        viewUsers()
    else:
        print('Invalid option')
        home()
        
def signup():
    print('Signup page\n')
    user = {
        'fullname': input('Fullname: ').strip().title(),
        'email': input('Email: ').strip().lower(),
        'password': input('Password: '),
        'balance': 0.0
    }
    
    database.append(user)
    print('Account created successfully')
    home()
    

def login():
    print('Login page\n')
    email = input('Email: ').strip().lower()
    password = input('Password: ')
    
    for user in database:
        if user['email'] == email and user['password'] == password:
            dashboard(user)

    print('Invalid email or password')
    home()
    

def viewUsers():
    print(database)
    home()

def dashboard(user):
    print(f'''
    Welcome back {user['fullname']}
    account balance: {user['balance']}
    
    1. Deposit
    2. Withdraw
    #. Home
    ''')
    choice = input('Choice: ').strip()
    if choice == '1':
        deposit()
    elif choice == '2':
        withdraw()
    elif choice == '#':
        home()
    else:
        print('Invalid input')
        dashboard(user)

def deposit():
    pass

def withdraw():
    pass

# home()

