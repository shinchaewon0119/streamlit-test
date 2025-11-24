import streamlit as st
from PIL import Image
import streamlit as st
import pandas as pd
import numpy as np
# 출력
st.title("텍스트 & 미디어 연습")

# 일반 텍스트
st.header("일반 텍스트")
st.title("제목 : st.title()")
st.header("헤더 : st.header()")
st.subheader("서브헤더 : st.subheader()")
st.text("본문 텍스트 : st.text()")
st.markdown("## 마크다운 : st.markdown()")
st.caption("캡션(작고 흐린 글씨 표시) : st.caption()")
st.divider()

# st.write() 예시
st.header("st.write() 예시")
st.write("# 마크다운 H1 : st.write()")
st.write("### 마크다운 H3 : st.write()")
st.write("")  # 빈 줄
st.write("이모지도 가능해요 😎🔥🍀 ")
st.divider()

# 색상 있는 텍스트
st.header("색상 있는 텍스트")
st.write(":red[빨간색 텍스트]")
st.write(":blue[파란색 텍스트]")
st.divider()

# 형식이 있는 텍스트
st.header("형식이 있는 텍스트")


# 코드블록
st.subheader("코드 블록 : st.code()")
st.code("print('Hello, World!')", language='python', line_numbers=True)


# 코드 + 결과 : st.echo()
st.subheader("코드 + 결과 : st.echo()") #출력까지 나오게함
with st.echo():
    name = "Chunghun Ha"
    st.write("Hello, Streamlit!", name)


# LaTeX 수식 : st.latex()
st.subheader("LaTeX 수식 : st.latex()")
st.latex(r"\int_a^b f(x) dx")
st.latex(r"\int_1^\infty\!\frac{1}{x^2}\,dx=\left[-\frac{\alpha\beta\gamma}{1}{x}\right]_1^\infty=1")

# 구분선
st.subheader("구분선 : st.divider()")
st.divider()


"""
# 🐶 :rainbow[Streamlit Magic]

### 마크다운 헤더3
- 마크다운 목록1. :red[**굵게**] 표시
- 마크다운 목록2. *기울임* 표시
    - 마크다운 목록2-1
    - 마크다운 목록2-2
1. 숫자마크다운
1. 숫자마크다운

### 마크다운 링크
- [네이버](https://naver.com)
- [구글](https://google.com)

### 마크다운 인용
> 인용문: "Streamlit은 데이터 앱을 쉽게 만들 수 있는 프레임워크입니다."
> 신채원 교수

### 마크다운 표
| 헤더1 | 헤더2 |
|-------|-------|
| 데이터1 | 데이터2 |

### 마크다운 코드 블록
```python
def hello_world():
    print("Hello, World!")'''

"""
st.divider()
st.title("🐶 미디어 삽입 연습")

# 이미지 삽입
st.header("이미지 넣기 : st.image()")
st.image(
    r"C:\Users\shinchaewon\Desktop\데이터시각화\KakaoTalk_20251124_140432552.jpg",
    width=200)

# 오디오 예시 (옵션)
# st.audio("경로", format="audio/mpeg", loop=True)

# 동영상 삽입
st.header("동영상 넣기 : st.video()")
st.video(
    r"C:\Users\shinchaewon\Downloads\5534286-hd_1080_1920_30fps.mp4",
    format="video/mp4",
    loop=True
)
st.divider()
st.title("📚 콜아웃(Callout) 예시")

# 정보 메시지 (Info)
st.subheader("정보 : st.info()")
st.info("This is a purely informational message", icon="ℹ️")

# 경고 메시지 (Warning)
st.subheader("경고 : st.warning()")
st.warning("This is a warning message", icon="⚠️")

# 에러 메시지 (Error)
st.subheader("에러 : st.error()")
st.error("This is an error message", icon="🚫")

# 성공 메시지 (Success)
st.subheader("성공 : st.success()")
st.success("This is a success message", icon="✅")

st.divider()
st.title("📊 데이터프레임 & 메트릭 예시")

# 데이터프레임 생성
st.header("Pandas 데이터프레임")
df = pd.DataFrame(
    {
        'id': [1, 2, 3],
        'name': ['Alice', 'Bob', 'Charlie'],
        'age': [24, 34, 45]
    }
)

st.write("👉 데이터프레임 출력")
st.dataframe(df)

# Metric 지표
st.header("지표(Metric)")

col1, col2, col3 = st.columns(3) # 컬럼으로 블록 자르기

col1.metric("Temperature", "70 ℉", "1.2 ℉") #파이썬 코드 변수 넣어서 만들기
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "-4%")

st.divider()
st.title("Streamlit 그래프")

# 랜덤 데이터프레임 생성
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"]
)

st.subheader("st.area_chart()")
st.area_chart(chart_data)

st.subheader("st.line_chart()")
st.line_chart(chart_data)

st.subheader("st.bar_chart()")
st.bar_chart(chart_data)

