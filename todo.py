
print('Welcome to TodoApp')
todos = []

['eat', 'sleep']

[
    {
        'todo': 'eat',
        'completed': False
    }
]

def home():
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
        addTodo()
    elif choice == '2':
        editTodo()
    elif choice == '3':
        deleteTodo()
    elif choice == '4':
        viewTodos()
    elif choice == '5':
        clearTodos()
    elif choice == '#':
        exit()
    else:
        print('Invalid Input')
        home() # recursive function
 
def addTodo():
    todo = input('Todo: ').strip().capitalize() 
    todos.append(todo)
    print('Todo added successfully')
    decide()

def editTodo():
    no = int(input('Edit todo at number: '))
    if no > len(todos):
        print('Number out of range.Try again!')
    else:
        new_todo = input('New todo: ').strip().capitalize()
        todos[no-1] = new_todo 
        print('Todo edited successfully.')
        
    decide()

def deleteTodo():
    pass

def viewTodos():
    for x, todo in enumerate(todos, 1):
        print(f'{x}. {todo}')
        
    decide()

def clearTodos():
    pass

def decide():
    user = input('Press enter to continue or 1 to exit: ').strip()
    if user == '1':
        exit()
    else:
        home()
    
home()