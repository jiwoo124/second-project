import streamlit as st
import random

# 🎨 스타일 커스터마이징
st.set_page_config(
    page_title="드라마 추천기 🎭📺",
    page_icon="🎬",
    layout="centered",
)

st.markdown(
    """
    <style>
    .big-title {
        font-size: 42px;
        color: #f63366;
        text-align: center;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .emoji-title {
        font-size: 28px;
        text-align: center;
    }
    .recommend-box {
        background-color: #fff5f8;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 2px 2px 10px rgba(246, 51, 102, 0.2);
        margin-top: 30px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 🎬 타이틀
st.markdown('<div class="big-title">🌟 드라마 추천기 🎭📺</div>', unsafe_allow_html=True)
st.markdown('<div class="emoji-title">장르를 골라주세요! 🎨</div>', unsafe_allow_html=True)

# 🎭 장르 선택
genres = {
    "로맨스 💕": ["사랑의 불시착", "그 해 우리는", "도깨비", "너의 시간 속으로"],
    "스릴러 🔪": ["시그널", "보이스", "악의 꽃", "마우스"],
    "코미디 😂": ["김비서가 왜 그럴까", "역도요정 김복주", "쌈 마이웨이", "하이바이, 마마!"],
    "판타지 🐉": ["호텔 델루나", "알함브라 궁전의 추억", "구미호뎐", "무빙"],
    "범죄/미스터리 🕵️‍♂️": ["비밀의 숲", "괴물", "모범형사", "라이프 온 마스"],
    "청춘 🎓": ["이태원 클라쓰", "치즈인더트랩", "우리들의 블루스", "스물다섯 스물하나"],
    "사극 👘": ["미스터 션샤인", "해를 품은 달", "옷소매 붉은 끝동", "철인왕후"],
}

selected_genre = st.selectbox("장르 선택 🎬", list(genres.keys()))

if selected_genre:
    st.markdown('<div class="recommend-box">', unsafe_allow_html=True)
    st.subheader(f"{selected_genre} 추천 드라마는... 🎁")
    recommendation = random.choice(genres[selected_genre])
    st.markdown(f"<h2 style='text-align: center;'>🌈 <strong>{recommendation}</strong> 🌈</h2>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# 🎉 푸터
st.markdown(
    """
    <br><hr>
    <div style='text-align: center; font-size: 16px;'>
    Made with ❤️ by DramaLover 🎬<br>
    즐거운 감상 되세요! 📺🍿
    </div>
    """,
    unsafe_allow_html=True
)