st.subheader("st.scatter_chart()")
st.scatter_chart(chart_data)

st.subheader("st.map()")
df = pd.DataFrame(
    np.random.randn(100, 2) / [100, 100] + [37.55, 126.92], #홍익대학교 위도경도
    columns=["lat", "lon"],
)

st.map(df)
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import altair as alt
import plotly.express as px

st.title("📊 다양한 그래프 예시")

# ---------------------------
# Matplotlib 그래프
# ---------------------------
st.subheader("Matplotlib: st.pyplot()")

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)

st.pyplot(fig)   # 👈 Matplotlib 출력
st.divider()     # 👈 구분선


# ---------------------------
# Altair 차트
# ---------------------------
st.subheader("Altair: st.altair_chart()")

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"]
)

c = (
    alt.Chart(chart_data)
    .mark_circle()
    .encode(
        x="a",
        y="b",
        size="c",
        color="c",
        tooltip=["a", "b", "c"]
    )
)

st.altair_chart(c, use_container_width=True)


# ---------------------------
# Plotly 차트
# ---------------------------
st.subheader("Plotly: st.plotly_chart()")

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length")

st.plotly_chart(fig)


st.title("🧩 레이아웃(columns & tabs) 예시")

# -----------------------------
# Columns 레이아웃
# -----------------------------
st.header("📌 컬럼(columns)")

# 1:2:1 비율로 컬럼 생성
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    st.write("✨ 1번 컬럼")
    st.checkbox("이것은 1번 컬럼에 속한 체크박스 1")
    st.checkbox("이것은 1번 컬럼에 속한 체크박스 2")

with col2:
    st.write("✨ 2번 컬럼")
    st.radio("2번 컬럼의 라디오 버튼", ['radio 1', 'radio 2', 'radio 3'])

with col3:
    st.write("✨ 3번 컬럼")
    st.selectbox("3번 컬럼의 셀렉트박스", ['select 1', 'select 2', 'select 3'])

# :orange[탭: st.tabs()]

# 탭 인스턴스 생성, 3개의 탭을 생성
tab_1, tab_2, tab_3 = st.tabs(['Python', 'R', 'Julia'])
with tab_1:
    st.write(
        """
'''python
import pandas as pd

df = pd.DataFrame(
    {
        'id': [1, 2, 3],
        'name': ['Alice', 'Bob', 'Charlie'],
        'age': [24, 34, 45]
    }
)
    '''
    """
)
with tab_2:
    st.write(
    """
    '''df <- data.frame(
        id = c(1, 2, 3),
        name = c('Alice', 'Bob', 'Charlie'),
        age = c(24, 34, 45)
    )
    '''
    """
    )
with tab_3:
    st.write(
    """
'''using DataFrames

df = DataFrame(
    id = [1, 2, 3],
    name = ["Alice", "Bob", "Charlie"],
    age = [24, 34, 45]
)
    '''
    """
)
# :orange[접기 레이아웃: st.expander()]
with st.expander('📌 접는 레이아웃'):
    st.write('🔍 접는 레이아웃은 특정 컨텐츠를 숨기거나 보이게 꼭 사용됩니다.')

# ------------------------------
# 사용자 입력 위젯
# ------------------------------

# :blue[사용자 입력]

# :orange[텍스트 입력]
text = st.text_input('여기에 텍스트를 입력해주세요')
st.write(f'입력한 텍스트: {text}')

# :orange[숫자 입력]
number = st.number_input('여기에 숫자를 입력해주세요')
st.write(f'입력한 숫자: {number}')

# :orange[날짜 입력]
date = st.date_input('여기에 날짜를 선택해주세요')
st.write(f'입력한 날짜: {date}')

# :orange[시간 입력]
time = st.time_input('시간을 선택해주세요')
st.write(f'입력한 시간: {time}')


# :orange[파일 업로드]
file = st.file_uploader('파일을 업로드해주세요')

# ------------------------------
# 파일을 임시적으 로 사용하는 방법
# ------------------------------
if file:
    st.write('업로드된 파일명:', file.name)

    # 파일 저장 경로 설정
    import os
    file_path = os.path.join("C:/Users/shinchaewon/Desktop/데이터시각화", file.name)

    # 저장
    with open(file_path, 'wb') as f:
        f.write(file.getbuffer())
    st.success(f'파일이 저장되었습니다: {file_path}')
# :blue[버튼]

# :orange[기본 버튼: st.button()]
button = st.button('일반 버튼')
if button:
    st.write('버튼이 클릭되었습니다!')

primary_button = st.button("주요 버튼", type='primary')
if primary_button:
    st.write('주요 버튼이 클릭되었습니다!')

# :orange[다운로드 버튼: st.download_button()]
with open(r"C:\Users\shinchaewon\Desktop\데이터시각화\KakaoTalk_20251124_140432552.jpg", "rb") as file:
    st.download_button(
        label="이미지 다운로드",
        data=file,
        file_name="KakaoTalk_20251124_140432552.jpg",
        mime="image/jpeg"
    )

