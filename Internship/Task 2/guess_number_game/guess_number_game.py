import streamlit as st
import random

# Initialize session state
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.score = 100
    st.session_state.game_over = False

st.title("🎮 Guess the Number Game")

st.write("Guess a number between 1 and 100")

guess = st.number_input("Enter your guess", min_value=1, max_value=100, step=1)

if st.button("Submit Guess") and not st.session_state.game_over:
    st.session_state.attempts += 1

    if guess < st.session_state.number:
        st.warning("📉 Too low! Try higher.")
        st.session_state.score -= 10

    elif guess > st.session_state.number:
        st.warning("📈 Too high! Try lower.")
        st.session_state.score -= 10

    else:
        st.success(f"🎉 Correct! You guessed it in {st.session_state.attempts} attempts.")
        st.success(f"🏆 Your Score: {st.session_state.score}")
        st.session_state.game_over = True

# Restart button
if st.button("🔄 Restart Game"):
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.score = 100
    st.session_state.game_over = False

# Display attempts
st.write(f"Attempts: {st.session_state.attempts}")