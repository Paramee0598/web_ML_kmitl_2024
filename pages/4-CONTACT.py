import streamlit as st 
from constant import *
import requests


st.set_page_config(page_title="Contacts", 
                   page_icon="🌏",
layout = "wide") #layout="wide"


# iamge ID
file_id = "1E6h8JymcUCpWOnTd0JSaTrrYwo9o7vMz=w1592-h786-iv1"

# URL
url = f"https://lh3.googleusercontent.com/fife/ALs6j_EbX_k8EcUbmRKTXEcHL4B4_oMv6hLKqCTTS67NmZ_7L91bQXrYcM4Ps_CjJukLq-kA8AokBBsts4anqmfuck8gYS33OB2LuvOHqIq2mqN9LAVbnOoutotGPHVnB4OWxAcxK_i_9IUQ-wZ4-bIvCZtBAsqLUEvRrU_dGA7ZKZxPfg5zmDkXbCUjII_o_9E2MMhJazU82s2_L9I8kO5tqSMYY4w0VFoArzYSCZNJC8nzLvs6Pavvwh5OXZ8a5ljsJauVHWXIfCVvPkEujtvAlAk33qdxi1m8-0DZYpB1yU18D92f54Ix6MkVgEPr1AK7W5U3v2x-ijI230HinFfbXdRHghMiI6KSOQ4a2wSt-7vBvxpqlwoRQ8iGhegEoMpp4r_YI3VA7AIW-ioThD0b7YGj6rbduSM9wnH8gcw4V94vND-T6mTnphEK6Uj9wRHwX7h4gwSTRCAxWi9t7IihLboGEYtOsrUpm0ow1JePklkZGzZnmH40H1l8EeplUVX7A9pcEBTH58Vd0pVLbb7IaTJl4cDkyDUEz58pPHJ7w66eUKAlmBTdW59OtnlVs19TRYxpKRjpZc29A3OSiVdTGHPmDCJde5lKgXrNHNee9RZXgJjGfDhfOR3T_izEQ8biQBAybp55ktbTXFAY4LkAm140BdMeCwqUjrZ_DPRXdKD5A6Ts2X0pWTYLtamGG_slbcbe3xgMlOtb51WwsFL3srgqI9LOzy0ZnuEOwfFAmaGWLB4aiZ5NpEMs3lwi1fPkhXHZ2tEsjqQCTcqNbCWhU7giTPelzHOeYX6QMYl4qNjFj-ADWCZJSQNOG-UrTLlgERN82oEFSwPtfssdiSja9Q_c5qA_hf08S-kx6wCrZdfFdK_zMD4HqgJcszLzRtCPtX7tGRZ90lIEo40sqUa5lQv4esWo4ArSkS_Pg_Xw7UucbDnIQrlNDrYbWsoepXLb1MkfdZgYu7NiFstjcTVvYEgYXUOvzgfz4iex44K2O0gxK6jPC29b_Bf_F1Y70yrs6PxyW-ZzKnxLcry5EXE-z9pRbVlHoFdPEXaL3du6g6GtUeS2EIriRE7TE_WwflhGo6aQ30X9oBv1jTkShc-gKfZXbAGLUUN-hOjkUxd8_R3VELyHeH24XyrBlJGUlKONCTlyFh3_TE31V-4YhJWdbJ880NwU4ot2xbCwP_Ov8zKKTeBBDbTLgBDo4Vo3WdJ2pm4f6HAX-vcmijxQhYLcGRfOGHAWJ4W0iBBfZRwvFPpDrfcNnPjadGn3CuCT_eJNDZEEd-F0-RHsZbq9xiPmwOZ3MMi6o6JBWB2LzqnQc5D5oAJNw4SYMs5QZgdqKI54Nm70Q91m5Dz7-xCsnBOLQ3pJsNrlUdmMLwx02fjwPwUsxkKm7heVnk8o84XwGn3zFhJo_ppKznei4zejaiQJdbxxfhdlGQLt1-yX3j8ibU6VDMXJPRLD1hlejAPOZPjBhA58zpibBh3Y8y2iRcwULVk2fPq-VrTnOjiWGIRBkL3HtRaV4RwgQpj9XPP8gwLH67VRt97EdKlD5mW-Qo8F9YBO6CUrziD3vPsg_T3l6tQAQC3tnIhYQmg-v4hd2wKGbqJivaSo0pS6Jbyo-Qz7B2HMQ-_idjvYQeLTO3B5d_vStcmrlivzF1b2miKhv2EmCXUIlbmxiErlnU9ks3OV62zrg0wVSA=w1592-h786"

response = requests.get(url)
st.image(response.content,width=200)

st.markdown(f"  MR. PARAMEE CHUMSRI")
st.markdown(f"  Bachelor's degree, Computer Engineering")
st.markdown(f"  King Mongkut's Institute of Technology Ladkrabang")

st.markdown(f" 📞 Phone:  {phone}")   
st.markdown(f" ✉️ Email:   {email}")

with st.container():
    col1, col2 = st.columns([0.1, 3])
    with col1:
        st.write(linkedin_logo, unsafe_allow_html=True)
    with col2:
        st.markdown(f"  Linkedin: {linkedin_link}")
with st.container():
    col1, col2 = st.columns([0.1, 3])
    with col1:
        st.write(github_logo, unsafe_allow_html=True)
    with col2:
        st.markdown(f"  Github: {github_link}")

st.caption('This website is part of the course KMITL Machine learning 2/2566. ')
