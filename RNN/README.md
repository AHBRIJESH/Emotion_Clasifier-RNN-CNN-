# Sentence Emotion Predictor

![Naive Bayes](https://img.shields.io/badge/Implementation-Nural%20Network%20-darkblue)

## Overview

The Sentence Emotion Predictor is a Python application built using TensorFlow and Kivy that predicts the emotional tone of a given sentence. It employs a deep learning model trained on labeled data to classify sentences into different emotion categories, such as sadness, happiness, love, anger, fear, and surprise.

## Features

- **Emotion Classification:** The predictor categorizes sentences into different emotions, providing insights into the emotional content of text.
- **User-Friendly Interface:** The application offers a simple and intuitive interface for users to input sentences and receive emotion predictions.
- **Model Persistence:** Trained models are saved in HDF5 format for easy loading and reuse.
- **Data Preprocessing:** The application preprocesses input sentences by tokenizing and padding them to match the model's input requirements.

## Getting Started

### Prerequisites

To run the application, you need to have the following installed:

- Python (>= 3.6)
- TensorFlow
- Kivy
- NumPy
- pandas

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/sentence-emotion-predictor.git
   cd sentence-emotion-predictor
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Run the Python script `interface.py`:
   ```bash
   python interface.py
   ```

2. Enter a sentence in the provided text input field.

3. Click the "Submit" button to get the predicted emotion for the input sentence.

### Example

```python
from tensorflow.keras.models import load_model

# Load the model
model = load_model('model.h5')

# Make predictions
sentence = "I am feeling happy today!"
predictions = model.predict([sentence])
```

## Project Structure

- `interface.py`: The main Python script containing the Kivy application for predicting emotions.
- `model.h5`: The saved deep learning model in HDF5 format.
- `training.csv`: The labeled dataset used for training the emotion predictor model.
- `README.md`: The project's README file containing an overview, features, installation instructions, and usage guide.

## Predection_UI.py

This is a simple interface built using Kivy for emotion detection using a pre-trained deep learning model. Users can input a sentence, and the application will predict the emotion associated with that sentence.

## Getting Started

To run this application, you need to have Python installed on your system. Additionally, you need to install kivy.

```bash
pip install kivy
```

## Usage

1. **Running the Application:**

   Run the `Predection_UI.py` script to start the Kivy application.

   ```bash
   python Predection_UI.py
   ```

2. **Using the Interface:**

   - Upon running the application, you will see a text input field with a label asking to enter a sentence.
   
   - Type a sentence in the text input field and press the "Submit" button.
   
   - The application will process the input using a pre-trained deep learning model and display the predicted emotion.

   - You can press the "Home" button to go back to the initial screen and enter another sentence.

## Dependencies

- TensorFlow: For loading the pre-trained model and performing inference.
- Kivy: For building the graphical user interface.
- NumPy: For numerical computations.
- pandas: For data manipulation and loading the dataset.

## Contributing

Contributions to the Sentence Emotion Predictor are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

Happy predicting emotions! 🚀

