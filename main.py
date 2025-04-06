from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

api = FastAPI()

class TodoBase(BaseModel):
    todo_name: str
    todo_description: str
    completed: bool = False

class TodoCreate(TodoBase):
    pass

class TodoUpdate(TodoBase):
    pass

class TodoResponse(TodoBase):
    todo_id: int

all_todos: List[TodoResponse] = [
    TodoResponse(todo_id=1, todo_name='Learn FastAPI', todo_description='Learn FastAPI with Python', completed=False),
    TodoResponse(todo_id=2, todo_name='Learn Python', todo_description='Learn Python with FastAPI', completed=False),
    TodoResponse(todo_id=3, todo_name='Learn Django', todo_description='Learn Django with Python', completed=False),
    TodoResponse(todo_id=4, todo_name='Learn Flask', todo_description='Learn Flask with Python', completed=False),
    TodoResponse(todo_id=5, todo_name='Learn JavaScript', todo_description='Learn JavaScript with Python', completed=False),
]

@api.get('/todos/{todo_id}', response_model=TodoResponse)
def get_todo(todo_id: int):
    for todo in all_todos:
        if todo.todo_id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

@api.get('/todos', response_model=List[TodoResponse])
def get_todos(first_n: Optional[int] = None):
    if first_n:
        return all_todos[:first_n]
    return all_todos

@api.post('/todos', response_model=TodoResponse)
def create_todo(todo: TodoCreate):
    new_todo_id = max(todo.todo_id for todo in all_todos) + 1 if all_todos else 1
    new_todo = TodoResponse(todo_id=new_todo_id, **todo.dict())
    all_todos.append(new_todo)
    return new_todo

@api.put('/todos/{todo_id}', response_model=TodoResponse)
def update_todo(todo_id: int, todo: TodoUpdate):
    for i, todo_item in enumerate(all_todos):
        if todo_item.todo_id == todo_id:
            updated_todo = todo_item.copy(update=todo.dict())
            all_todos[i] = updated_todo
            return updated_todo
    raise HTTPException(status_code=404, detail="Todo not found")

@api.delete('/todos/{todo_id}', response_model=TodoResponse)
def delete_todo(todo_id: int):
    for i, todo_item in enumerate(all_todos):
        if todo_item.todo_id == todo_id:
            deleted_todo = all_todos.pop(i)
            return deleted_todo
    raise HTTPException(status_code=404, detail="Todo not found")
