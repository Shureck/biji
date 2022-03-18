from fastapi import FastAPI
import schema
app = FastAPI()

@app.get("/")
async def getR():
    return "lol"

@app.get("/add")
async def addUser():
    schema.add_new_user("shureck", "keklol","fuck_lol")
    return "lol"

@app.get("/get")
async def getUser():
    t = schema.get_user("shureck")
    return t