# :orange[피드백: st.feedback()]
sentiment_mapping = {"one": "⭐", "two": "⭐⭐", "three": "⭐⭐⭐", "four": "⭐⭐⭐⭐", "five": "⭐⭐⭐⭐⭐"}
selected = st.feedback("stars")
if selected is not None:
    st.markdown(f"{sentiment_mapping[selected]} 선택하셨습니다!")

sentiment_mapping = {"material/thumb_down": "👎", "material/thumb_up": "👍"}
selected = st.feedback("thumbs")
if selected is not None:
    st.markdown(f"{sentiment_mapping[selected]} 선택하셨습니다!")

# :orange[링크 버튼: st.link_button()]
st.link_button("갤러리 링크", "https://streamlit.io/gallery")
st.title("선택박스")

# :orange[체크박스]
check = st.checkbox('여기를 체크하세요')## 이게 키임
if check:
    st.write('체크되었습니다.')

# :orange[라디오 버튼]
radio = st.radio('여기에서 선택하세요', ['선택 1', '선택 2', '선택 3']) #여기에서 선택하세요 가 키임
st.write(radio + '가 선택되었습니다.')

# :orange[셀렉트 박스]
select = st.selectbox('여기에서 선택하세요', ['선택 1', '선택 2', '선택 3']) # 선택1 선택2 말고 다른이름이름의 선택지면 상관 ㄴㄴ
st.write(select + '가 선택되었습니다.')

# :orange[멀티 셀렉트 박스]
multi = st.multiselect('여기에서 여러 값을 선택하세요', ['선택 1', '선택 2', '선택 3'])
st.write(f'{type(multi)} = , {multi}가 선택되었습니다.')

st.title("🎚️ 슬라이더, 프로그레스 바")

# 슬라이더는 선택된 값을 반환
### :orange[슬라이더]
slider = st.slider('여기에서 값을 선택하세요', 0, 100, 50)
st.write(f'현재의 값은 {slider} 입니다.')

# 선택 슬라이더는 선택된 값 범위를 반환
### :orange[선택 슬라이더]
range_slider = st.select_slider('여기에서 값을 선택하세요', options=range(101), value=(25, 75))
st.write(f'현재의 값은 {range_slider} 입니다.')

# 컬러피커는 선택된 값을 반환
### :orange[컬러 피커]
color = st.color_picker('색을 선택하세요', '#00f900')
st.write(f'선택된 색은 {color} 입니다.')

# 프로그레스 바는 진행 상태를 반환
### :orange[프로그레스 바]
import time
button1 = st.button('실시')  # 버튼은 클릭 여부를 반환
if button1:
    progress = st.progress(0)
    for i in range(101):
        progress.progress(i)
        if i % 20 == 0:
            st.write(f'진행 상태: {i}%')
        time.sleep(0.05)

# spinner는 진행 상태를 반환
### :orange[스피너]
button2 = st.button('로드')  # 버튼은 클릭 여부를 반환
if button2:
    with st.spinner('로딩 중입니다...'):
        time.sleep(3)
    st.success('로딩 완료!')
st.title('애니매이션')
# 🎈 풍선 애니메이션
button4 = st.button('풍선을 띄워보세요')  # 버튼 클릭 여부를 반환
if button4:
    st.balloons()  # 풍선 애니메이션 출력

# ❄️ 눈 애니메이션
button5 = st.button('눈을 내려 보세요')  # 버튼 클릭 여부를 반환
if button5:
    st.snow()  # 눈 애니메이션 출력
st.title('캐싱')
# 5_✨고급기능.py

import time

@st.cache_data
def long_running_function(param1):
    time.sleep(5)
    return param1 + param1

start = time.time()

# 숫자 입력을 입력된 값을 반환
num_1 = st.number_input('입력한 숫자의 제곱을 계산합니다.')
st.write(f'num_1의 제곱은 {long_running_function(num_1)} 입니다.' +
         f'계산시간은 {time.time()-start:.2f}초 소요')
st.write(':green[캐싱이 적용되면 동일한 계산은 저장된 결과를 사용하여 빠르게 처리함]')

st.title('세션상태')
df = pd.DataFrame(np.random.randn(20, 2), columns=["x", "y"])

st.write('### :orange[session_state를 사용하지 않은 경우]')
color1 = st.color_picker("Color1", "#FF0000")
st.divider()  # 구분선
st.scatter_chart(df, x="x", y="y", color=color1)

if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(np.random.randn(20, 2), columns=["x", "y"])

st.write('### :orange[session_state를 사용한 경우]')
color2 = st.color_picker("Color2", "#FF0000")
st.divider()  # 구분선
st.scatter_chart(st.session_state.df, x="x", y="y", color=color2)

st.write('💕 :green[session_state를 사용하면, 저장된 state를 사용하므로 값이 고정됨]')
