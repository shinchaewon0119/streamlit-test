#!/usr/bin/env python
# coding: utf-8

# In[5]:


import altair as alt
import pandas as pd
import folium  
import altair as alt
import pydeck as pdk
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
from plotly.subplots import make_subplots 
pio.renderers.default='notebook_connected' 
import warnings
warnings.filterwarnings("ignore")


# In[6]:


import sys
print(sys.executable)


# In[49]:


from itertools import combinations
from collections import Counter
import networkx as nx
import matplotlib.pyplot as plt
import re
from konlpy.tag import Okt
import streamlit as st


# In[8]:


# 이전 사용했었던 코드 기반으로 초기 작성 네이버 api 로 작성


# In[9]:


import os
import sys
import urllib.request
import urllib.parse
import urllib.error
import pandas as pd
import json

# 네이버에서 발급받은 클라이언트 ID와 시크릿 사용
client_id = "l_TbyQUetE38ozvKUt1g"
client_secret = "Hc8Dk9xHXi"

# 파라미터 설정
display_count = 100          # 한 페이지에 표시할 검색 결과 수
num_data = 1000              # 전체 검색 데이터 개수
sort = "date"                # 정렬 기준 (date:날짜순, sim:유사도순)

# 검색할 단어의 URL 인코딩
encText = urllib.parse.quote("K팝 데몬 헌터스 팬덤")

# 결과를 저장할 list 생성
results = []

# for문을 사용하여 검색 결과를 페이지별로 요청
for idx in range(0, num_data, display_count):

    # JSON 결과 요청용 URL 생성
    url = (
        "https://openapi.naver.com/v1/search/news.json"
        + f"?query={encText}&start={idx+1}&display={display_count}&sort={sort}"
    )

    # 요청 객체 생성
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)

    try:
        # 요청 보내고 응답 받기
        response = urllib.request.urlopen(request)
        rescode = response.getcode()

        if rescode == 200:  # 응답 코드가 200이면 성공
            response_body = response.read()
            response_dict = json.loads(response_body.decode("utf-8"))
            results += response_dict["items"]
        else:
            print("Error Code:", rescode)

    except urllib.error.HTTPError as e:
        print("HTTPError:", e.code)
        print("Response body:", e.read().decode("utf-8"))
        break

print(f"총 데이터 개수: {len(results)}")

# pandas DataFrame으로 확인해보고 싶으면
df = pd.DataFrame(results)

print(df.head())

df.to_csv("k팝results.csv", index=False, encoding="utf-8-sig")



# In[10]:


import pandas as pd
from itertools import combinations
from collections import Counter
import networkx as nx
import matplotlib.pyplot as plt
import re
from konlpy.tag import Okt

# 수집한 데이터 불러오기
df = pd.read_csv(r"C:\Users\shinchaewon\Desktop\데이터시각화\3차시험\k팝results.csv")

df.head()


# In[11]:


descriptions = df["description"].dropna().tolist()


# In[12]:


# 오류 문제로 okt 경로문제로 llm 씀


# In[13]:


from konlpy.tag import Okt

okt = Okt(
    jvmpath=r"C:\Users\shinchaewon\anaconda3\envs\rstudio-_1\Library\bin\server\jvm.dll"
)
print(okt.morphs("자바 경로 테스트입니다"))



# In[14]:


okt = Okt()

# 불용어 사전 불러오기
with open(
    r"C:\Users\shinchaewon\Desktop\데이터시각화\stopword.txt",
    "r",
    encoding="utf-8"
) as f:
    stopwords = f.read().splitlines()

# 불용어 추가
stopwords.extend( [
    "기자", "보도", "뉴스", "기사", "사진",
    "밝혔다", "전했다", "말했다", "설명했다",
    "이번", "지난", "당시", "최근",
    "관련", "통해", "대해", "등",
    "한편", "또한", "그러나", "하지만",
    "위해", "때문", "경우", "사실"
]
)


# In[15]:


all_nouns = []

