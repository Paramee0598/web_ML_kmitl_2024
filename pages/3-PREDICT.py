import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt
import numpy as np
import base64
import hydralit_components as hc
import pickle
import time

st.set_page_config(
    page_title="Predict",
    page_icon="🤖",
    layout = "wide",

)

#Define Functions 
def style_negative(v, props=''):
    """ Style negative values in dataframe"""
    try: 
        return props if v < 0 else None
    except:
        pass

def style_positive(v, props=''):
    """Style positive values in dataframe"""
    try: 
        return props if v > 0 else None
    except:
        pass    

@st.cache_data
def lond_model():
    with open('model/best_entropy_model.pkl', 'rb') as f:
        best_entropy_model = pickle.load(f)
    with open('model/best_gini_model.pkl', 'rb') as f:
        best_gini_model = pickle.load(f)
    
    return best_entropy_model , best_gini_model

@st.cache_data
def lond_data():
    df_test = pd.read_csv("dataset/Data_test_non_stdScaler.csv") 
    df_avg = pd.read_csv("dataset/Data_df_non_stdScaler.csv")
    return df_test,df_avg
    




with hc.HyLoader('Loading Model Please waite...',hc.Loaders.standard_loaders,index=5):
#    best_entropy_model = lond_model()
    best_entropy_model , best_gini_model = lond_model()
    df_test,df_avg = lond_data()

st.title(f'Prediction Model')
option_sidebar = {"Entropy","Gini" }
add_model_bar = st.selectbox('Model Type :',option_sidebar,index=None,placeholder = "(Defaults  : Entropy)")


if add_model_bar == "Entropy":
    model_predict = best_entropy_model
    #m = add_model_bar
elif add_model_bar == "Gini":
    model_predict = best_gini_model
    #m = add_model_bar
else:
    model_predict = best_entropy_model
    #m = "Entropy"


# ฟังก์ชันทำนาย
def predict(age, hgb, wbc, plt, neutro, mono, sex):
    sex_female = 1 if sex == 'female' else 0
    sex_male = 1 if sex == 'male' else 0
    
    input_data = {
        'Age': [age],
        'HGB': [hgb],
        'WBC': [wbc],
        'PLT': [plt],
        'Neutro': [neutro],
        'Mono': [mono],
        'Sex_female': [sex_female],
        'Sex_male': [sex_male]
    }
    input_df = pd.DataFrame(input_data)
    
    y_pred_input = model_predict.predict(input_df)
    return y_pred_input
check_chart = False

