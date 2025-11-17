import streamlit as st
import pandas as pd
import pydeck as pdk
import plotly.express as px
import altair as alt

# -----------------------
# Sidebar 구성
# -----------------------
st.sidebar.title("📌 설정 메뉴")

# 1) 선택 박스
chart_type = st.sidebar.selectbox(
    "그래프 종류 선택",
    ["Line", "Bar", "Area"]
)

# 2) 슬라이더
count = st.sidebar.slider(
    "데이터 개수",
    min_value=5,
    max_value=50,
    value=20
)

# 3) 체크박스
show_table = st.sidebar.checkbox("데이터 테이블 보기")

# -----------------------
# 메인 화면
# -----------------------
st.title("📊 사이드바 인터랙티브 데모")

# 랜덤 데이터 생성
df = pd.DataFrame({
    "x": list(range(count)),
    "y": [v * 2 for v in range(count)]
})

# Plotly 그래프 생성
if chart_type == "Line":
    fig = px.line(df, x="x", y="y", markers=True)
elif chart_type == "Bar":
    fig = px.bar(df, x="x", y="y")
else:
    fig = px.area(df, x="x", y="y")

st.plotly_chart(fig, use_container_width=True)

# 테이블 표시 옵션
if show_table:
    st.subheader("📄 데이터 테이블")
    st.dataframe(df)

st.title("🌏 PyDeck 3D 지도")

df = pd.DataFrame({
    'lat': [37.5665, 35.1796, 35.8714],
    'lon': [126.9780, 129.0756, 128.6014],
    'value': [10, 30, 20]
})

layer = pdk.Layer(
    'ScatterplotLayer',
    data=df,
    get_position='[lon, lat]',
    get_radius=5000,
    get_color='[200, value*10, 100]',
    pickable=True
)

view_state = pdk.ViewState(
    latitude=36.5,
    longitude=127.8,
    zoom=6
)

st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state))

st.title("그래프연습")

# 데이터프레임
df = pd.DataFrame({
    "x": [1, 2, 3, 4, 5],
    "y": [10, 20, 5, 30, 15]
})

# Altair 그래프
chart = (
    alt.Chart(df)
    .mark_line(point=True)
    .encode(
        x="x:Q",
        y="y:Q"
    )
)

st.altair_chart(chart, use_container_width=True)
