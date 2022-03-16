import numpy as np
from numpy import array
import pandas as pd
from keras.applications.inception_v3 import InceptionV3
from pickle import dump, load
import matplotlib.pyplot as plt
from keras.models import Model
from keras.preprocessing import image

from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
from keras.applications.inception_v3 import preprocess_input

def preprocess(image_path):
    img = image.load_img(image_path, target_size=(299, 299))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    return x

def encode(image):
    image = preprocess(image) # preprocess the image
    fea_vec = model_new.predict(image) # Get the encoding vector for the image
    fea_vec = np.reshape(fea_vec, fea_vec.shape[1]) # reshape from (1, 2048) to (2048, )
    return fea_vec


def text_to_dict(file_name):
    file = open("{}.txt".format(file_name), "r")
    return eval(file.read())


    

wordtoix = text_to_dict('/home/aravind/volume/final_project/Assisting_blind_ppl/blind_ppl/webapp/model/wordtoix')
ixtoword = text_to_dict('/home/aravind/volume/final_project/Assisting_blind_ppl/blind_ppl/webapp/model/ixtoword')


def imageSearch(photo):
    in_text = 'startseq'
    for i in range(34):
        sequence = [wordtoix[w] for w in in_text.split() if w in wordtoix]
        sequence = pad_sequences([sequence], maxlen=34)
        yhat = model.predict([photo,sequence], verbose=0)
        yhat = np.argmax(yhat)
        word = ixtoword[yhat]
        in_text += ' ' + word
        if word == 'endseq':
            break
    final = in_text.split()
    final = final[1:-1]
    final = ' '.join(final)
    return final




model = load_model('/home/aravind/volume/final_project/Assisting_blind_ppl/blind_ppl/webapp/model/model_weights/model_149.h5')
pred_image="/home/aravind/volume/final_project/Assisting_blind_ppl/blind_ppl/webapp/static/images/image.jpg"


modell = InceptionV3(weights='imagenet')
model_new = Model(modell.input, modell.layers[-2].output)


gen_caption = imageSearch(encode(pred_image).reshape((1,2048)))

