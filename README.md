# Emotion Classifier – CNN & RNN

This repository contains **two deep learning–based emotion classification systems**:

1. **CNN-based Facial Emotion Recognition** (Image-based)
2. **RNN-based Emotion Classification** (Text-based)

The CNN model is production-ready, Dockerized, and deployable on **Docker & Kubernetes**.

---

## 📁 Project Structure

```
Emotion_Clasifier-RNN-CNN-
│
├── CNN/
│   ├── app.py                  # Flask API for CNN inference
│   ├── model.h5                # Trained CNN model (emotion classification)
│   ├── Dockerfile              # Docker configuration for CNN service
│   ├── requirements.txt        # Python dependencies
│   ├── cnn-deployment.yaml     # Kubernetes Deployment
│   ├── cnn-service.yaml        # Kubernetes Service (ClusterIP)
│   ├── test.py                 # Client-side test script
│   └── Image Classifier.ipynb  # CNN training & experimentation notebook
│
├── RNN/
│   ├── model.h5                # Trained RNN model (text emotion classification)
│   ├── Predection_UI.py        # Local UI / script for prediction
│   ├── TextClassifier1.ipynb   # RNN training notebook
│   ├── training.csv            # Training dataset
│   └── README.md               # RNN-specific documentation
```

---

## 🧠 CNN – Facial Emotion Recognition

A **Convolutional Neural Network (CNN)** trained to classify facial emotions from images.
The model is exposed as a **Flask REST API** and packaged as a **Docker container**.

### 🎭 Supported Emotions

* Angry
* Disgusted
* Fearful
* Happy
* Neutral
* Sad
* Surprised

---

## 🐳 Docker Image (CNN)

The CNN service is available as a public Docker image:

🔗 **Docker Hub Repository**
[https://hub.docker.com/repository/docker/brijesh944/emotion_cnn/general](https://hub.docker.com/repository/docker/brijesh944/emotion_cnn/general)

### ▶️ Run with Docker

```bash
docker run -p 5000:5000 brijesh944/emotion_cnn
```

Access:

```
http://localhost:5000
```

---

## ☸️ Run CNN with Kubernetes (Docker Desktop / Minikube)

### Deploy

```bash
kubectl apply -f cnn-deployment.yaml
kubectl apply -f cnn-service.yaml
```

### Verify

```bash
kubectl get pods
kubectl get svc
```

Inside the cluster, the service is accessible via:

```
http://cnn:5000
```

From local machine:

```bash
kubectl port-forward svc/cnn 5000:5000
```

---

## 📡 CNN API Endpoint

### POST `/predict`

**Request (JSON):**

```json
[[[[...image pixel values...]]]]
```

**Response:**

```json
{
  "predicted_class": 3
}
```

---

## 🧪 Testing the CNN API

Use the provided script:

```bash
python test.py
```

Or send a request using `requests`:

```python
requests.post("http://localhost:5000/predict", json=data)
```

---

## 🧠 RNN – Text Emotion Classification

The RNN module focuses on **text-based emotion detection** using sequential models.

### Features

* Trained RNN model (`model.h5`)
* Notebook for training & evaluation
* Local prediction UI / script
* CSV-based training dataset

> Note: The RNN module is currently designed for **local execution**, not containerized.

---

## 🛠️ Tech Stack

* Python 3
* TensorFlow / Keras
* Flask
* NumPy
* Docker
* Kubernetes
* Jupyter Notebook

---

## 🎯 Use Cases

* Facial emotion recognition demos
* Text-based emotion analysis
* ML inference microservices
* Docker & Kubernetes learning
* MLOps and deployment practice

---

## ⚠️ Notes

* The CNN service binds to `0.0.0.0:5000` for container compatibility
* Models are intended for **educational and prototype purposes**
* Not optimized for large-scale production inference

---

## 👤 Author

**Brijesh**
Computer Science Engineer | AI & Deep Learning Enthusiast

---

If you plan to extend this project:

* Add RNN Docker support
* Introduce model versioning
* Add Ingress / LoadBalancer
* Implement CI/CD for ML pipelines

🚀
