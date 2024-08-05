import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt
import numpy as np
import os
import hydralit_components as hc
import time

#@st.cache
#will lond one time 
#st.header('_Streamlit_ is :blue[cool] :sunglasses:')
import base64

st.set_page_config(
    page_title="Dataset",
    page_icon="👋",
    layout = "wide",

)

@st.cache_data
def lond_data ():
    cbc_dataset_meandeley = pd.read_csv("dataset/CBC data_for_meandeley_preded.csv")  #ผู้ที่เป็น/ไม่เป็นโรค
    cbc_dataset_pregnant = pd.read_excel("dataset/Dataset for Reference Intervals of Complete Blood Count and Coagulation Tests in Vietnamese Pregnant Women.xlsx") #ท้อง
    cbc_dataset_dengue = pd.read_excel("dataset/dengue patients_data set.xlsx") #คลีนิค
    cbc_dataset_kenya = pd.read_excel("dataset/good_RRP data Kenya haematology_data repository.xlsx") #เคนย่า
    cbc_dataset_diagnoses = pd.read_csv("dataset/cbc_diagnoses_dataset_with_labels.csv") #ผ่าตัด

    return  cbc_dataset_meandeley , cbc_dataset_pregnant,cbc_dataset_dengue,cbc_dataset_kenya,cbc_dataset_diagnoses



# Set the background image
background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
    background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
    background-position: center;  
    background-repeat: no-repeat;
}
</style>
"""

#st.markdown(background_image, unsafe_allow_html=True)
input_style = """
<style>
input[type="text"] {
    background-color: transparent;
    color: #a19eae;  // This changes the text color inside the input box
}
div[data-baseweb="base-input"] {
    background-color: transparent !important;
}
[data-testid="stAppViewContainer"] {
    background-color: transparent !important;
}
</style>
"""
#st.markdown(input_style, unsafe_allow_html=True)

        
st.markdown("""
<style>
/* ตั้งค่า background image สำหรับแอป */
[data-testid="stAppViewContainer"] > .main {
    background-color: transparent !important; /* ตั้งค่าให้พื้นหลังของแอปเป็นโปร่งใส */
}

/* ตั้งค่า background image และสไตล์สำหรับ div */
.custom-div {
    background-image: url("https://ihealzy.com/wp-content/uploads/2021/09/complete-blood-count-CBC-1.jpg");
    background-size: cover; /* ทำให้ภาพพื้นหลังครอบคลุม div */
    background-position: center; /* จัดตำแหน่งภาพพื้นหลังตรงกลาง */
    background-repeat: no-repeat; /* ไม่ซ้ำภาพพื้นหลัง */
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    color: white; /* ตั้งค่าสีข้อความ */
    backdrop-filter: blur(10px); /* เพิ่มเอฟเฟกต์มัวในส่วนของภาพพื้นหลัง */
    text-shadow: -2px -2px 0 #000,  
                 2px -2px 0 #000,
                -2px  2px 0 #000,
                 2px  2px 0 #000; /* เพิ่มเอฟเฟกต์ขอบแบบ outline โดยใช้ text-shadow */
    
}

/* ตั้งค่า font และการจัดเรียงข้อความ */
.big-font {
    font-size: 50px !important;
}

.text-align-center {
    text-align: center !important;
}

/* ตั้งค่า sidebar */
section[data-testid="stSidebar"] {
    width: 70px !important;
}
</style>
""", unsafe_allow_html=True)
with hc.HyLoader('Loading Data Please waite...',hc.Loaders.standard_loaders,index=5):
    cbc_dataset_meandeley , cbc_dataset_pregnant,cbc_dataset_dengue,cbc_dataset_kenya,cbc_dataset_diagnoses = lond_data()
    time.sleep(0.7)
    
st.markdown("""
    <div class="custom-div">
        <p class="big-font text-align-center">Dataset</p>
    </div>