for text in descriptions:
    # 한글 + 공백만 남기기
    text_cleaned = re.sub(r"[^가-힣\s]", "", text)

    # 명사 추출
    nouns = okt.nouns(text_cleaned)

    # 한 글자 제거 + 불용어 제거 + 중복 제거
    nouns = [
        word for word in set(nouns)
        if len(word) > 1 and word not in stopwords
    ]

    all_nouns.append(nouns)

print(all_nouns[:5])


# In[16]:


edge_list = []

for nouns in all_nouns:
    if len(nouns) > 1:
        edge_list.extend(combinations(sorted(nouns), 2))

edge_counts = Counter(edge_list)

print(edge_counts.most_common(10))


# In[17]:


min_count = 20

filtered_edges = {
    edge: weight
    for edge, weight in edge_counts.items()
    if weight >= min_count
}

print("필터링된 엣지 수:", len(filtered_edges))


# In[18]:


G = nx.Graph()

weighted_edges = [
    (u, v, w) for (u, v), w in filtered_edges.items()
]

G.add_weighted_edges_from(weighted_edges)


# In[19]:


st.markdown("---")

import streamlit as st

st.subheader("네트워크 분석 기반 핵심 해석")

st.markdown("""
네트워크 중심에는 **K팝, 음악, 아이돌, 그룹, 앨범** 관련 키워드가 밀집되어 있으며,  
이와 함께 **세계, 해외, 미국** 등 글로벌 확장 키워드가 강하게 연결되어 있습니다.  
이는 해당 콘텐츠가 단순한 애니메이션이 아니라  
**K팝 산업의 글로벌 확장 사례로 인식되고 있음을 시사합니다.**

또한 **넷플릭스, 공개, 시작, 확산, 플랫폼** 키워드가 중심부에 위치해 있어,  
팬덤 형성 과정에서 **콘텐츠 자체뿐 아니라 넷플릭스 유통 구조가 중요한 촉매 역할**을 했음을 보여줍니다.  
이로 인해 **특정 요일에 기사와 관심이 집중되는 현상**이 발생했을 가능성이 높습니다.

한편 **노래, OST, 음원, 퍼포먼스** 키워드가 다수 연결되어 나타나,  
서사 중심보다는 **음악 소비를 통해 팬이 유입되고 팬덤으로 확장되는 구조**가 뚜렷하게 확인됩니다.  
이는 기존 **K팝 팬층이 자연스럽게 유입된 배경**으로 해석할 수 있습니다.
""")


# In[20]:


pos = nx.spring_layout(G, k=0.3, iterations=50, seed=42)

node_sizes = [G.degree(node) * 100 for node in G.nodes()]
edge_widths = [G[u][v]["weight"] * 0.05 for u, v in G.edges()]

plt.figure(figsize=(15, 15))

nx.draw_networkx(
    G,
    pos,
    with_labels=True,
    node_size=node_sizes,
    width=edge_widths,
    font_size=12,
    node_color="skyblue",
    edge_color="gray",
    alpha=0.8
)

plt.title("케이팝데몬헌터스 팬덤에 대한 네이버 뉴스 키워드 네트워크", fontsize=20)
plt.axis("off")



# In[21]:


import networkx as nx
import matplotlib.pyplot as plt
# -----------------------------
# 네트워크 레이아웃 설정
# -----------------------------
pos = nx.spring_layout(G, k=0.3, iterations=50, seed=42)

node_sizes = [G.degree(node) * 100 for node in G.nodes()]
edge_widths = [G[u][v]["weight"] * 0.05 for u, v in G.edges()]

# -----------------------------
# Matplotlib Figure 생성
# -----------------------------
plt.figure(figsize=(15, 15))

nx.draw_networkx(
    G,
    pos,
    with_labels=True,
    node_size=node_sizes,
    font_size=12,
    node_color="skyblue",
    edge_color="gray",
    alpha=0.8
)

plt.title(
    "케이팝데몬헌터스 팬덤에 대한 네이버 뉴스 키워드 네트워크",
    fontsize=20
)
plt.axis("off")



# In[22]:


