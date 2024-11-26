import streamlit as st

def web_gen (header, image, info):

    st.set_page_config(layout='wide')

    ### Page

    st.title(header)
    st.image(image)
    st.write(info)

