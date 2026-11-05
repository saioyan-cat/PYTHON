import streamlit as st

# 網頁標題
st.title("我的網頁小工具")

# 文字輸入框（直接用變數接收輸入的值）
name = st.text_input("請輸入名字：")

# 網頁按鈕與點擊後的邏輯
if st.button("點我"):
    if name:
        st.success(f"嗨，{name}！")
    else:
        st.warning("你還沒有輸入名字喔！")