import streamlit as st
from PIL import Image

img_path = r"C:\Users\shinchaewon\Desktop\네트워크 결과.png"
img = Image.open(img_path)

st.subheader("네트워크 분석 결과")

# 🔹 버튼 위젯
if st.button("네트워크 결과 이미지 보기"):
    st.image(img, caption="네트워크 분석 결과", use_container_width=True)




# In[23]:


import pandas as pd

path = r"C:\Users\shinchaewon\Desktop\KC_KOREA_CLTUR_CNTNTS_GENRE_OBSTRC_FCTR_INFO_2024.csv"

df = pd.read_csv(path, encoding="utf-8-sig")

df.head()


# In[24]:


df.info()


# In[25]:


# 한류 실태조사 데이터 


# In[26]:


df = df.rename(columns={
    "OBSTRC_FCTR_CN": "저해요인",
    "ALL_TOTAL_CO": "응답자수",
    "MALE_RATE": "남성비율",
    "FEMALE_RATE": "여성비율",
    "ALL_N10S_RATE": "10대비율",
    "ALL_N20S_RATE": "20대비율",
    "ALL_N30S_RATE": "30대비율",
    "ALL_N40S_RATE": "40대비율",
    "ALL_N50S_RATE": "50대이상비율",
    "REPRT_YEAR_CN": "조사연도",
    "EXAMIN_COUNTRY_NM": "국가",
    "CNTNTS_URL": "출처URL"
})


# In[27]:


st.title("한류 콘텐츠 저해요인 분석")
st.subheader("결과 해석")

st.markdown("""
**핵심 요약**
-크게 보이는 문구인 **‘한국과 자국의 정치·외교 관계’**는 콘텐츠 품질과 별개로, **국가 간 관계/정책/여론**이 한류 수용에 영향을 줄 수 있음을 시사합니다.  
 **외교·정치 요인**은 특정 국가/시기에서 한류 확산을 제한할 수 있는 외생 변수로 작동할 수 있습니다.
""")


# In[33]:


import sys
print(sys.executable)
from wordcloud import WordCloud
print("wordcloud OK")


# In[34]:


import streamlit as st
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter

st.subheader("저해요인 워드클라우드")

# 1) 저해요인 텍스트 정리
texts = (
    df["저해요인"]
    .dropna()
    .astype(str)
    .str.strip()
)
texts = texts[texts != ""]

freq = Counter(texts)

# 2) 워드클라우드 생성
font_path = r"C:\Windows\Fonts\malgun.ttf"
wc = WordCloud(
    font_path=font_path,
    width=900,
    height=600,
    background_color="white",
    max_words=80,
    collocations=False
).generate_from_frequencies(freq)

fig, ax = plt.subplots(figsize=(10, 7))
ax.imshow(wc)
ax.axis("off")

st.pyplot(fig)

# 메모리/중복 출력 방지
plt.close(fig)


# In[ ]:


st.title("한류 콘텐츠 저해요인 분석")
st.subheader("결과 해석")

st.markdown("""
**핵심 요약**
-크게 보이는 문구인 **‘한국과 자국의 정치·외교 관계’**는 콘텐츠 품질과 별개로, **국가 간 관계/정책/여론**이 한류 수용에 영향을 줄 수 있음을 시사합니다.  
 **외교·정치 요인**은 특정 국가/시기에서 한류 확산을 제한할 수 있는 외생 변수로 작동할 수 있습니다.
""")


# In[29]:


import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("한류 콘텐츠 저해요인 분석")

# ======================
# 사이드바 필터
# ======================
st.sidebar.header("필터")

year = st.sidebar.selectbox(
    "조사연도 선택",
    sorted(df["조사연도"].unique())
)

country = st.sidebar.selectbox(
    "국가 선택",
    sorted(df["국가"].unique())
)

# 필터 적용
df_f = df[(df["조사연도"] == year) & (df["국가"] == country)]


# In[35]:


import koreanize_matplotlib


# In[39]:


import seaborn as sns


# In[37]:


st.subheader("저해요인 TOP 10 (Seaborn)")

