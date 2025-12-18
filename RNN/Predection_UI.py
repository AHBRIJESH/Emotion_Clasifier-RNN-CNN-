from tensorflow.keras.models import load_model
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import tensorflow as tf
import numpy as np
import pandas as pd 

class interface(App):
    
    def build(self,*args):
        self.layout = BoxLayout(orientation='vertical')
        label_ui = Label(text = "Enter your sentence",size_hint=(0.40,0.001))
        self.layout.add_widget(label_ui)
        self.user_input = TextInput(hint_text = 'type here',size_hint=(0.70,0.01),pos_hint={'x':0.25 ,'y':0.5})
        self.layout.add_widget(self.user_input)
        self.button = Button(text='Submit',on_press = self.response,size_hint=(0.09,0.010),bold=True,pos_hint={'x':0 ,'y':0.5})
        self.layout.add_widget(self.button)
        return self.layout
    
    def response(self,instance):
        sentence = self.user_input.text
        data = pd.read_csv('training.csv')
        tokenizer = tf.keras.preprocessing.text.Tokenizer()
        tokenizer.fit_on_texts(data['text'])
        sequence = tokenizer.texts_to_sequences([sentence])
        padding = tf.keras.preprocessing.sequence.pad_sequences(sequence,maxlen=66)
        
        model = load_model('model.h5')
        predict = np.argmax(model.predict(padding))
        emotions = ['sadness','happy','love','anger','fear','suprise']
        print(predict)
        self.layout.clear_widgets()
        response_label = Label(text=emotions[predict])
        self.layout.add_widget(response_label)
        home_button = Button(text="Home",on_press= self.home_screen)
        self.layout.add_widget(home_button)
        return self.layout
    
    def home_screen(self,instance):
        self.layout.clear_widgets()
        label_uin = Label(text = "Enter your sentence")
        self.layout.add_widget(label_uin)
        self.user_inputn = TextInput(hint_text = 'type here',size_hint=(0.70,0.10))
        self.layout.add_widget(self.user_inputn)
        layoutn_button = Button(text='Submit',on_press = self.response,size_hint=(0.05,0.10),bold=True)
        self.layout.add_widget(layoutn_button)
        return self.layout

if __name__ == "__main__":
    interface().run()