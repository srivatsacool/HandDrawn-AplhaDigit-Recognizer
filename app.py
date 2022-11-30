import pandas as pd
from PIL import Image, ImageOps
import streamlit as st
from streamlit_drawable_canvas import st_canvas
import matplotlib.pyplot as plt
import numpy as np
from numpy import argmax
from tensorflow.keras.utils import load_img
from tensorflow.keras.utils import img_to_array
from keras.models import load_model
import pyttsx3
    

#engine = pyttsx3.init()
st.image("example1.png")
st.image("example2.png")
# Create a canvas componentI
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
    stroke_width=15,
    stroke_color="white",
    background_color='#000000',
    update_streamlit=True,
    height=400,
    width=400, 
    background_image = Image.open("number_5.png"),
    drawing_mode="freedraw",
    key="canvas",
)

# Do something interesting with the image data and paths
if canvas_result.image_data is not None:
    st.image(canvas_result.image_data)
    print(canvas_result.image_data)
    print(canvas_result.image_data.shape)
    img = Image.fromarray(canvas_result.image_data)
    img = ImageOps.grayscale(img)
    img.save("pil.png")


def load_image(filename):
        # load the image
        img = load_img(filename, color_mode = "grayscale", target_size=(28, 28))
        # convert to array
        img = img_to_array(img)
        print(img.shape)
        # reshape into a single sample with 1 channel
        img = img.reshape(1, 28, 28, 1)
        # prepare pixel data
        img = img.astype('float32')
        img = img / 255.0
        return img

# load an image and predict the class
def run_example():
        # load the image
        img = load_image('pil.png')
        # load model
        model = load_model('final_model.h5')
        # predict the class
        predict_value = model.predict(img)
        digit = argmax(predict_value)
        print(predict_value)
        print(digit)
        return digit
        
if st.button("Submit"):
    res = run_example()
    st.write(res)
    engine = pyttsx3.init()
    engine.say(f'The predicted Number is {res}.')
    engine.runAndWait()
    engine = None