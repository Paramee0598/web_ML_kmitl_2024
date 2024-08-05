import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt
import numpy as np
import base64
st.set_page_config(
    page_title="Introduction",
    page_icon="🩸",
    layout = "wide",

)

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

col1, col2, col3 = st.columns(3)


st.markdown("""
    <div class="custom-div">
        <p class="big-font text-align-center">Predict Dengue Fever</p>
        <p class="big-font text-align-center">by Complete Blood Count</p>
    </div>
""", unsafe_allow_html=True)
st.header('')
st.header('', divider='red')
st.header('')

st.markdown("สวัสดีครับ นี่จะเป็นการแนะนำสั้นๆเกี่ยวกับ โมเดลการทำนายโรคไข้เลือดออก โดยใช้ <b>ค่าผลตรวจความสมบูรณ์ของเม็ดเลือด : Complete Blood Count (CBC)</b> ", unsafe_allow_html=True)
st.write("โดยจะเป็นการกล่าวถึงเพียง ข้อมูลขาเข้า(input) และ ผลลัพธ์(result) เท่านั้น โดยรายละเอียดอื่นๆ สามารถกดดูได้ที่ลิงค์ด้านสุดเลยครับ")
st.divider()
st.header('ข้อมูลขาเข้า')
st.caption('เป็นข้อมูลที่ใช้ในการทำนายโรค')
st.write("""
-  Age : อายุ
-  Gender : เพศ
-  Hemoglobin (HGB): เป็นโปรตีนในเม็ดเลือดแดงที่มีหน้าที่นำพาออกซิเจนไปเลี้ยงอวัยวะต่างๆ ทั่วร่างกาย
-  White Blood Cell Count (WBC) : จำนวนเซลล์เม็ดเลือดขาว
-  Platelets (PLT) : จำนวนเกล็ดเลือด
-  Hematocrit : ค่าร้อยละของปริมาตรเม็ดเลือดแดงต่อปริมาตรเลือดทั้งหมด
-  Neutrophil : เป็นเม็ดเลือดขาวชนิดหนึ่งที่มีหน้าที่ต่อสู้กับแบคทีเรีย
-  Monocyte : เป็นเม็ดเลือดขาวชนิดหนึ่ง มีหน้าที่สำคัญในระบบภูมิคุ้มกันของร่างกาย ทำหน้าที่หลักในการกำจัดสิ่งแปลกปลอม และเนื้อเยื่อที่เสียหาย
""")
st.divider()
st.header('ผลลัพธ์') 
st.caption('เป็นผลลัพธ์ของการทำนายถึงเลือดของผู้ที่ถูกตรวจว่าเสี่ยงที่จะเป็นโรคต่างๆหรือไม่')
st.write("""
-  ผู้ที่มีเลือดที่เป็นโรคโลหิตจาง : Anemia
-  ผู้ที่มีเลือดที่เป็นโรคไข้เลือดออก : Dengue
-  ผู้ที่มีเลือดที่เสี่ยงจะติดเชื้อในกระแสเลือด : Probable CAB
-  ผู้ที่อยู่ในภาวะติดเชื้อในกระแสเลือด : Confirmed CAB
-  ผู้ที่มีผลลัพธ์ของเลือดที่ปกติ : Normal
""")

st.header('', divider='grey')
url = "https://www.streamlit.io"
st.write("*สามารถอ่านรายละเอียดทั้งหมดได้ที่ [Medium : 🤖🧠⚙สร้างโมเดล Machine Learning ง่ายๆ จากผลตรวจเลือด!!🩸](%s)" % url)
st.caption('This website is part of the course KMITL Machine learning 2/2566. ')



