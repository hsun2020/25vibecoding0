import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

# 주가 범위 기준 설정
def price_level(current, low, high):
    if current <= low * 1.1:
        return "📉 현재는 저점 근처입니다."
    elif current >= high * 0.9:
        return "📈 현재는 고점 근처입니다."
    else:
        return "📊 현재는 중간 가격대입니다."

# 간단한 매수 추천 로직
def buy_recommendation(current, low, high):
    level = current / low
    if level <= 1.1:
        return "✅ 매수 추천", "현재가가 최근 저점 대비 낮은 수준입니다."
    elif level >= 1.4:
        return "❌ 매수 비추천", "현재가가 고점 대비 너무 높습니다."
    else:
        return "⚠️ 보류", "가격대가 애매하므로 더 지켜보는 것이 좋습니다."

# 뉴스 크롤링 (Yahoo Finance 사용)
def fetch_news(ticker):
    url = f"https://finance.yahoo.com/quote/{ticker}?p={ticker}"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    news_items = soup.select('li.js-stream-content')

    news_list = []
    for item in news_items[:5]:
        title = item.get_text(strip=True)
        news_list.append(title)
    return news_list

# 메인 웹앱
st.title("📊 미국 주식 분석 웹앱")
st.markdown("**미국 주식의 차트, 가격 분석, 추천 및 뉴스 이슈 제공**")

ticker = st.text_input("티커 입력 (예: AAPL, TSLA, MSFT 등)", "AAPL")

if ticker:
    stock = yf.Ticker(ticker)
    df = stock.history(period="1y")

    if df.empty:
        st.error("데이터를 불러올 수 없습니다. 올바른 티커인지 확인해주세요.")
    else:
        st.subheader(f"{ticker} 주가 차트")

        # 차트 선택
        view = st.radio("차트 타입 선택", ["일봉", "주봉", "월봉"])

        if view == "주봉":
            df = df.resample("W").agg({"Open": "first", "High": "max", "Low": "min", "Close": "last", "Volume": "sum"})
        elif view == "월봉":
            df = df.resample("M").agg({"Open": "first", "High": "max", "Low": "min", "Close": "last", "Volume": "sum"})

        fig = go.Figure(data=[go.Candlestick(
            x=df.index,
            open=df['Open'],
            high=df['High'],
            low=df['Low'],
            close=df['Close']
        )])
        fig.update_layout(title=f"{ticker} {view} 차트", xaxis_rangeslider_visible=False)
        st.plotly_chart(fig)

        # 현재가, 고점, 저점 분석
        current_price = df['Close'][-1]
        low_52w = df['Low'].min()
        high_52w = df['High'].max()

        st.subheader("📈 가격 분석")
        st.write(f"**현재가:** ${current_price:.2f}")
        st.write(f"**52주 최저가:** ${low_52w:.2f}")
        st.write(f"**52주 최고가:** ${high_52w:.2f}")
        st.info(price_level(current_price, low_52w, high_52w))

        # 추천
        st.subheader("📌 매수 의견")
        recommendation, reason = buy_recommendation(current_price, low_52w, high_52w)
        st.write(f"**매수 추천 여부:** {recommendation}")
        st.write(f"**이유:** {reason}")
        st.write(f"**추천 매수 가격:** ${low_52w * 1.05:.2f} 이하")

        # 뉴스
        st.subheader("📰 최근 뉴스")
        try:
            news = fetch_news(ticker)
            for i, item in enumerate(news):
                st.markdown(f"{i+1}. {item}")
        except:
            st.warning("뉴스를 가져올 수 없습니다.")

