import streamlit as st
import random

st.title("🎲 숫자 맞히기 게임")
st.write("1부터 100 사이의 숫자를 맞혀보세요!")


if "secret" not in st.session_state:
    st.session_state.secret = random.randint(1, 100)
    st.session_state.attempts = 0


guess = st.number_input("숫자를 입력하세요", min_value=1, max_value=100, step=1)


if st.button("맞혀볼게요!"):
    st.session_state.attempts += 1
    if guess < st.session_state.secret:
        st.warning("📉 너무 작아요!")
    elif guess > st.session_state.secret:
        st.warning("📈 너무 커요!")
    else:
        st.success(f"🎉 정답이에요! {st.session_state.attempts}번 만에 맞혔어요!")
        if st.button("다시 시작하기"):
            st.session_state.secret = random.randint(1, 100)
            st.session_state.attempts = 0