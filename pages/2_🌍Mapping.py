import streamlit as st
import pandas as pd
import pydeck as pdk
from urllib.error import URLError

st.set_page_config(page_title="교통민원 데이터 지도 시각화",layout="wide", page_icon="🌍")

col1, col2, col3 = st.columns([1,5,2])
with col2:
    
    st.markdown("# 교통민원 데이터 지도 시각화")

    data = pd.read_csv("/Users/ksy/문서/공모전/제3회_민원데이터분석경진대회/data/민원데이터_전체통합_주소완료_1003.csv.csv")

    # Streamlit selectbox 위젯으로 CSV 파일 선택하기
    selected_csv_name = st.selectbox("Select a dataset:",data['신고유형'].unique())


    # 선택된 CSV 파일에서 데이터 로드 (위도와 경도 열이 '위도', '경도'인 경우)


    # # NaN 값 제거 

    data = data.fillna('NaN')

    layer = pdk.Layer(
        "ScatterplotLayer",
        data=data,
        get_position=["경도", "위도"],  # 주의: pydeck에서는 [경도, 위도] 순서로 입력합니다.
        get_color=[200, 30, 0, 160],
        get_radius=100,
    )

    view_state = pdk.ViewState(
        latitude=data["위도"].mean(),
        longitude=data["경도"].mean(),
        zoom=6,
        pitch=0,
    )

    # Render
    r = pdk.Deck(layers=[layer], initial_view_state=view_state)
    st.pydeck_chart(r)
