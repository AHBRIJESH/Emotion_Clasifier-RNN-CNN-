from tensorflow.keras.models import load_model
from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)
model = load_model('model.h5')

@app.route('/predict', methods=['POST'])
def predict():  
    data = np.array(request.get_json(),dtype=np.float32)
    prediction = model.predict(data)
    predicted_class = int(np.argmax(prediction, axis=1)[0])
    return jsonify({'predicted_class': float(predicted_class)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)