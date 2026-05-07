from flask import Flask, render_template, request
import os
from utils import predict_image, get_disease_info

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        image = request.files['image']
        if image:
            filepath = os.path.join(UPLOAD_FOLDER, image.filename)
            image.save(filepath)

            prediction, confidence = predict_image(filepath)
            info = get_disease_info(prediction)

            return render_template('index.html',
                                   prediction=prediction,
                                   confidence=confidence,
                                   filename=image.filename,
                                   info=info)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)