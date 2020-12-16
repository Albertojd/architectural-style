from __future__ import division, print_function

# Keras
from keras.models import load_model
from keras.applications.imagenet_utils import preprocess_input

# Flask 
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

import os
import numpy as np
import cv2

from keras.preprocessing.image import load_img, img_to_array

from PIL import Image

names = ['Baroqoue','Byzantine','Egyptian','Gothic']

# Definimos una instancia de Flask
app = Flask(__name__)
# Path del modelo preentrenado
MODEL_PATH = 'modelo/model.h5'

# Cargamos el modelo preentrenado
model = load_model(MODEL_PATH)

# Realizamos la predicción usando la imagen cargada y el modelo
def model_predict(file_path, target_size=(64,64)):
    img=load_img(file_path)
    img = img.resize(target_size)
    img=img_to_array(img)
    img=np.expand_dims(img, axis=0) 
    pred=model.predict(img) 
    result=pred
    style=names[np.argmax(result)]
    return style

@app.route('/', methods=['GET'])
def index():
    # Página principal
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Obtiene el archivo del request
        f = request.files['file']

        # Graba el archivo en ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)
        preds = model_predict(file_path)              
        return preds
    return None

if __name__ == '__main__':
    app.run(debug=True, threaded=False)