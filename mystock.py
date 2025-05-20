import streamlit as st

# MBTI별 추천 직업 데이터
mbti_jobs = {
    "INTJ": ["데이터 과학자 📊", "전략 컨설턴트 🧠", "엔지니어 👷"],
    "INTP": ["연구원 🔬", "프로그래머 💻", "발명가 🛠️"],
    "ENTJ": ["CEO 🧑‍💼", "기획자 📈", "경영 컨설턴트 💼"],
    "ENTP": ["스타트업 창업자 🚀", "마케터 📣", "기획자 💡"],

    "INFJ": ["상담사 🧘", "작가 ✍️", "인권운동가 🕊️"],
    "INFP": ["디자이너 🎨", "예술가 🎭", "심리학자 🧠"],
    "ENFJ": ["교사 🧑‍🏫", "홍보 담당자 📢", "리더십 코치 🤝"],
    "ENFP": ["광고 기획자 📺", "배우 🎬", "창작자 🎤"],

    "ISTJ": ["회계사 📒", "공무원 🏛️", "법률 전문가 ⚖️"],
    "ISFJ": ["간호사 🏥", "교사 📚", "사회복지사 ❤️"],
    "ESTJ": ["매니저 📋", "군인 🎖️", "현장 감독 🏗️"],
    "ESFJ": ["행사 기획자 🎉", "간호조무사 💉", "인사 담당자 👥"],

    "ISTP": ["기술자 🧰", "정비사 🔧", "파일럿 ✈️"],
    "ISFP": ["플로리스트 🌸", "포토그래퍼 📸", "스타일리스트 👗"],
    "ESTP": ["영업 사원 💼", "모험가 🧗", "기업가 💵"],
    "ESFP": ["연예인 🎤", "여행 가이드 🧳", "MC 🎙️"],
}

# Streamlit 앱 UI 구성
st.set_page_config(page_title="MBTI 직업 추천", layout="centered")
st.title("🧠 MBTI 기반 직업 추천기")
st.write("MBTI 성격유형을 선택하면 어울리는 직업을 추천해드려요!")

# MBTI 선택
mbti_list = list(mbti_jobs.keys())
selected_mbti = st.selectbox("📌 MBTI 유형을 선택하세요", mbti_list)

# 추천 직업 출력
if selected_mbti:
    st.subheader(f"🔍 {selected_mbti} 유형에게 어울리는 직업은?")
    jobs = mbti_jobs[selected_mbti]
    for job in jobs:
        st.markdown(f"- {job}")
