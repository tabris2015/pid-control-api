import uvicorn
from enum import Enum
from typing import Optional
from fastapi import FastAPI


class ModelName(str, Enum):
    alexnet = 'alexnet'
    resnet = 'resnet'
    lenet = 'lenet'


app = FastAPI()
fake_items_db = [{'item_name': 'ahu'}, {'item_name': 'uha'}, {'item_name': 'asdf'}]


@app.get('/')
async def root():
    return {'mensaje': 'hola bola'}


@app.get('/items/')
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip:skip + limit]


@app.get('/items/{item_id}')
async def read_item(item_id: int, q: Optional[str] = None, short: bool = False):
    if q:
        return {'item_id': item_id, 'q': q}
    return {'item_id': item_id}


@app.get('/users/me')
async def read_user_me():
    return {'user_id': 'usuario actual'}


@app.get('/users/{user_id}')
async def read_user(user_id: str):
    return {'user_id': user_id}


@app.get('/model/{model_name}')
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {'model_name': model_name, 'message': 'ahuuu'}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@app.get('/files/{file_path:path')
async def read_file(file_path: str):
    return {'file_path': file_path}

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)
