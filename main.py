import streamlit as st

st.set_page_config(page_title="MBTI 직업 추천", page_icon="🌟", layout="centered")

# 🎨 웹앱 헤더
st.markdown("<h1 style='text-align: center; color: #FF69B4;'>🌈 MBTI로 알아보는 나의 미래 직업 💼✨</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>내 성격 유형(MBTI)을 선택하면, 나에게 딱 맞는 직업을 추천해줄게요! 💖</h3>", unsafe_allow_html=True)

# 🎯 MBTI 목록
mbti_list = [
    "INTJ 🧠", "INTP 📘", "ENTJ 🕶️", "ENTP 💡",
    "INFJ 🌌", "INFP 🎨", "ENFJ 🌟", "ENFP 🔥",
    "ISTJ 📏", "ISFJ 🍀", "ESTJ 🧱", "ESFJ 💐",
    "ISTP 🛠️", "ISFP 🎶", "ESTP 🚀", "ESFP 🎭"
]

mbti_choice = st.selectbox("💡 당신의 MBTI를 선택하세요:", mbti_list)

# 📚 MBTI별 직업 추천 딕셔너리
job_recommendations = {
    "INTJ": ["🔬 데이터 과학자", "🧠 전략 기획자", "📊 경영 컨설턴트"],
    "INTP": ["🧪 연구원", "👨‍💻 개발자", "🧩 퍼즐 디자이너"],
    "ENTJ": ["💼 CEO", "📈 투자 분석가", "🧭 프로젝트 매니저"],
    "ENTP": ["💡 창업가", "🎙️ 방송인", "🧪 발명가"],
    "INFJ": ["🧘 심리상담가", "📖 작가", "🌱 NGO 활동가"],
    "INFP": ["🎨 예술가", "📚 시인", "💌 콘텐츠 크리에이터"],
    "ENFJ": ["👩‍🏫 교사", "🎤 리더십 코치", "🌟 연설가"],
    "ENFP": ["🎬 영화 감독", "📣 마케팅 전문가", "🌈 크리에이터"],
    "ISTJ": ["💼 회계사", "⚖️ 법률 전문가", "📦 물류 관리자"],
    "ISFJ": ["🏥 간호사", "👩‍🍳 요리사", "📚 사서"],
    "ESTJ": ["🛠️ 엔지니어", "📋 관리자", "🚔 경찰관"],
    "ESFJ": ["💐 이벤트 플래너", "🏫 교직원", "🤝 HR 매니저"],
    "ISTP": ["🔧 정비사", "🕹️ 게임 개발자", "🏍️ 레이서"],
    "ISFP": ["🎶 뮤지션", "📸 포토그래퍼", "👗 패션 디자이너"],
    "ESTP": ["🚀 세일즈", "📣 광고 기획자", "🎮 e스포츠 선수"],
    "ESFP": ["🎭 배우", "🎤 가수", "🌟 인플루언서"]
}

# 🧩 MBTI 코드 추출
mbti_code = mbti_choice.split()[0]

# 결과 출력 🎉
if mbti_code in job_recommendations:
    st.markdown(f"<h2 style='color: #FFD700;'>✨ {mbti_choice} 유형 추천 직업 ✨</h2>", unsafe_allow_html=True)
    for job in job_recommendations[mbti_code]:
        st.markdown(f"- {job}")

    st.balloons()
    st.markdown("---")
