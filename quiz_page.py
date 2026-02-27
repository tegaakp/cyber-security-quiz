import streamlit as st

"""
This module focuses on the main quiz page, highlighting what end users will see.
"""

def show_quiz_screen(quiz):
    """
    Show the quiz page with all questions.

    Arguments:
        quiz: A Quiz object that stores the questions and records the user's answers.
    """
    st.title("Cyber Security Quiz")

    # Reset answers only the first time quiz loads
    if "quiz_loaded" not in st.session_state:
        st.session_state.quiz_loaded = True

    # Show each question

    """
       Enumerate lets you loop through a list AND automatically gives you the index number for each item.
    """
    for index, q in enumerate(quiz.questions):
        st.write(f"### Question {index + 1}")
        st.write(q.text)

        answer = st.radio(
            "Choose an answer:",
            q.options,
            key=f"question_{index}",
            index=None
        )

        if answer is not None:
            quiz.answer_question(index, answer)

        st.write("---")

    # Submit button
    if st.button("Submit Quiz"):
        # Check if all questions are answered using OOP method
        if not quiz.is_complete():
            st.warning("⚠️ Please answer all questions before submitting.")
            return

        # Calculate score using OOP method
        score = quiz.calculate_score()

        # Store quiz object and results in session
        st.session_state.quiz = quiz
        st.session_state.score = score
        st.session_state.total_questions = quiz.get_total_questions()
        st.session_state.screen = "end"
        st.rerun()