with st.form(key='prediction_form'):
    col3, col4 , colx = st.columns(3)

    with col3:
        age = st.text_input('Age:', value='0')
        sex = st.selectbox('Sex:', ['Male', 'Female'])
        if sex == "Male":
            sex = "male"
        elif sex == "Female" :
            sex = "female"
        else :
            pass


        


    with col4:
        hgb = st.text_input('HGB:', value='0.0')
        neutro = st.text_input('Neutro:', value='0.0')

    
    with colx:
        mono = st.text_input('Mono:', value='0.0')
        wbc = st.text_input('WBC:', value='0.0')


    col5 , coly  = st.columns([0.3, 0.7])

    with col5:
        plt = st.text_input('PLT:', value='0.0')
        submitted = st.form_submit_button('Predict',use_container_width = True)
        st.markdown(f"<p style=' '>Result : </p>", unsafe_allow_html=True)



        if submitted:
            def validate_and_convert(input_value, input_name):
                try:
                    value = float(input_value)
                    if value <= 0:
                        return None, f"กรุณาป้อนค่าที่ถูกต้องสำหรับ {input_name}"
                    return value, None
                except ValueError:
                    return None, f"กรุณาป้อนค่าที่ถูกต้องสำหรับ {input_name}"
                
            def validate_age_and_convert(input_value, input_name):
                try:
                    value = float(input_value)
                    if value <= 0:
                        return None, f"กรุณาป้อนค่าที่ถูกต้องสำหรับ {input_name}"
                    elif value > 89:
                        return None, f"ขออภัย อายุของท่านเกินกว่าขอบเขตของข้อมูล กรุณาป้อนค่าอายุไม่เกินที่ 89 ปี "
                    return value, None
                except ValueError:
                    return None, f"กรุณาป้อนค่าที่ถูกต้องสำหรับ {input_name}"
            


            age, age_error = validate_and_convert(age, 'Age')
            hgb, hgb_error = validate_and_convert(hgb, 'HGB')
            wbc, wbc_error = validate_and_convert(wbc, 'WBC')
            plt, plt_error = validate_and_convert(plt, 'PLT')
            neutro, neutro_error = validate_and_convert(neutro, 'Neutro')
            mono, mono_error = validate_and_convert(mono, 'Mono')


            errors = [age_error, hgb_error, wbc_error, plt_error, neutro_error, mono_error]
            errors = [error for error in errors if error is not None]

            if errors:
                for error in errors:
                    st.error(error)
            else:
                y_pred_input = predict(age, hgb, wbc, plt, neutro, mono, sex)

                result = ''
                if y_pred_input.size > 0:
                    if y_pred_input[0, 0]:
                        #result = 'คุณเป็นโรคโลหิตจาง'
                        result = 'Anemia.'
                        check_chart = True


                    elif y_pred_input[0, 1]:
                        #result = 'คุณมีภาวะติดเชื้อในกระแสเลือด'
                        result = 'Confirm Bloodstream Infection.'
                        check_chart = True


                    elif y_pred_input[0, 2]:
                        #result = 'คุณเป็นโรคไข้เลือดออก'
                        result = 'Dengue.'
                        check_chart = True


                    elif y_pred_input[0, 3]:
                        #result = 'คุณไม่เป็นโรคใดๆ'
                        result = 'Normal.'
                        check_chart = True
                        


                    elif y_pred_input[0, 4]:
                        #result = 'คุณเสี่ยงที่จะติดเชื้อในกระแสเลือด'
                        result = 'Probably Bloodstream Infection.'
                        check_chart = True
                        

                    else :
                        #result = 'ข้อมูลไม่ถูกต้อง โปรดตรวจสอบอีกครั้ง'
                        result = 'Worng data Please check again.'
                        check_chart = False


                else:
                    #result = 'คุณไม่เป็นโรคใดๆ'
                    result = 'Normal'
                    check_chart = True

                
                st.markdown(f"<h4 style='text-align: center; margin-top: -55px;margin-right: -30px'>{result}</h4>", unsafe_allow_html=True)


    with coly:
        st.caption("Data for Test (can scroll.)")
        st.dataframe(df_test,use_container_width  = True ,height =140 , hide_index=True)






        






# ฟังก์ชันเพื่อแบ่งช่วงอายุ
def get_age_group(age):
    if age <= 0:
        raise ValueError("Age cannot be negative")
    elif age <= 18:
        return '0-18'
    elif age <= 25:
        return '19-25'
    elif age <= 30:
        return '26-30'
    elif age <= 40:
        return '31-40'
    elif age <= 50:
        return '41-50'
    elif age <= 60:
        return '51-60'
    else:
        return '61+'

# ฟังก์ชันเพื่อกรอง DataFrame ตามช่วงอายุและเพศ
def filter_df_by_age_sex(df, age, sex):
    # กรองเฉพาะแถวที่มีค่า Diagnosis เป็น "normal"
    df_normal = df[df['Diagnosis'] == 'normal']
    
    # หาช่วงอายุที่ตรงกับ input_age
    age_group = get_age_group(age)
    
    # สร้างช่วงอายุที่คุณต้องการ
    age_bins = [0, 18, 25, 30, 40, 50, 60, float('inf')]
    age_labels = ['0-18', '19-25', '26-30', '31-40', '41-50', '51-60', '61+']

    # สร้างคอลัมน์ใหม่เพื่อระบุช่วงอายุใน DataFrame ที่กรองแล้ว
    df_normal['AgeGroup'] = pd.cut(df_normal['Age'], bins=age_bins, labels=age_labels, right=False)
    
    # กรองตามช่วงอายุและเพศ
    filtered_df = df_normal[(df_normal['AgeGroup'] == age_group) & (df_normal['Sex'] == sex)]
    return filtered_df





