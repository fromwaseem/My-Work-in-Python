import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import model_from_json
from tensorflow.keras.preprocessing.text import tokenizer_from_json
from tensorflow.keras.preprocessing import sequence
import numpy as np
import pickle
        
def predict_response(response):
    
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
    #print("Loading saved tokenizer...")

    # load json and create model
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()

    model = model_from_json(loaded_model_json)
    # load weights into new model
    model.load_weights('my_model.h5')
    #print("Loading saved model...")
    '''
    0 - very negative
    1 - somewhat negative
    2 - neutral
    3 - somewhat positive
    4 - very positive
    '''
    #print(f'You said: \n{response}\n')
    
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
    
# user_input = input()  // input
# response = predict_response(response=[user_input])
# print(response) 
 
from tkinter import *

root= Tk()
root.geometry('250x400')

def button():
       
    text= entry1.get() 
    text1 = predict_response(s)
  
    
    entry2.insert(0, text1)
    

entry1=Entry(root,width='50')
entry1.pack()

entry2=Entry(root,width='20')
entry2.pack()

Button(root,text="Check", command=button).pack()


root.mainloop()