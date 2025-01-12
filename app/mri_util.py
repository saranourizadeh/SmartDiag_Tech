from fastapi import FastAPI, File, UploadFile
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
app = FastAPI()
endpoint = "http://localhost:8501/v1/models/mri_model:predict"
MODEL = tf.keras.models.load_model('/Users/saranourizadeh/code/YashS16/diagnostics-report-interpretation/project/app/model')
CLASS_NAMES = ['glioma_tumor', 'meningioma_tumor', 'no_tumor', 'pituitary_tumor']
@app.get('/')
def ping():
    # load a machine learning model
    # model.predict
    return {"ok": True}
def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)).resize((331, 331)))
    img = image.load_img(file.file, target_size=(331, 331))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    
    return image
@app.post("/predict")
async def predict(
    file: UploadFile = File(...)
    ):
     image = read_file_as_image(await file.read())
    #  img_batch = np.expand_dims(image, 0)
    #  my_img = np.stack((img_batch,) * 3, axis=-1)
     prediction = MODEL.predict(image)
     prediction_class = CLASS_NAMES[np.argmax(prediction[0])]
     confidence = np.max(prediction[0])
     return {
         'Class': prediction_class,
        'Confidence': float(confidence)
    }
