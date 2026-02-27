import streamlit as st


def show_end_screen(quiz):
    """
    Display the quiz completion screen with results.
    
    Args:
        quiz: Quiz object containing questions, answers, and results
    """
    st.title("Quiz Completed!")

    # Calculate and display score
    score = quiz.calculate_score()
    total_questions = quiz.get_total_questions()
    
    st.write(f"### Your Score: **{score} / {total_questions}**")
    
    # Calculate percentage
    percentage = (score / total_questions * 100) if total_questions > 0 else 0
    st.write(f"**Percentage: {percentage:.1f}%**")
    
    # Save results to CSV
    username = st.session_state.get("username", "Anonymous")
    try:
        quiz.save_results_to_csv(username)
        st.success("✅ Results saved to quiz_results.csv")
    except Exception as e:
        st.warning(f"Could not save results: {e}")
    
    st.write("## Results Breakdown")

    # Show results for each question using OOP methods
    for index, question in enumerate(quiz.questions):
        result = quiz.get_result_for_question(index)
        
        if result['is_correct']:
            st.success(f"Q{index+1}: Correct — {result['user_answer']}")
        else:
            st.error(f"Q{index+1}: Incorrect — {result['user_answer']}")
            st.write(f"Correct answer: {result['correct_answer']}")

    # Restart button
    if st.button("Restart Quiz"):
        # Reset everything
        keys_to_delete = ["quiz", "quiz_loaded", "screen", "score", "total_questions"]
        for key in keys_to_delete:
            if key in st.session_state:
                del st.session_state[key]

        st.session_state.screen = "welcome"
        st.rerun()
