# 📊 API de Predicción de Anuncios 🚀

Esta es una API construida con **FastAPI** que permite realizar predicciones de ventas basadas en datos de anuncios publicitarios en diferentes medios (TV, radio, periódicos). Además, la API permite la ingesta de nuevos datos y el reentrenamiento del modelo de predicción. 📈

---

## 📋 Requisitos

- Python 3.11 🐍
- FastAPI 🚀
- Uvicorn ⚡
- SQLite3 🗃️
- Pandas 🐼
- Scikit-learn 🤖
- Pickle 🥒

---

## 🛠️ Instalación

1. Clona este repositorio o descarga el código. 📂
2. Instala las dependencias necesarias:

   ```bash
   pip install fastapi uvicorn sqlite3 pandas scikit-learn
Asegúrate de tener un archivo advertising_model.pkl en la carpeta ./data/ que contenga el modelo preentrenado. 🤖

🐳 Docker Hub

Esta aplicación también está disponible como una imagen de Docker en Docker Hub. Puedes descargarla y ejecutarla fácilmente en tu entorno local. 🐳

Pasos para usar la imagen de Docker:
Descarga la imagen desde Docker Hub:

bash
Copy
docker pull vanessalop/modelo_api-fastapi-app:latest
Ejecuta el contenedor:

bash
Copy
docker run -p 8000:8000 vanessalop/modelo_api-fastapi-app
La API estará disponible en http://127.0.0.1:8000. 🌐

🚀 Uso

Ejecutar la API
Para ejecutar la API, utiliza el siguiente comando:

bash
Copy
uvicorn app_model:app --reload
La API estará disponible en http://127.0.0.1:8000. 🌐

🔌 Endpoints

1. Endpoint de Predicción 🔮

Método: POST

Ruta: /predict

Descripción: Realiza una predicción de ventas basada en los datos de anuncios proporcionados.

Ejemplo de solicitud:

json
Copy
{
  "data": [[100, 50, 25]]
}
Ejemplo de respuesta:

json
Copy
{
  "input": {"TV": 100, "radio": 50, "newspaper": 25},
  "prediction": 15.3
}

2. Endpoint de Ingesta de Datos 📥

Método: POST

Ruta: /ingest/

Descripción: Permite ingresar nuevos datos de anuncios y ventas en la base de datos.

Ejemplo de solicitud:

json
Copy
{
  "data": [[100, 50, 25, 15.3], [200, 30, 40, 20.5]]
}
Ejemplo de respuesta:

json
Copy
{
  "message": "Datos ingresados correctamente"
}

3. Endpoint de Reentrenamiento del Modelo 🔄

Método: POST

Ruta: /retrain

Descripción: Reentrena el modelo de predicción utilizando todos los datos disponibles en la base de datos.

Ejemplo de respuesta:

json
Copy
{
  "message": "Modelo reentrenado correctamente."
}

🗃️ Base de Datos

La API utiliza una base de datos SQLite llamada prediccion_anuncios.db para almacenar los datos de anuncios y ventas. La tabla prediccion_anuncios tiene las siguientes columnas:

TV: Gasto en anuncios de TV. 📺

radio: Gasto en anuncios de radio. 📻

newspaper: Gasto en anuncios de periódicos. 📰

sales: Ventas generadas. 💰