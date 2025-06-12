import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="🔥 근육 성장 & 운동 가이드 💪",
    page_icon="🏋️‍♂️",
    layout="centered",
)

# CSS 스타일 (남자답게, 강렬하게)
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    color: #fff;
    font-family: 'Arial Black', Arial, sans-serif;
    padding: 0 20px 40px 20px;
}
h1 {
    font-size: 48px;
    text-align: center;
    margin-top: 40px;
    text-shadow: 4px 4px 10px #000000bb;
}
h3 {
    text-align: center;
    margin-top: 20px;
    color: #f39c12;
    text-shadow: 2px 2px 5px #000;
}
.selectbox-container {
    max-width: 500px;
    margin: 30px auto 0 auto;
}
.recommendation-box {
    background: #e74c3c;
    border-radius: 15px;
    padding: 30px;
    margin-top: 40px;
    box-shadow: 0 0 25px #e74c3caa;
    text-align: left;
}
.recommendation-box h2 {
    font-size: 38px;
    margin-bottom: 10px;
    text-align: center;
    text-shadow: 2px 2px 4px #000;
}
.recommendation-box p {
    font-size: 20px;
    font-weight: 600;
    line-height: 1.5;
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
st.markdown("<h1>🔥 근육 성장 & 운동 가이드 💪</h1>", unsafe_allow_html=True)
st.markdown("<h3>키우고 싶은 근육을 선택하면 운동과 자세한 방법을 알려줍니다! 🏋️‍♂️</h3>", unsafe_allow_html=True)

# 운동 데이터 (운동 이름, 설명)
muscle_workouts = {
    "가슴 (Chest) 🏋️": [
        {
            "name": "벤치프레스",
            "description": "벤치에 누워 바벨을 가슴 높이까지 내렸다가 밀어 올리는 운동입니다. 가슴 근육에 큰 자극을 줍니다.\n"
                           "✅ 자세: 발은 바닥에 고정, 허리는 살짝 아치형, 바벨을 천천히 내렸다가 폭발적으로 밀어 올리세요."
        },
        {
            "name": "푸쉬업",
            "description": "몸을 일직선으로 유지하며 팔을 굽혀 가슴이 바닥에 가까워지도록 내렸다가 다시 밀어 올리는 운동입니다.\n"
                           "✅ 자세: 손은 어깨너비보다 조금 넓게, 몸 전체가 일직선을 유지하도록 합니다."
        },
        {
            "name": "딥스",
            "description": "평행봉을 잡고 몸을 아래로 내렸다가 팔로 밀어 올려 가슴과 삼두를 강화하는 운동입니다.\n"
                           "✅ 자세: 몸을 약간 앞으로 기울여 가슴에 더 자극을 주세요."
        },
    ],
    "등 (Back) 💪": [
        {
            "name": "데드리프트",
            "description": "바벨을 바닥에서 들어 올리는 운동으로 등과 하체 근육을 동시에 강화합니다.\n"
                           "✅ 자세: 허리를 곧게 펴고, 무릎과 엉덩이를 사용해 바벨을 들어 올리세요."
        },
        {
            "name": "풀업",
            "description": "철봉을 잡고 몸을 위로 끌어올려 등 근육을 단련하는 운동입니다.\n"
                           "✅ 자세: 손은 어깨 너비로, 팔꿈치를 아래로 당기면서 천천히 올라가세요."
        },
        {
            "name": "바벨 로우",
            "description": "허리를 숙인 상태에서 바벨을 복부 쪽으로 당기는 운동입니다.\n"
                           "✅ 자세: 허리를 곧게 펴고 팔꿈치를 뒤로 당겨 등 근육을 조여주세요."
        },
    ],
    "어깨 (Shoulders) 🔥": [
        {
            "name": "밀리터리 프레스",
            "description": "바벨을 어깨 위에서 머리 위로 밀어 올리는 어깨 운동입니다.\n"
                           "✅ 자세: 허리를 곧게 펴고 팔꿈치를 완전히 펴면서 밀어 올리세요."
        },
        {
            "name": "사이드 레터럴 레이즈",
            "description": "덤벨을 들고 팔을 옆으로 들어 올려 어깨 측면을 강화합니다.\n"
                           "✅ 자세: 팔꿈치는 약간 굽히고 천천히 컨트롤하며 올리세요."
        },
        {
            "name": "업라이트 로우",
            "description": "바벨을 몸 앞에서 턱까지 끌어올려 어깨와 승모근을 단련합니다.\n"
                           "✅ 자세: 손은 어깨너비로 잡고 팔꿈치를 높게 유지하세요."
        },
    ],
    "팔 (Arms) 💥": [
        {
            "name": "바벨 컬",
            "description": "바벨을 들고 팔꿈치를 고정한 채 이두근을 수축시키는 운동입니다.\n"
                           "✅ 자세: 몸을 흔들지 말고 팔만 움직이세요."
        },
        {
            "name": "트라이셉스 익스텐션",
            "description": "덤벨이나 바벨을 머리 뒤로 내렸다가 팔을 펴는 삼두 운동입니다.\n"
                           "✅ 자세: 팔꿈치를 고정하고 천천히 움직이세요."
        },
        {
            "name": "해머 컬",
            "description": "덤벨을 수직으로 잡고 이두근과 팔뚝을 강화합니다.\n"
                           "✅ 자세: 팔꿈치를 몸 옆에 붙이고 천천히 올리세요."
        },
    ],
    "하체 (Legs) 🦵": [
        {
            "name": "스쿼트",
            "description": "어깨에 바벨을 올리고 무릎을 굽혀 앉았다 일어나는 운동으로 하체와 코어를 강화합니다.\n"
                           "✅ 자세: 무릎이 발끝을 넘지 않도록 주의하고, 허리는 곧게 펴세요."
        },
        {
            "name": "레그 프레스",
            "description": "레그프레스 머신을 사용해 다리를 밀어내는 하체 운동입니다.\n"
                           "✅ 자세: 발을 어깨너비로 벌리고 무릎을 완전히 펴지 마세요."
        },
        {
            "name": "런지",
            "description": "한쪽 다리를 앞으로 내딛고 무릎을 굽혀 하체를 강화합니다.\n"
                           "✅ 자세: 앞 무릎이 발끝을 넘지 않게 조절하세요."
        },
    ],
    "복근 (Abs) ⚡️": [
        {
            "name": "크런치",
            "description": "등을 바닥에 대고 상체를 살짝 들어 올리는 복근 운동입니다.\n"
                           "✅ 자세: 목에 힘 빼고 복근에 집중하세요."
        },
        {
            "name": "플랭크",
            "description": "팔꿈치와 발끝으로 몸을 지탱하며 코어를 단련하는 운동입니다.\n"
                           "✅ 자세: 몸이 일직선이 되도록 유지하세요."
        },
        {
            "name": "레그 레이즈",
            "description": "누운 상태에서 다리를 천천히 들어 올려 복근 하부를 자극합니다.\n"
                           "✅ 자세: 허리가 바닥에서 뜨지 않게 조심하세요."
        },
    ],
}

# 근육 선택 UI
selected_muscle = st.selectbox("💥 키우고 싶은 근육 부위를 선택하세요!", list(muscle_workouts.keys()))

# 운동 추천 & 설명
if selected_muscle:
    # 1. selected_muscle 키가 딕셔너리에 있는지 확인
    if selected_muscle not in muscle_workouts:
        st.error("❌ 선택한 근육 부위에 해당하는 운동이 없습니다!")
    else:
        workouts_list = muscle_workouts[selected_muscle]
        # 2. 운동 리스트가 비어있는지 확인
        if not workouts_list:
            st.error("⚠️ 해당 근육 부위에 등록된 운동이 없습니다.")
        else:
            workout = random.choice(workouts_list)
            st.markdown('<div class="recommendation-box">', unsafe_allow_html=True)
            st.markdown(f"<h2>🔥 {workout['name']} 🔥</h2>", unsafe_allow_html=True)
            st.markdown(f"<p>{workout['description'].replace(chr(10),'<br>')}</p>", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

# 푸터
st.markdown("""
<div class="footer">
    Made with 💪 by FitnessKing | Keep pushing your limits! 🔥🔥🔥
</div>
""", unsafe_allow_html=True)
