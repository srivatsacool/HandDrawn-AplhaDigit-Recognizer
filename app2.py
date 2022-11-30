import streamlit as st
from PIL import Image , ImageOps
import streamlit as st
from streamlit_drawable_canvas import st_canvas
import matplotlib.pyplot as plt
import numpy as np
from numpy import argmax
from tensorflow.keras.utils import load_img
from tensorflow.keras.utils import img_to_array
from keras.models import load_model
import pyttsx3

st.set_page_config(
    page_title="Hand-drawn Alphadigit Recognizer",
    page_icon="🔤",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)
st.markdown("<h1 style='font-family: monaco, monospace;text-align: center;font-size: 70px;background: linear-gradient(to left,violet,indigo,blue,green, yellow, orange,red);-webkit-background-clip: text;color: transparent;'>Handwritten AlphaNumeric Recognizer</h1> ", unsafe_allow_html=True)

st.markdown("""<center><h2>This Project is made by :-</h2></center><br>
            <center><h3>Srivatsa Gorti E20BCA012</h3></center>
            <center><h3>Rahul E20BCA024</h3></center>
            <center><h3>Yash E20BCA022</h3></center>
            """
            , unsafe_allow_html=True)
bg_image = st.sidebar.selectbox(
    label="Any particular number you want to Draw ?",
    options=("Number_0","Number_1","Number_2","Number_3","Number_4","Number_5" , "Number_6","Number_7","Number_8","Number_9"),
)
final_image = (f"numbers/{bg_image}.png")
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
    background_image=Image.open(final_image) if final_image != "None" else None,
    drawing_mode="freedraw",
    key="canvas",
)
#st_canvas["background_image"] = Image.open("numbers/number_0.png")
# Do something interesting with the image data and paths
if canvas_result.image_data is not None:
    st.image(canvas_result.image_data)
    #print(canvas_result.image_data)
    #print(canvas_result.image_data.shape)
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
    st.success(f'This is the predicted number {res}', icon="✅")
    engine = pyttsx3.init()
    engine = pyttsx3.init()
    if res == int((bg_image).split("_")[1]):
        st.success("Correct number predicted.✅")
        engine.say(f'Well-Done the selected number and the predicted number is same . The predicted Number is {res}.')
        engine.runAndWait()
        engine = None
    else:
        st.success("Worong number predicted.❌")
        engine.say(f'Well Tried , but the selected number and the predicted number are different . The predicted Number is {res}.')
        engine.runAndWait()
        engine = None
