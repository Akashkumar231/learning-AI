from fastapi import FastAPI
import json

app = FastAPI()

def loadData():
    with open("patients.json" ,'r') as file:
        data = json.loads(file.read())
    return data

@app.get("/")
def hello():
    return {'message' : 'Hello World'}

@app.get('/about')
def about():
    return {'message': 'Welcome to learning AI'}

@app.get('/view')
def view():
    return loadData()