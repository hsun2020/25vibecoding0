pip install streamlit yfinance


import streamlit as st
import yfinance as yf

st.set_page_config(page_title="미국 주식 상태 분석", layout="centered")
st.title("📊 미국 주식 상태 분석기")
st.write("주식 티커를 입력하면 지금이 바닥인지 상투인지 알려줄게요! 😎")

# 사용자 입력
ticker = st.text_input("🔍 주식 티커(symbol)를 입력하세요 (예: AAPL, TSLA, MSFT)", "AAPL")

if ticker:
    stock = yf.Ticker(ticker)
    df = stock.history(period="1y")

    if df.empty:
        st.error("❌ 데이터를 불러오지 못했어요. 티커를 다시 확인해주세요.")
    else:
        current_price = df["Close"][-1]
        low_price = df["Low"].min()
        high_price = df["High"].max()
        position = (current_price - low_price) / (high_price - low_price + 1e-6) * 100

        st.markdown(f"### 💰 현재 주가: **${current_price:.2f}**")
        st.markdown(f"📉 1년 최저가: **${low_price:.2f}**")
        st.markdown(f"📈 1년 최고가: **${high_price:.2f}**")
        st.markdown(f"🧭 현재 위치: **{position:.1f}%** (0% = 최저가, 100% = 최고가)")

        # 상태 분석
        if position < 20:
            st.markdown("🟢 **저점 근처! 바닥일 가능성이 높아요** 🐢")
            st.success("👍 지금은 **매수 추천** 시점입니다!")
        elif position > 80:
            st.markdown("🔴 **고점 근처! 상투일 수 있어요** 🐂")
            st.warning("⚠️ 지금은 **매도 추천** 시점일 수 있어요.")
        else:
            st.markdown("🟡 **중간 구간** 🤔")
            st.info("👀 조금 더 기다리는 것이 좋을 수도 있어요.")

        st.caption("※ 단순히 1년 고점/저점을 기준으로 한 참고용 분석입니다.")
