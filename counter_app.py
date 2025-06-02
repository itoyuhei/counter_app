import streamlit as st

st.title("Counter App")

# セッション状態にカウンターを保存
if 'count' not in st.session_state:
    st.session_state.count = 0

def increment():
    st.session_state.count += 1

if st.button("カウント"):
    increment()

st.write(f"Count: {st.session_state.count}")
