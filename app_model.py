from fastapi import FastAPI, requests, HTTPException, Query
from pydantic import BaseModel
import sqlite3
import uvicorn
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import pandas as pd
from typing import List


app = FastAPI()

class Anuncios(BaseModel):
    TV: float
    radio: float
    newspaper: float
    sales: float


conn = sqlite3.connect('./data/prediccion_anuncios.db')
cursor = conn.cursor()

@app.get("/")
async def hello():
    return "API de BBDD de Predicción de Anuncios"

# 1. Endpoint de predicción

# Cargar el modelo.
with open('./data/advertising_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

#Prediccion.
@app.post("/predict")
async def test_predict_endpoint(prediction_data: dict):  
        input_data = prediction_data['data'][0]    
        prediction = model.predict([input_data])[0]

        # Respuesta con la predicción.
        return {
        "input": {"TV": input_data[0], "radio": input_data[1], "newspaper": input_data[2]},
        "prediction": prediction
        }

# TypeError: Object of type OperationalError is not JSON serializable
# 2. Endpoint de ingesta de datos

@app.post("/ingest/")
async def test_ingest_endpoint(data: dict):  
    try:    
        data_list = data.get("data")
        cursor.executemany('INSERT INTO Advertising (TV, Radio, Newspaper, Sales) VALUES (?, ?, ?, ?)',
                            (data_list))
        conn.commit()
        return {'message': 'Datos ingresados correctamente'}
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)
    

""" @app.post("/ingest/")
async def test_ingest_endpoint(data: dict):  
    try:    
        data_list = data.get("data", [])
        for row in data_list:
            cursor.execute('INSERT INTO prediccion_anuncios (TV, radio, newpaper, sales) VALUES (?, ?, ?, ?)',
                            (row[0], row[1], row[2], row[3]))
        conn.commit()
        return {'message': 'Datos ingresados correctamente'}
    except Exception as e:
        raise HTTPException(status_code=500, detail=e) """



# 3. Endpoint de reentramiento del modelo

@app.post("/retrain")
async def test_retrain_endpoint():
    cursor.execute('SELECT TV, Radio, Newspaper, Sales FROM Advertising')
    tabla = cursor.fetchall()
    df = pd.DataFrame(tabla, columns=['TV', 'radio', 'newspaper', 'sales'])
    X = df[['TV', 'radio', 'newspaper']]
    y = df['sales']
    escalar = StandardScaler()
    X_scaled = escalar.fit_transform(X)
    model = LinearRegression()
    model.fit(X_scaled, y)
    return {'message': 'Modelo reentrenado correctamente.'}
     
# Ejecutar la aplicación
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)




