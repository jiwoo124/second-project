import streamlit as st
import random

# 페이지 설정
st.set_page_config(
    page_title="💪 근육 성장 운동 추천 💥",
    page_icon="🏋️‍♂️",
    layout="centered",
)

# CSS 스타일링 - 강렬하고 남자다운 느낌!
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #1f1c2c, #928dab);
    color: #fff;
    font-family: 'Arial Black', Arial, sans-serif;
}
h1 {
    font-size: 48px;
    text-align: center;
    margin-top: 40px;
    text-shadow: 3px 3px 8px #000000aa;
}
h3 {
    text-align: center;
    margin-top: 20px;
    color: #f0a500;
    text-shadow: 2px 2px 5px #000;
}
.selectbox-container {
    max-width: 400px;
    margin: 30px auto 0 auto;
}
.recommendation-box {
    background: #ff3c00;
    border-radius: 15px;
    padding: 30px;
    margin-top: 40px;
    box-shadow: 0 0 20px #ff3c00aa;
    text-align: center;
}
.recommendation-box h2 {
    font-size: 38px;
    margin-bottom: 10px;
}
.recommendation-box p {
    font-size: 22px;
    font-weight: bold;
}
.footer {
    margin-top: 80px;
    font-size: 14px;
    text-align: center;
    color: #ccc;
}
</style>
""", unsafe_allow_html=True)

# 타이틀
st.markdown("<h1>🔥 근육 성장 운동 추천기 💪</h1>", unsafe_allow_html=True)
st.markdown("<h3>키우고 싶은 근육을 선택하세요! 🏋️‍♂️</h3>", unsafe_allow_html=True)

# 근육별 운동 리스트
muscle_workouts = {
    "가슴 (Chest) 🏋️": [
        "벤치프레스 - 무게감 있게! 🏋️‍♂️",
        "푸쉬업 - 가슴 불태워! 🔥",
        "딥스 - 깊게 내려가자! ⬇️"
    ],
    "등 (Back) 💪": [
        "데드리프트 - 등 근육 완전 자극! ⚡️",
        "풀업 - 철봉 위의 지배자! 🦾",
        "바벨 로우 - 강한 등 만들기! 🏋️"
    ],
    "어깨 (Shoulders) 🔥": [
        "밀리터리 프레스 - 어깨 정복! 💥",
        "사이드 레터럴 레이즈 - 광배근 발달! ✨",
        "업라이트 로우 - 어깨 깡패 되자! 💪"
    ],
    "팔 (Arms) 💥": [
        "바벨 컬 - 이두 불태워! 🔥",
        "트라이셉스 익스텐션 - 팔 근육 빵빵! 💣",
        "해머 컬 - 팔뚝 근육 장전! 🛠️"
    ],
    "하체 (Legs) 🦵": [
        "스쿼트 - 힘의 근원! 🏋️‍♂️",
        "레그 프레스 - 다리 폭발시키기! 💥",
        "런지 - 강철 다리 만들기! ⚔️"
    ],
    "복근 (Abs) ⚡️": [
        "크런치 - 복부 집중 공격! 🔥",
        "플랭크 - 코어 완전 강화! 🛡️",
        "레그 레이즈 - 복근 깊게 다지기! 💪"
    ],
}

# 선택 박스
selected_muscle = st.selectbox("근육 부위 선택", list(muscle_workouts.keys()))

# 추천 출력
if selected_muscle:
    st.markdown('<div class="recommendation-box">', unsafe_allow_html=True)
    st.markdown(f"<h2>{selected_muscle} 운동 추천</h2>", unsafe_allow_html=True)
    workout = random.choice(muscle_workouts[selected_muscle])
    st.markdown(f"<p>👉 {workout}</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# 푸터
st.markdown("""
<div class="footer">
    Made with 💪 by FitnessKing | Keep pushing your limits! 🔥🔥🔥
</div>
""", unsafe_allow_html=True)
