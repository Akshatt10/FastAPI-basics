from fastapi import FastAPI

api = FastAPI()


all_todos = [
    {'todo_id': 1, 'todo_name': 'Learn FastAPI', 'todo_description': 'Learn FastAPI with Python', 'completed': False},
    {'todo_id': 2, 'todo_name': 'Learn Python', 'todo_description': 'Learn Python with FastAPI', 'completed': False},
    {'todo_id': 3, 'todo_name': 'Learn Django', 'todo_description': 'Learn Django with Python', 'completed': False},
    {'todo_id': 4, 'todo_name': 'Learn Flask', 'todo_description': 'Learn Flask with Python', 'completed': False},
    {'todo_id': 5, 'todo_name': 'Learn JavaScript', 'todo_description': 'Learn JavaScript with Python', 'completed': False},
]
#GET, POST, PUT, DELETE

@api.get('/')
def index():
    return {"HELLO WORLD"}

@api.get('/todos/{todo_id}')
def get_todo(todo_id: int):
    for todo in all_todos:
        if todo['todo_id'] == todo_id:
            return {'result': todo}
    return {'error': 'Todo not found'}    



@api.get('/todos')
def get_todos(first_n: int = None):
    if first_n:
        return {'result': all_todos[:first_n]}
    else:
        return {'result': all_todos}
       