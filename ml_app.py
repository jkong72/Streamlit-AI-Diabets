import streamlit as st
import numpy as np
import pandas as pd

import joblib

def run_ml_app():
    df = pd.read_csv('Data/diabetes.csv')
    classifier = joblib.load('Data/best_model.pkl')
    scaler_X = joblib.load('Data/scaler_X.pkl')
    
    st.subheader ('인공지능 예측')
    st.write ('입력한 데이터를 바탕으로, 당뇨병 여부를 예측할 수 있습니다.')
    st.write ('예측한 결과는 실제와는 상이할 수 있습니다. 참고용으로만 사용하시고')
    st.write ('정확한 의학적 소견은 전문의와 상담을 통해 얻어야 합니다.')

    st.subheader ('자료 입력란')
    preg = st.number_input('임신횟수', min_value=0)
    glucose = st.number_input ('공복혈당 (mg/dL)', min_value=0, help='최소 지난 2시간동안 공복을 유지했을 때의 혈당')
    pressure = st.number_input ('이완기 혈압 (mm HG)', min_value=0, help='혈압기에 표시되는 혈압중 낮은 쪽이 이완기 혈압입니다.')
    skinthick = st.number_input ('피부 두께 (mm)', min_value=0)
    insulin = st.number_input ('혈청 인슐린 (mu U/ml)', min_value=0)
    height = st.number_input ('신장 (cm)', min_value = 0, help='BMI 수치를 구하기 위해 사용됩니다.')
    weight = st.number_input ('체중 (kg)', min_value=0, help='BMI 수치를 구하기 위해 사용됩니다.')
    if height != 0 and weight != 0:
        bmi = weight/((height/100)**2)  
    dia = df['DiabetesPedigreeFunction'].mean()
    # bmi = st.number_input('BMI', min_value=0)
    # dia = st.number_input('DiabetesPedigr', min_value=0)
    age = st.number_input('연령', min_value=0)
    print(dia)

    if st.button('결과 보기'):
        new_data = np.array([preg, glucose, pressure, skinthick, insulin, bmi, dia, age])

        new_data = new_data.reshape(1,new_data.size)

        new_data = scaler_X.transform(new_data)
        y_pred = classifier.predict(new_data)
        st.write(y_pred[0])

        if y_pred[0] == 0:
            st.write ('당뇨병이 의심되지 않습니다.')

        else:
            st.write ('당뇨병이 의심됩니다. 전문의와의 상담을 권장합니다.')