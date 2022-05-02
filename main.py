import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image

left, right = st.columns(2)

with left:
    st.header("Christian Salomonsen")
    st.markdown(
        """
        **Welcome to my personal website!** :wave:

        Check out my links for more information!

        - [GitHub](https://github.com/salomaestro) :link:
        - [LinkedIn](linkedin.com/in/christian-salomonsen-932923207) :link:
        
        You can also reach me through the following channels:
        - [Email](mailto:csa047@uit.no) :email:
        """
    )

with right:
    st.image("images/portrett.png")