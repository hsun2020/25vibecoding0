import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
from datetime import datetime, timedelta

st.set_page_config(page_title="미국 주식 분석", layout="wide")

st.title("🇺🇸 미국 주식 분석 웹앱")
st.markdown("주식을 선택하면 차트와 현재 상태를 분석해드려요! 📊")

# 📌 주식 선택
ticker = st.text_input("티커(symbol)을 입력하세요 (예: AAPL, TSLA, MSFT):", "AAPL")

# 데이터 가져오기
if ticker:
    stock = yf.Ticker(ticker)
    
    # 오늘 날짜
    today = datetime.today()
    
    # 📅 일봉 1년
    daily_df = stock.history(period="1y", interval="1d")
    # 📅 주봉 5년
    weekly_df = stock.history(period="5y", interval="1wk")

    st.subheader("📈 1년간 일봉 차트")
    fig_daily = go.Figure(data=[go.Candlestick(
        x=daily_df.index,
        open=daily_df["Open"],
        high=daily_df["High"],
        low=daily_df["Low"],
        close=daily_df["Close"]
    )])
    fig_daily.update_layout(xaxis_title="날짜", yaxis_title="주가", height=400)
    st.plotly_chart(fig_daily, use_container_width=True)

    st.subheader("📉 5년간 주봉 차트")
    fig_weekly = go.Figure(data=[go.Candlestick(
        x=weekly_df.index,
        open=weekly_df["Open"],
        high=weekly_df["High"],
        low=weekly_df["Low"],
        close=weekly_df["Close"]
    )])
    fig_weekly.update_layout(xaxis_title="날짜", yaxis_title="주가", height=400)
    st.plotly_chart(fig_weekly, use_container_width=True)

    # 📊 간단한 상태 판단
    current_price = daily_df["Close"][-1]
    low_1y = daily_df["Low"].min()
    high_1y = daily_df["High"].max()

    st.subheader("🔍 현재 상태 분석")

    col1, col2 = st.columns(2)
    with col1:
        st.metric("현재 주가", f"${current_price:.2f}")
    with col2:
        percent = (current_price - low_1y) / (high_1y - low_1y + 1e-6) * 100
        st.metric("1년 등락 위치", f"{percent:.1f}% 위치")

    # 상태 분석 결과
    status = ""
    emoji = ""
    advice = ""

    if percent < 20:
        status = "📉 저점 근처 (바닥일 가능성 있음)"
        emoji = "🟢"
        advice = "지금은 **매수 추천** 👍"
    elif percent > 80:
        status = "📈 고점 근처 (상투일 가능성 있음)"
        emoji = "🔴"
        advice = "지금은 **매도 추천** ⚠️"
    else:
        status = "🤔 중간 위치 (관망)"
        emoji = "🟡"
        advice = "지켜보는 것을 추천합니다 👀"

    st.markdown(f"### {emoji} {status}")
    st.markdown(f"**💡 조언:** {advice}")

