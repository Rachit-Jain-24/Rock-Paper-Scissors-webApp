import streamlit as st
import random

def play_game(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    st.set_page_config(page_title="Rock Paper Scissors", page_icon="✊✋✌️", layout="wide")

    st.title("🎮 Rock Paper Scissors Challenge!")

    # Custom CSS for better styling
    st.markdown("""
    <style>
    .big-font {
        font-size:30px !important;
        font-weight: bold;
    }
    .medium-font {
        font-size:20px !important;
    }
    .stButton>button {
        height: 3em;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

    # Initialize session state variables
    if 'rounds' not in st.session_state:
        st.session_state.rounds = 0
    if 'user_wins' not in st.session_state:
        st.session_state.user_wins = 0
    if 'computer_wins' not in st.session_state:
        st.session_state.computer_wins = 0
    if 'user_choices' not in st.session_state:
        st.session_state.user_choices = []
    if 'computer_choices' not in st.session_state:
        st.session_state.computer_choices = []
    if 'last_result' not in st.session_state:
        st.session_state.last_result = ""

    col1, col2, col3 = st.columns([1,2,1])

    with col1:
        st.markdown("<p class='big-font'>You</p>", unsafe_allow_html=True)
        st.markdown(f"<p class='medium-font'>Wins: {st.session_state.user_wins}</p>", unsafe_allow_html=True)

    with col3:
        st.markdown("<p class='big-font'>Computer</p>", unsafe_allow_html=True)
        st.markdown(f"<p class='medium-font'>Wins: {st.session_state.computer_wins}</p>", unsafe_allow_html=True)

    with col2:
        st.markdown("<p class='big-font'>Choose your move:</p>", unsafe_allow_html=True)
        col_rock, col_paper, col_scissors = st.columns(3)
        with col_rock:
            rock = st.button("🪨 Rock")
        with col_paper:
            paper = st.button("📄 Paper")
        with col_scissors:
            scissors = st.button("✂️ Scissors")

        if rock or paper or scissors:
            user_choice = "rock" if rock else "paper" if paper else "scissors"
            computer_choice = random.choice(["rock", "paper", "scissors"])
            result = play_game(user_choice, computer_choice)
            
            st.session_state.rounds += 1
            st.session_state.user_choices.append(user_choice)
            st.session_state.computer_choices.append(computer_choice)
            
            if result == "You win!":
                st.session_state.user_wins += 1
            elif result == "Computer wins!":
                st.session_state.computer_wins += 1

            st.session_state.last_result = f"Your choice: {user_choice.capitalize()} | Computer's choice: {computer_choice.capitalize()} | {result}"

        if st.session_state.last_result:
            st.markdown(f"<p class='medium-font'>{st.session_state.last_result}</p>", unsafe_allow_html=True)

    st.markdown("---")

    col_stats, col_chart = st.columns(2)

    with col_stats:
        st.subheader("📊 Game Statistics")
        st.write(f"Total rounds played: {st.session_state.rounds}")

    with col_chart:
        if st.session_state.rounds > 0:
            st.subheader("🥧 Choice Distribution")
            choices = ["rock", "paper", "scissors"]
            user_choice_counts = [st.session_state.user_choices.count(choice) for choice in choices]
            computer_choice_counts = [st.session_state.computer_choices.count(choice) for choice in choices]
            
            chart_data = {
                "Choices": choices * 2,
                "Counts": user_choice_counts + computer_choice_counts,
                "Player": ["You"] * 3 + ["Computer"] * 3
            }
            
            st.bar_chart(chart_data, x="Choices", y="Counts", color="Player")

    if st.button("🔄 Reset Game"):
        for key in st.session_state.keys():
            del st.session_state[key]
        st.experimental_rerun()

if __name__ == "__main__":
    main()