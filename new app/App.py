
from tkinter import *

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import model_from_json
from tensorflow.keras.preprocessing.text import tokenizer_from_json
from tensorflow.keras.preprocessing import sequence
import numpy as np
import pickle

with open('data/tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)
#print("Loading saved tokenizer...")

# load json and create model
json_file = open('data/model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()

model = model_from_json(loaded_model_json)
# load weights into new model
model.load_weights("data/model.h5")
#print("Loading saved model...")

def predict_response(response):
    '''
    0 - very negative
    1 - somewhat negative
    2 - neutral
    3 - somewhat positive
    4 - very positive
    '''
   # print(f'You said: \n{response}\n')
    
    response = tokenizer.texts_to_sequences(response)
    response = sequence.pad_sequences(response, maxlen=259)
    pred = np.argmax(model.predict(response))
    
    if pred == 0:
        return 'Negatívne' #' Negative'
    elif pred == 1:
        return 'pozitívne'#'pozitívne'
      
    

class Application(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.instruction = Label(self,text ="Nájdite skóre sentimentu svojej vety") #Find the Sentiment Score of your sentence!
        self.instruction.grid(row=0, column=0, columnspan = 2, sticky= W)

        self.sentence = Label(self, text = " Zadajte vetu:") #Enter a sentence:
        self.sentence.grid(row=1, column=0, sticky=W)

        self.entry = Entry(self)
        self.entry.grid(row = 1, column=1,sticky=W)

        self.submit_button= Button(self,text="Predložiť", command=self.reveal) #submit
        self.submit_button.grid(row=2, column=0, sticky = W)

        self.text = Text(self,width=35,height = 5, wrap = WORD)
        self.text.grid(row=3, column = 0, columnspan = 2, sticky = W)

        self.clear_button = Button(self, text = "Jasný text" ,command =self.clear_text) #Clear text
        self.clear_button.grid(row=2, column=1, sticky=W)
        
    def reveal(self):
        self.text = Text(self,width=35,height = 5, wrap = WORD)
        self.text.grid(row=3, column = 0, columnspan = 2, sticky = W)
        
        
        response = predict_response(response=[self.entry.get()])
       
        message = (response)
       
        self.text.insert(0.0," Toto je sentiment\n" + str(message)+ "\n ") # This is the sentiment
            
    def clear_text(self):
        self.text = Text(self,width=35,height = 5, wrap = WORD)
        self.text.grid(row=3, column = 0, columnspan = 2, sticky = W)
        
        

root = Tk()
root.title("Analýza sentimentu ") #

app = Application(root)

root.mainloop()        