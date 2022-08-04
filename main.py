
from model import Param
from fastapi import FastAPI
import pickle

app = FastAPI()


@app.on_event("startup")
def load_model():
    global model
    model = pickle.load(open("forestfirepediction.pkl", "rb"))


@app.get('/')
def index():
    return {'message': 'This is the homepage of the API '}


@app.post('/predict')
def get_music_category(data: Param):
    received = data.dict()
    x = received['x']
    y = received['y']
    month = received['month']
    is_weekend = received['is_weekend']
    ffmc = received['ffmc']
    dmc = received['dmc']
    dc = received['dc']
    isi = received['isi']
    temp = received['temp']
    rh = received['rh']
    wind = received['wind']
    rain = received['rain']
    area = received['area']
    pred_value = model.predict([[x, y, month,
                                 is_weekend, ffmc, dmc, dc, isi, temp, rh, wind, rain, area]]).tolist()[0]
    return {'prediction': pred_value}