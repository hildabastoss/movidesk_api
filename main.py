from fastapi import FastAPI
from services.movidesk import get_data_movidesk

app = FastAPI()

@app.get('/home')
def home():
    return {"message":"welcome to setealem"}


@app.get('/movidesk')
def movidesk():
    return get_data_movidesk()    

