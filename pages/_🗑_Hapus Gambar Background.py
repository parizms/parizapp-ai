import streamlit as st
from rembg import remove
from PIL import Image
from io import BytesIO
import base64

st.set_page_config(layout="wide", page_title="Hapus Background Gambar")

st.write("Hapus Background Gambar")
st.write(
    ":cat: Coba unggah gambar untuk melihat latar belakang dihapus secara ajaib. Gambar berkualitas penuh dapat diunduh dari sidebar. Informasi lebih lanjut tentang aplikasi ini bisa hubungi saya melalui website [www.bacaris.xyz](https://www.bacaris.xyz/) ."
)
st.sidebar.write("## Upload and download :gear:")


# Download the fixed image
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im


def fix_image(upload):
    image = Image.open(upload)
    col1.write("Gambar Sebelumnya :camera:")
    col1.image(image)

    fixed = remove(image)
    col2.write("Gambar Sesudah hapus background :wrench:")
    col2.image(fixed)
    st.sidebar.markdown("\n")
    st.sidebar.download_button("Download Gambar ini dengan background yang sudah di remove", convert_image(fixed), "fixed.png", "image/png")


col1, col2 = st.columns(2)
my_upload = st.sidebar.file_uploader("Upload Gambar", type=["png", "jpg", "jpeg"])

if my_upload is not None:
    fix_image(upload=my_upload)
else:
    fix_image("poto.png")


hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)