import streamlit as st
from PIL import Image

img_ardi = Image.open(r"ardi pict.jpg")
img_nara = Image.open(r"nara pict.jpg")
img_date = Image.open(r"first date.jpg")
first_foto = Image.open(r"first foto.jpg")
badminton = Image.open(r"badminton.jpg")
date = open(r"date day.mp4","rb")
ultah_nara = (r"nara's birtday.jpg")
ultah_ardi = (r"ardi's birthday.jpg")
batik_day = (r"batik day.jpg")
univday = open(r"univday.mp4","rb")
st.set_page_config(page_title="Made by Love", page_icon=":sparkles:", layout="wide")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            """

audio_file = "music.mp3"  
audio_html = f"""
<audio autoplay loop muted>
    <source src="{audio_file}" type="audio/mp3">
    Your browser does not support the audio element.
</audio>
"""
st.markdown(audio_html, unsafe_allow_html=True)
st.markdown(hide_st_style, unsafe_allow_html=True)

with st.container():
    st.title("Hallo, This is Our Website")
    st.write("Sebelum kita berpisah jarak lagi, aku mau membuat sesuatu yang bisa dengan mudah kamu liat kalo lagi kangen!!")
    st.write("Yang paling penting dari suatu hubungan ketika sedang ldr adalah saling menjaga kepercayaan and aku selalu menjaga itu!")
    st.write("Enjoyy!!")

with st.container():
    st.write("---")
    col1,col2 = st.columns(2)
    with col1:
        st.header("About Ardi")
        st.image(img_ardi)
        st.write(
            """
            Hi my name is Ardi i'm 18 y.o and now aku kuliah di Jogja. Aku ingin hidup seperti orang yang memiliki bisnis besar gitulohh like mengurus bisnis ini itu seru banget!!
            Yang paling menarik adalah kalo di film atau novel ada C-Levels yang fall in love with his secretary, i do the same things when i 17. i fall in love with my secretary.
            And i wish, my biggest wish is i want be with my secretary forever. i want to build my empire, to protect the queen (my secretary)
            """
        )
    with col2:
        st.header("About Nara")
        st.image(img_nara)
        st.write(
            """
            Haii, ini Nara! orang yang sebenarnya udah aku temui sejak SMP dia nyalonin jadi pengurus osis waktu itu gess.
            Nara sangat suka sekali musik! suka dengar musik! suka menyanyi! dan karena nara aku jadi suka musik juga loh gess aku jadi suka dewa!!
            Nara pengen nanti kalo kerja di kantor like mba mba SCBD gitu dress well, hangout sambil kerja, dan kerja di instansi pemerintahan juga suka!!!
            The important things is Nara sangat suka berbagi cerita!!! Apalagi kalo ada hot news :DD
            """
        )
st.write('---')
with st.container():
    st.title("OUR MOMENTS")
tab1, tab2, tab3, tab4, tab5, tab6,tab7, tab8 = st.tabs(['our first date','our first pict','hari aku nembak nara!','main badminton!','hari batik!',"ardi's birthday","nara's birthday",'univday!'])
with tab1:
    st.image(img_date)
with tab2:
    st.image(first_foto)
with tab3:
    st.video(date, muted=True)
with tab4:
    st.image(badminton)
with tab5:
    st.image(batik_day)
with tab6:
    st.image(ultah_ardi)
with tab7:
    st.image(ultah_nara)
with tab8:
    st.video(univday, muted=True)
