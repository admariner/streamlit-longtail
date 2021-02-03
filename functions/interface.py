import streamlit as st
import streamlit.components.v1 as components
from time import sleep
from stqdm import stqdm
import base64

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
        body {
            background-image: url("data:image/png;base64,%s");
            background-size: cover;
        }
    </style>
    ''' % bin_str

    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

def progress_bar(range_size, sleep_size):

    for _ in stqdm(range(range_size), desc="This is a slow task, please be patient"):
        sleep(sleep_size)
    return

def balloons(result):
    st.balloons()
    st.text('Done! thanks for being patient.')
    st.text("Here's your " + result)
    return