""", unsafe_allow_html=True)
st.header('', divider='red')
st.header('')
st.markdown("เป็นข้อมูลทั้งหมดที่ยังไม่มีการ Cleaning Data ซึ่งจะเป็นข้อมูลที่ใช้ในการสร้างโมเดลการทำนายโรคต่อไป  ", unsafe_allow_html=True)
st.write("ประกอบไปด้วยข้อมูลผลการตรวจเลือดต่างๆ ดังนี้")
st.divider()



col1, col2, col3 = st.columns(3)
col1 = col1.container(height=550)
col2 = col2.container(height=550)
col3 = col3.container(height=550)
with col1:
    
    st.markdown("""
    <div class="">
        <p class=" text-align-center"> <b>ผู้ที่เป็น/ไม่เป็นภาวะเลือดจาง</b></p>
    </div>
""", unsafe_allow_html=True)
    st.write(cbc_dataset_meandeley)
    st.caption("ผู้ที่มีเลือดปกติ และ ผู้ที่มีเลือดที่เป็นโรคเลือดจาง")

with col2:
    st.markdown("""
    <div class="">
        <p class=" text-align-center"> <b>ผู้หญิงตั้งครรภ์ที่มีสุขภาพแข็งแรง</b></p>
    </div>
""", unsafe_allow_html=True)
    st.write(cbc_dataset_pregnant)
    st.caption("""เนื่องจากผู้หญิงที่่กำลังตั้งครรภ์ อาจมีภาวะคล้ายกับผู้ที่เป็นโรคโลหิตจาง
                จึงจำเป็นต้องมีข้อมูลของผู้หญิงที่กำลังตั้งครรภ์แต่ยังคงมีสุขภาพที่แข็งแรง""")

with col3:
    st.markdown("""
    <div class="">
        <p class=" text-align-center"> <b>ชาวเคนย่าที่มีสุขภาพแข็งแรง</b></p>
    </div>
""", unsafe_allow_html=True)
    st.write(cbc_dataset_kenya)
    st.caption("ชาวเคนย่าที่เป็นผู้ที่มีสุขภาพแข็งแรงและมีค่าเลือดปกติ")

col4, col5 = st.columns(2)
col4 = col4.container(height=605)
col5 = col5.container(height=605)

with col4:
    st.markdown("""
    <div class="">
        <p class=" text-align-center"> <b>ผู้ที่เข้ารับการวินิจฉัยโรคจากคลีนิค</b></p>
    </div>
""", unsafe_allow_html=True)
    st.write(cbc_dataset_dengue)
    st.caption("""จะบอกถึงผลการวินิจฉัยโรคของผู้ตรวจที่มีภาวะการติดเชื้อในกระแสเลือด(CAB)ไปแล้ว หรือ เพียงแค่ต้องสงสัย รวมไปถึง การเป็นโรคไข้เลือดออกอีกด้วย """)
    st.caption("""*ก่อนเป็นไข้เลือดออก มักจะถูกต้องสงสัยว่าติดเชื้อในกระแสเลือดไว้ก่อน โดยที่ไข้เลือดออก กับ การติดเชื้อในกระแสเลือดจะไม่ใช่โรคเดียวกัน""")

with col5:
    st.markdown("""
    <div class="">
        <p class=" text-align-center"> <b>ผู้ที่กำลังได้รับการผ่าตัด</b></p>
    </div>
""", unsafe_allow_html=True)
    st.write(cbc_dataset_diagnoses)
    st.caption("""ค่าของเลือดต่างๆของผู้ที่ได้รับการผ่าตัด เนื่องจากโรคต่างๆ รวมไปถึงโรคที่ติดเชื้อในกระแสเลือดด้วย """)



st.header('', divider='grey')
st.write("ขั้นตอนการจัดการข้อมูลทั้งหมดดูได้ที่ [Jupyter Notebook : Data Cleaning ](%s)" % "https://github.com/Paramee0598/Machine_Learning_Project_2-2023/blob/main/data_cleaning_CBC.ipynb")
st.write("Google Colab : Data Cleaning [Link](%s)" % "https://drive.google.com/file/d/1j4Ryfr74KHhYmD5Kq2NjuaGzu7HSYU24/view?usp=sharing")
st.caption('This website is part of the course KMITL Machine learning 2/2566. ')


