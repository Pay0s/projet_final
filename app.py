from flask import Flask
from PIL import Image

from ultralytics import YOLO
import numpy as np
from PIL import Image
import requests
from io import BytesIO
import cv2



app = Flask(__name__)

@app.route('/')
def image():

    chemin_image = "../valid/images/IMG_0786_jpeg.rf.f355de46249dd1b66e53e120a9b260cb.jpg"
    image = Image.open(chemin_image)

    model = YOLO("yolov8n.pt")

    response = requests.get("https://images.unsplash.com/photo-1600880292203-757bb62b4baf?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2070&q=80")
    image = Image.open(BytesIO(response.content))
    image = np.asarray(image)

    results = model.predict(image)

    text = str(results[0].boxes.boxes)

    return text

if __name__ == '__main__':
    app.run(debug=True)
