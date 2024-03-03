from turtle import window_width
from matplotlib import image
from matplotlib.font_manager import weight_dict
import streamlit as st
import cv2
import mediapipe as mp
import numpy as np
import tempfile
import time
from PIL import Image
from streamlit_webrtc import webrtc_streamer

st.title('Pose2Play: Revolutionizing Gaming with Real-time Pose Detection')
st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        width: 350px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        width: 350px;
        margin-left: -350px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.sidebar.title('Pose2Play Sidebar')
st.sidebar.subheader('Parameters')

@st.cache()
def image_resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image

    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)

    else:
        r = width / float(w)
        dim = (width, int(h * r))

    # Resize the image
    resized = cv2.resize(image, dim, interpolation=inter)
    return resized
app_mode=st.sidebar.selectbox('Choose the app mode',
                              ['Home','Game','About Website','About us'])

if app_mode == 'Game' :
    st.header("Webcam Live Feed")
    st.markdown('Click on the play button to start live webcam and Enjoy the Game!')
    webrtc_streamer(key="example", video_transformer_factory=VideoTransformer)

if app_mode=='About App':
    st.markdown('In this Application we are using Mediapipe for creating game automation app. So that one can have a real experience of having fun while playing game ')
st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        width: 350px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        width: 350px;
        margin-left: -350px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

if app_mode=='About us':

# Displaying an image with smaller size
    st.image("k1.jpg", caption="Code Breakers", width=350)

    st.markdown('We team codebreakers - 404')