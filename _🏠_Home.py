import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Risenha",
)


# Title
st.title('Selamatkan Datang di Website Ris')

# Content
c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15 = st.columns(15)
c1.image(Image.open('images/html.png'))
c2.image(Image.open('images/css.png'))
c3.image(Image.open('images/js.png'))
c4.image(Image.open('images/php.png'))
c5.image(Image.open('images/laravel.png'))
c6.image(Image.open('images/bootstrap.png'))
c7.image(Image.open('images/mysql.png'))
c8.image(Image.open('images/python.png'))
c9.image(Image.open('images/vscode.png'))
c10.image(Image.open('images/excel.png'))
c11.image(Image.open('images/word.png'))
c12.image(Image.open('images/pp.png'))
c13.image(Image.open('images/canva.png'))
c14.image(Image.open('images/filmora.png'))
c15.image(Image.open('images/stream.png'))

st.write(
    """
    Website Ris Merupakan website yang bisa membantu anda melakukan apapun dengan mudah. Alat ini dirancang untuk memungkinkan pemirsa melakukan pekerjaan dengan mudah.
    Alat ini dirancang dan disusun dalam beberapa Halaman yang dapat diakses menggunakan sidebar atau samping kiri halaman. 
    Masing-masing Halaman ini mempunyai segmen atau fungsi tersendiri sesuai dengan keperluan anda yang berbeda.
    Seperti ( Menghapus background gambar, mengubah audio menjadi teks, mengubah teks menjadi audio, filter gambar menjadi karakter anime dll)
    
    Anda bisa melakukan penggunaan aplikasi kapan pun dan dimana pun😊
    """
)

st.subheader('Methodology')
st.write(
    """
    Aplikasi ini dirancang menggunakan Bahasa Pemrograman Python dan framework python streamlit. 
    Dengan menggunakan kerangka kerja ini, pengembang dapat mempercepat proses pengembangan dan membuat aplikasi web yang lebih skalabel, mudah dipelihara, dan lebih aman.
    Python menjadi bahasa pemrograman yang sangat populer, terutama dengan dukungan dari berbagai perpustakaan analisis data seperti Pandas, NumPy, SciPy, Matplotlib, dan sebagainya.

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris vel libero euismod, eleifend ex quis, fermentum leo. 
    Duis pharetra dui vel purus iaculis malesuada. Fusce dictum scelerisque enim, ac elementum libero facilisis at. 
    Sed ultricies magna in elit maximus lacinia. Maecenas convallis magna nec purus tristique, non malesuada quam vestibulum. 
    Nulla tincidunt posuere diam euismod posuere. Sed eget enim vel tellus interdum pharetra id id dui. Fusce vitae posuere sapien. 
    Maecenas vel ligula ac lectus rutrum venenatis. Nulla facilisi. Aenean consectetur quis ipsum in bibendum. 
    In auctor orci ac libero posuere facilisis. Suspendisse interdum sapien eu augue ultricies aliquam.
    """
)

st.subheader('Future Works')
st.write(
    """
    Aplikasi ini sedang dalam proses dan akan terus dikembangkan ke depannya.
    Menambahkan fungsi lain yang nantinya bisa membantu anda dalam pekerjaannya.
    Kami akan mengoptimalkan kode secara umum, meningkatkan UI/UX, dan yang lebih penting, meningkatkan performa website adalah salah satu prioritas utama untuk pengembangan aplikasi ini. 
    Jangan ragu untuk membagikan masukan, saran, dan juga kritik Anda kepada saya.

    """
)


c1, c2, c3 = st.columns(3)
with c1:
    st.info('**Instagram: [@Pariz_ms](https://www.youtube.com/)**', icon="💡")
with c2:
    st.info('**GitHub: [@parizms](#)**', icon="💻")
with c3:
    st.info('**Facebook: [Parizs](#)**', icon="📲")

    hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
