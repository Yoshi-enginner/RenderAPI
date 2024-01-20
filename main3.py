from fastapi import FastAPI
import json

app = FastAPI()

temp = open("C:\\Users\\tokyo\\AppData\\Local\\TEST2022\\sample.json",'r')
sample_data = json.load(temp)

@app.get("/items")
async def get_messages():

    return sample_data
