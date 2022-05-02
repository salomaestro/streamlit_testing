import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image

left, right = st.columns(2)

left.header("Original")
right.header("Kontrast og skarphet")

@st.cache
def load_data():
    img = Image.open('imgs/original.JPG')
    img2 = Image.open('imgs/sharpened.png')
    weird1 = Image.open('imgs/segmented_-2_3000.png')
    weird2 = Image.open('imgs/segmented_-2_5000.png')

    return img, img2, weird1, weird2

img, img2, weird1, weird2 = load_data()

left.image(img, caption='Johanne tok med Christian til Paris, det var gøy!', use_column_width=True)
right.image(img2, caption="La på noen filter.", use_column_width=True)


left.image(weird1, caption="segmentert comp=10^-2, segmenter=3000", use_column_width=True)
right.image(weird2, caption="segmentert comp=10^-2, segmenter=5000", use_column_width=True)