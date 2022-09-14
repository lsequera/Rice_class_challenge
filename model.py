import numpy as np
import tensorflow as tf

from tensorflow.keras.models import load_model

class Model:
    #Loading pre-trained model
    
    def preprocess(self, file_path):
        img = tf.keras.preprocessing.image.load_img(file_path, target_size=(128,128))
        img_norm = tf.keras.preprocessing.image.img_to_array(img)
        img_f = np.array([img_norm])
        return img_f
    
    def predict(self, file_path):
        model_path = './Rice_model_Alexnet.h5'
        model = load_model(model_path)
        x = model.predict(self.preprocess(file_path))
        y = np.argmax(x[0])
        return y
