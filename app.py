import streamlit as st
import datetime
import requests
from PIL import Image
import io

'''
# Image convertisseur front v0.0.5
'''

def convert_image(input_path, output_format):
    with Image.open(input_path) as im:
        output_buffer = io.BytesIO()
        im.save(output_buffer, format=output_format)
        output_buffer.seek(0)
        return output_buffer

pickup_format = st.selectbox('Choose your format',
    ("JPEG", "PNG", "GIF", "BMP", "TIFF", "WebP", "ICO", "PBM", "PGM", "PPM", "RGB", "RGBA", "CMYK", "YCbCr", "LAB", "HSV", "I;16", "I;16L", "I;16B", "F"))

take_file = st.file_uploader('Image uploader')

if take_file:
    if st.button('Convertir mon image'):
        transformed_img = convert_image(take_file, pickup_format)
        st.download_button(
            label="Download the converted image",
            data=transformed_img,
            file_name="converted_image.jpg",
            mime="image/jpeg"
        )
