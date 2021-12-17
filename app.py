### 데이터 분석 라이브러리 ##########
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
### 파일 입출력 라이브러리 ##########
import joblib
### 내부 파일 ##########
from eda_app import run_eda_app
from ml_app import run_ml_app

#####
def main():
    menu = ['홈', '데이터분석', '인공지능']
    menu_sel = st.sidebar.selectbox('메뉴', menu)

    st.title ('당뇨병 데이터 분석 및 예측')

    # 메뉴 홈
    if menu_sel == menu[0]:
        st.subheader('개요')
        st.write ('당뇨병 환자들의 데이터를 분석하고')
        st.write ('인공지능을 통해 당뇨병 의심 여부를 확인할 수 있습니다.')

    # 메뉴 데이터분석
    elif menu_sel == menu[1]:
        run_eda_app()

    # 메뉴 인공지능
    elif menu_sel == menu[2]:
        run_ml_app()

if __name__ == '__main__':
    main()

