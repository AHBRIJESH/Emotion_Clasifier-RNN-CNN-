from tensorflow.keras.preprocessing.image import load_img
import numpy as np
import requests

img = load_img('1000_F_60587854_dm0AgQ2xWPRRnsZeNubLM9yY5omv2TxV.jpg', target_size=(64, 64))
img_array = np.array(img,dtype=np.float32) / 255.0
img_array = np.expand_dims(img_array, axis=0)

response = requests.post('http://localhost:5000/predict', json=img_array.tolist())

lv = ['angry', 'disgusted', 'fearful', 'happy', 'neutral', 'sad', 'surprised']

print('Predicted class:', lv[int(response.json()['predicted_class'])])