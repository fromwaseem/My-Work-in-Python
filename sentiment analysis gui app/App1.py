
from tkinter import *

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import model_from_json
from tensorflow.keras.preprocessing.text import tokenizer_from_json
from tensorflow.keras.preprocessing import sequence
import numpy as np
import pickle

with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)
#print("Loading saved tokenizer...")

# load json and create model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()

model = model_from_json(loaded_model_json)
# load weights into new model
model.load_weights("my_model.h5")
#print("Loading saved model...")

def predict_response(response):
    '''
    0 - very negative
    1 - somewhat negative
    2 - neutral
    3 - somewhat positive
    4 - very positive
    '''
    print(f'You said: \n{response}\n')
    
    response = tokenizer.texts_to_sequences(response)
    response = sequence.pad_sequences(response, maxlen=11109)
    pred = np.argmax(model.predict(response))
    if pred == 0:
        return 'Very Negative'
    elif pred == 1:
        return 'Somewhat Negative'
    elif pred == 2:
        return 'Nuetral'
    elif pred == 3:
        return 'Somewhat Positive'
    elif pred == 4:
        return 'Very Positive'   
    

class Application(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.instruction = Label(self,text ="Find the Sentiment Score of your sentence!")
        self.instruction.grid(row=0, column=0, columnspan = 2, sticky= W)

        self.sentence = Label(self, text = "Enter a sentence: ")
        self.sentence.grid(row=1, column=0, sticky=W)

        self.entry = Entry(self)
        self.entry.grid(row = 1, column=1,sticky=W)

        self.submit_button= Button(self,text="submit", command=self.reveal)
        self.submit_button.grid(row=2, column=0, sticky = W)

        self.text = Text(self,width=35,height = 5, wrap = WORD)
        self.text.grid(row=3, column = 0, columnspan = 2, sticky = W)

        self.clear_button = Button(self, text = "Clear text", command =self.clear_text)
        self.clear_button.grid(row=2, column=1, sticky=W)
        
    def reveal(self):
        self.text = Text(self,width=35,height = 5, wrap = WORD)
        self.text.grid(row=3, column = 0, columnspan = 2, sticky = W)
        
        
        response = predict_response(response=[self.entry.get()])
       
        message = (response)
       
        self.text.insert(0.0,"This is the sentiment score\n" + str(message)+ "\n ")
            
    def clear_text(self):
        self.text = Text(self,width=35,height = 5, wrap = WORD)
        self.text.grid(row=3, column = 0, columnspan = 2, sticky = W)
        
        

root = Tk()
root.title("Sentiment Aanalysis ")

app = Application(root)

root.mainloop()        