if check_chart == True :
    # สร้าง DataFrame โดยใช้ค่า scalar และระบุจำนวนแถวที่ต้องการ
    data_input = {
        'Age': [age] * 1,
        'Sex': [sex] * 1,
        'HGB': [hgb] * 1,
        'WBC': [wbc] * 1,
        'PLT': [plt] * 1,
        'Neutro': [neutro] * 1,
        'Mono': [mono] * 1
    }
    df_data_input = pd.DataFrame(data_input)
    compare_df = filter_df_by_age_sex(df_avg, age, sex)  # input => age,sex
    range_age = compare_df['AgeGroup']
    compare_df = compare_df.drop(columns=["AgeGroup","Diagnosis","HCT","Age","Sex"])
    df_data_input = df_data_input.drop(columns=["Age","Sex"])

    diff_df = (df_data_input.mean()) - (compare_df.mean())
    diff_df = pd.DataFrame(diff_df, columns=['Mean Difference'])
        # หาค่าเฉลี่ยและปัดทศนิยม 1 ตำแหน่ง
    df_data_input_mean = df_data_input[['HGB', 'WBC', 'PLT', 'Neutro', 'Mono']].mean().round(1)
    compare_df_mean = compare_df[['HGB', 'WBC', 'PLT', 'Neutro', 'Mono']].mean().round(1)
    print(df_data_input_mean)


    def calculate_percent_difference(parameter):
        try:
            # ดึงค่าของ User และ Normal People สำหรับพารามิเตอร์ที่ระบุ
            user_value = df_data_input_mean.loc[parameter]
            normal_value = compare_df_mean.loc[parameter]
            
            # คำนวณผลต่าง
            difference = user_value - normal_value
            
            # คำนวณเปอร์เซ็นต์ที่แตกต่าง
            percent_difference = (difference / normal_value) * 100
            
            return percent_difference
        except KeyError:
            return f"Parameter '{parameter} ' not found in DataFrame."
        except ZeroDivisionError:
            return "Cannot calculate percent difference due to division by zero."

    # สร้าง DataFrame จากค่าเฉลี่ยที่แยกแยะตามคอลัมน์
    mean_data = pd.DataFrame({
        'You': df_data_input_mean.values,
        'Normal People': compare_df_mean.values
    }, index=df_data_input_mean.index)

    # เปลี่ยนชื่อ Index ของ DataFrame
    mean_data.index.name = 'Parameter'

    # แสดงผลลัพธ์
    #st.dataframe(mean_data.loc['HGB'])   


    st.markdown(f"<h2 style=''>Analysis ({range_age.unique()[0]} year)</h2>", unsafe_allow_html=True)
    #st.markdown(f"<h2 style=''> </h2>", unsafe_allow_html=True)
    st.caption("The average is compared to normal people in your chosen age range.")



    col5, col6 ,col7 = st.columns(3)


    with col5:
        mono_g = calculate_percent_difference('Mono')
        st.metric("Mono", mean_data.loc['Mono', 'You'], f'{mono_g.round(1)} %')
        st.bar_chart(mean_data.loc[['Mono']].transpose(),horizontal=True )



    with col6:

        hgb_g = calculate_percent_difference('HGB')
        st.metric("HGB", mean_data.loc['HGB', 'You'], f'{hgb_g.round(1)} %')
        st.bar_chart(mean_data.loc[['HGB']].transpose(),horizontal=True )




    with col7:
        neutro_g = calculate_percent_difference('Neutro')
        st.metric("Neutro", mean_data.loc['Neutro', 'You'], f'{neutro_g.round(1)} %')
        st.bar_chart(mean_data.loc[['Neutro']].transpose(),horizontal=True )


    col8, col9 = st.columns(2)



    with col8:
        st.divider()
        wbc_g = calculate_percent_difference('WBC')
        st.metric("WBC", mean_data.loc['WBC', 'You'], f'{wbc_g.round(1)} %')
        st.bar_chart(mean_data.loc[['WBC']].transpose(),horizontal=True )




    with col9:
        st.divider()
        plt_g = calculate_percent_difference('PLT')
        st.metric("PLT", mean_data.loc['PLT', 'You'], f'{plt_g.round(1)} %')
        st.bar_chart(mean_data.loc[['PLT']].transpose(),horizontal=True )


else :
    pass

st.header('', divider='grey')
url = "https://www.streamlit.io"
st.write("*Read all the details [Medium : 🤖🧠⚙สร้างโมเดล Machine Learning ง่ายๆ จากผลตรวจเลือด!!🩸](%s)" % url)
st.caption('This website is part of the course KMITL Machine learning 2/2566. ')