top10 = (
    df_f.groupby("저해요인", as_index=False)["응답자수"]
    .sum()
    .sort_values("응답자수", ascending=False)
    .head(10)
)

fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(
    data=top10,
    x="응답자수",
    y="저해요인",
    ax=ax
)

ax.set_title("저해요인 TOP 10")
ax.set_xlabel("응답자수")
ax.set_ylabel("저해요인")

st.pyplot(fig)
plt.close(fig)


# In[38]:


st.title("한류 콘텐츠 저해요인 분석")
st.subheader("결과 해석")

st.markdown("""
**핵심 요약**
연령대가 높아질수록(특히 50대 이상) 한류 콘텐츠에 대한 저해 인식 비율이 전반적으로 높으며, 저해요인의 성격도 ‘언어·문화 이해’에서 ‘콘텐츠 적합성·가치 인식’으로 이동합니다.""")


# In[31]:


import altair as alt

st.subheader("연령대별 저해요인 비율 (Altair)")

age_cols = ["10대비율", "20대비율", "30대비율", "40대비율", "50대이상비율"]

df_long = df_f.melt(
    id_vars=["저해요인"],
    value_vars=age_cols,
    var_name="연령대",
    value_name="비율"
)

chart = (
    alt.Chart(df_long)
    .mark_bar()
    .encode(
        x=alt.X("비율:Q", title="비율"),
        y=alt.Y("저해요인:N", sort="-x"),
        color="연령대:N",
        tooltip=["저해요인", "연령대", "비율"]
    )
    .properties(height=400)
)

st.altair_chart(chart, use_container_width=True)


# In[ ]:





# In[48]:


import streamlit as st
import plotly.express as px

st.subheader("저해요인 비율 (Donut)")
st.markdown("""
저해요인 비중을 순서대로 살펴보면, 한류 콘텐츠 소비를 가장 크게 저해하는 요인은 한국어가 어렵고 생소하다는 인식으로 나타났다. 그 다음으로는 자막이나 더빙을 통한 시청 과정의 불편함이 뒤를 이어, 언어 이해와 관련된 문제가 상위 요인을 형성하고 있음을 알 수 있다. 이후에는 자국과의 정치·외교적 관계가 중요한 저해요인으로 나타나, 문화 콘텐츠 수용이 외부 환경의 영향을 받는다는 점을 보여준다. 그 다음 단계에서는 비용 부담과 한국적인 색채가 강하다는 인식이 주요 요인으로 이어지며, 콘텐츠 및 상품의 현지 적합성 문제가 나타난다. 이후에는 가격 대비 품질, 콘텐츠의 다양성, 소재·스토리의 진부함, 문화적 이해의 어려움 등이 비교적 비슷한 수준으로 분포하며, 전반적으로 언어·문화·현지화 요인이 복합적으로 작용하고 있는 구조임을 확인할 수 있다.
""")

st.markdown("""
위젯이 실행되는데 시간이 조금 걸릴 수 있음""")
#  위젯 1: TOP N 선택
top_n = st.slider(
    "상위 저해요인 개수 선택",
    min_value=5,
    max_value=15,
    value=10,
    step=1
)

# ======================
# 위젯 2: 정렬 기준 선택

sort_order = st.radio(
    "정렬 기준 선택",
    ["응답자수 많은 순", "응답자수 적은 순"]
)

# ======================
# 데이터 정렬 및 TOP N 적용
# ======================
topN = (
    df_f.groupby("저해요인", as_index=False)["응답자수"]
    .sum()
)

if sort_order == "응답자수 많은 순":
    topN = topN.sort_values("응답자수", ascending=False)
else:
    topN = topN.sort_values("응답자수", ascending=True)

topN = topN.head(top_n)

# ======================
# 도넛 차트
# ======================
fig = px.pie(
    topN,
    names="저해요인",
    values="응답자수",
    hole=0.4,
    title=f"저해요인 비율 (TOP {top_n})"
)

st.plotly_chart(fig, use_container_width=True)


# In[ ]:




