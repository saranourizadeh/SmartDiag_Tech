# app/main.py
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import numpy as np
from PIL import Image
import io

from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model

app = FastAPI()
model = load_model('app/model/model1.h5')



@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    img = Image.open(io.BytesIO(contents))
    img= np.array(img.resize((331, 331)))
    img_batch = np.expand_dims(img, 0)
    img_array = np.stack((img_batch,) * 3, axis=-1)
    # img = img.resize((331, 331))
    # img_array = Image.img_to_array(img)

# Convert PIL Image to NumPy array
    # img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    covid_probability = prediction[0][0]

    return JSONResponse(content={"covid_probability": float(covid_probability)})
