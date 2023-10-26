import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm 


# 폰트 파일의 위치를 지정
font_path = './font/NanumGothic-Bold.ttf'
# 폰트 프로퍼티를 생성
fontprop = fm.FontProperties(fname=font_path, size=18)

sns.set(font=fontprop.get_name())
plt.rc('font', family=fontprop.get_name())


# 외부 페이지 노출 시 표시되는 데이터
st.set_page_config(
    page_title="교통관련 데이터 시각화 갤러리",
    page_icon="⭐️",
    initial_sidebar_state="expanded"
)
col1, col2, col3 = st.columns([1,5,2])
with col2:
    st.title("🚘교통관련 데이터 시각화 갤러리")
    st.markdown(
            """
    안녕하세요~~👋

    **교통사고 민원데이터 갤러리**에 오신 것을 환영합니다!

    왼쪽 사이드 바에서 다양한 시각화를 둘러보세요~!

    """
    )
