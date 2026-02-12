import streamlit as st

# 1. ページ設定：ノイズを消し、ダークモードを強制
st.set_page_config(
    page_title="GDP Analyzer",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. 画像のデザインを再現するCSS
st.markdown("""
    <style>
    /* 背景色を画像のダークグレーに合わせる */
    .stApp {
        background-color: #121212;
    }
    /* ヘッダーやフッターのノイズを非表示 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* カードデザイン：角丸と控えめな境界線 */
    .card {
        background-color: #1E1E1E;
        padding: 1.5rem;
        border-radius: 20px;
        border: 1px solid #2C2C2C;
        margin-bottom: 1rem;
    }
    
    /* フォント：視認性の高いSans-serif */
    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)
