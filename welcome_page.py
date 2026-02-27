import streamlit as st
from user import User


def show_welcome_screen():
    """
    Display the welcome screen with user name input and validation.
    Uses the User class for OOP-based validation.
    """
    st.title("Welcome to the Cyber Security Quiz 🔒")

    # Ask for name
    name = st.text_input("Enter your name:")

    # When the user clicks Start
    if st.button("Start Quiz"):
        # Create User object and validate using OOP
        user = User(name)
        is_valid, error_message = user.validate_name()
        
        if not is_valid:
            st.error(error_message)
        else:
            # Save user object and move to quiz
            st.session_state.user = user
            st.session_state.username = name  # Keep for backward compatibility
            st.session_state.screen = "quiz"
            st.rerun()







