import numpy as np
from flask import Flask, request, jsonify
from PIL import Image
import torch
from io import BytesIO

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def image():
    chemin_model = "./runs/train/exp4/weights/best.pt"
    model = torch.hub.load('ultralytics/yolov5', 'custom', path=chemin_model, force_reload=True)

    uploaded_file = request.files['file']

    if uploaded_file.filename == '':
        return jsonify({"error": "Aucune image téléchargée."}), 400
    
    file_content = uploaded_file.read()
    image = Image.open(BytesIO(file_content))
    image = np.asarray(image)

    results = model(image)

    boxes = results.pred[0].numpy()  # Par exemple, pour obtenir les boîtes de détection de la première classe

    # Créez un dictionnaire Python contenant les résultats
    response_data = {"boxes": boxes.tolist()}  # Utilisez tolist() pour convertir les tableaux numpy en listes Python

    # Utilisez jsonify pour renvoyer une réponse JSON
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
