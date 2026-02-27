import streamlit as st
from welcome_page import show_welcome_screen
from quiz_manager import QuizManager
from quiz_page import show_quiz_screen
from quiz_complete import show_end_screen


def main():
    """
This is the main part of the program.
It controls which screen the user sees (welcome, quiz, results)
It stores important objects like the QuizManager and Quiz in Streamlit’s session state so the app can remember data between screens.
It manages the full quiz flow—from the welcome page to the quiz questions
and finally the results screen—using your OOP classes to keep everything organised and consistent.
    """
    # Initialize QuizManager 
    if "quiz_manager" not in st.session_state:
        st.session_state.quiz_manager = QuizManager()
    
    # Set default screen
    if "screen" not in st.session_state:
        st.session_state.screen = "welcome"

    # Show welcome screen
    if st.session_state.screen == "welcome":
        show_welcome_screen()

    # Show quiz screen
    elif st.session_state.screen == "quiz":
        # Create a new quiz instance if not exists
        if "quiz" not in st.session_state:
            st.session_state.quiz = st.session_state.quiz_manager.create_quiz()
        
        show_quiz_screen(st.session_state.quiz)

    # Show end screen
    elif st.session_state.screen == "end":
        # Use the quiz object from session state
        quiz = st.session_state.get("quiz")
        if quiz:
            show_end_screen(quiz)
        else:
            # Fallback if quiz object is missing
            st.error("Quiz data not found. Please restart the quiz.")
            if st.button("Restart"):
                st.session_state.screen = "welcome"
                st.rerun()


if __name__ == "__main__":
    main()


