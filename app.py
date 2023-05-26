import streamlit as st
import datetime
import requests
from PIL import Image
import io

'''
# Image convertisseur front v0.0.2
'''

def convert_image(input_file, output_format):
    with Image.open(input_file) as im:
        buffer = io.BytesIO()
        im.save(buffer, format=output_format)
        return buffer.getvalue()

with st.form(key='params_for_api'):

    pickup_format = st.selectbox('Choose your format',
    ("JPEG", "PNG", "GIF", "BMP", "TIFF", "WebP", "ICO", "PBM", "PGM", "PPM", "RGB", "RGBA", "CMYK", "YCbCr", "LAB", "HSV", "I;16", "I;16L", "I;16B", "F"))

    take_file = st.file_uploader('Image uploader')

    if take_file:

        transformed_img = convert_image(take_file.getvalue(), pickup_format)

        st.image(transformed_img, use_column_width=True)

        download_button = st.button(
            label="Download the converted image",
            data=transformed_img,
            file_name="converted_image"
        )

if download_button:
    st.download_button(
        data=transformed_img,
        file_name="converted_image",
        mime="image/{}".format(pickup_format.lower())  # Format the MIME type with proper extension
    )
