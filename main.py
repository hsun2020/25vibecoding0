import streamlit as st

st.set_page_config(page_title="MBTI 궁합 추천 💖", page_icon="💫", layout="centered")

# 🎀 타이틀
st.markdown("""
    <h1 style='text-align: center; color: #FFC0CB;'>💞 MBTI 궁합 추천 💞</h1>
    <h3 style='text-align: center;'>내 MBTI와 잘 맞는 성격 유형은 무엇일까? 🫶<br>유명한 인물 예시도 함께 알아보자! ✨</h3>
""", unsafe_allow_html=True)

# 🌈 MBTI 선택
mbti_list = [
    "INTJ 🧠", "INTP 📘", "ENTJ 🕶️", "ENTP 💡",
    "INFJ 🌌", "INFP 🎨", "ENFJ 🌟", "ENFP 🔥",
    "ISTJ 📏", "ISFJ 🍀", "ESTJ 🧱", "ESFJ 💐",
    "ISTP 🛠️", "ISFP 🎶", "ESTP 🚀", "ESFP 🎭"
]

mbti_choice = st.selectbox("🌟 당신의 MBTI를 선택하세요:", mbti_list)

# 💘 궁합 추천 데이터
mbti_match = {
    "INTJ": {"match": "ENFP 🔥", "examples": ["Tony Stark (Iron Man) 🦾", "Mark Zuckerberg 👨‍💻"]},
    "INTP": {"match": "ENTP 💡", "examples": ["Neo (The Matrix) 🕶️", "Albert Einstein 🧠"]},
    "ENTJ": {"match": "INFP 🎨", "examples": ["Gordon Ramsay 🍳", "Harvey Specter 💼"]},
    "ENTP": {"match": "INFJ 🌌", "examples": ["The Joker 🃏", "Robert Downey Jr. 🎬"]},
    "INFJ": {"match": "ENFP 🔥", "examples": ["Elsa (Frozen) ❄️", "Benedict Cumberbatch 🎭"]},
    "INFP": {"match": "ENFJ 🌟", "examples": ["Frodo Baggins 🧝‍♂️", "Alicia Keys 🎹"]},
    "ENFJ": {"match": "INFP 🎨", "examples": ["Mufasa (Lion King) 🦁", "Barack Obama 🇺🇸"]},
    "ENFP": {"match": "INFJ 🌌", "examples": ["Rapunzel 🌸", "Robin Williams 🎤"]},
    "ISTJ": {"match": "ESFP 🎭", "examples": ["Batman 🦇", "Natalie Portman 🎬"]},
    "ISFJ": {"match": "ESTP 🚀", "examples": ["Captain America 🛡️", "Selena Gomez 🎤"]},
    "ESTJ": {"match": "ISFP 🎶", "examples": ["Dwight Schrute 💼", "Judge Judy ⚖️"]},
    "ESFJ": {"match": "ISTP 🛠️", "examples": ["Monica Geller 🍝", "Taylor Swift 🎶"]},
    "ISTP": {"match": "ESFJ 💐", "examples": ["Arya Stark ⚔️", "Clint Eastwood 🤠"]},
    "ISFP": {"match": "ESTJ 🧱", "examples": ["Legolas 🏹", "Britney Spears 🎤"]},
    "ESTP": {"match": "ISFJ 🍀", "examples": ["James Bond 🕶️", "Madonna 🎤"]},
    "ESFP": {"match": "ISTJ 📏", "examples": ["Homer Simpson 🍩", "Miley Cyrus 🎤"]}
}

# 🧡 결과 보여주기
if mbti_choice:
    mbti_code = mbti_choice.split()[0]
    match_info = mbti_match.get(mbti_code, {})
    
    st.markdown(f"""
    <h2 style='color:#FF69B4;'>💖 {mbti_choice}와 잘 맞는 MBTI는... <span style='color:#FFB6C1'>{match_info.get("match", "❓")}</span> 💖</h2>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🎬 대표 인물/캐릭터 예시:")
    for ex in match_info.get("examples", []):
        st.markdown(f"- {ex}")

    st.balloons()

# 🌷 하단 여백 & 문구
st.markdown("---")
st.markdown("<div style='text-align: center; font-size: 15px;'>🌼 MBTI는 참고용일 뿐, 진짜 궁합은 마음으로 느껴보세요 💫</div>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center;'>Made with 💕 by [YourName]</div>", unsafe_allow_html=True)
