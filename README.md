# Cyber-Security-quiz

## Introduction


This cybersecurity quiz is a minimum viable product (MVP) designed for early‑career professionals joining the organisation. Its purpose is to introduce new hires to essential cybersecurity practices, reinforce internal standards, and promote strong data protection and privacy habits across all levels of the organisation.

All data used in this quiz is synthetic and intentionally simplified to support beginner‑level learning and ensure a safe, controlled training environment.

This cyber security app is a desktop application that uses [Python](https://www.python.org/0), [Streamlit](https://docs.streamlit.io/develop/concepts) and [Figma](https://www.figma.com/files/902667414815738345/recents-and-sharing?fuid=1560570689866732652). The quiz collects the user’s unique ID passcode to generate a personalised set of security questions. This helps new joiners learn how to stay safe online and protect the organisation’s assets through practical, beginner‑friendly scenarios.


This readme will cover both technical and user documentation.
For technical documentation this readme cover:
- Designing the quiz
- Coding 
- Testing 
- Deploying the code 
- Implementing GUI/UI design 


For user documentation, this readme will cover:


- What the quiz does
-  Instructions on how to run the quiz locally on your computer
- Pre-requisites and running the code 


## DESIGN

In this section, we focus on the design of the quiz interface. The graphical user interface (GUI) was created using [Figma](https://www.figma.com/files/902667414815738345/recents-and-sharing?fuid=1560570689866732652) , which was used to plan and organise how the quiz looks and behaves before development. The design shows the layout, button placement, question screens, and overall structure to ensure the experience is clear and easy to follow. Figure 1 illustrates the user flow from a front-end perspective, meaning it represents what users will actually see and interact with in the final version. This includes how users move between questions, enter their answers, receive validation messages, and progress through the quiz in a logical and structured way. The aim of the design is to provide a simple, intuitive, and user-friendly experience for all users.

<img width="1005" height="620" alt="Screenshot 2026-02-27 at 09 31 12" src="https://github.com/user-attachments/assets/2afde016-1704-406c-9fdb-3ff689940aba" />
<img width="679" height="522" alt="Screenshot 2026-02-27 at 09 33 57" src="https://github.com/user-attachments/assets/6cdab6d3-93ed-4788-9641-d2764d353ed0" />


## DEVELOPMENT

This section highlights the technical side of how the quiz was built and is intended for readers who want a deeper look into the development process. If you’re looking for a more user‑friendly explanation instead, please refer to the **Documentation** section of this README.

This quiz contains the following modules in the python domain

- main.py
- quiz_page.py
- welcome_page.py
- quiz_complete.py
- questions.csv
- quiz_results.csv
  The following represent Class Modules
  - user.py
  - quiz.py
  - quiz_manager.py
 
**Pre-requisites**

Please ensure you have the latest version of python or Python 3.11+ . Run this command to check your current python version.

      python --version

If you are using python 3 run this command:

      python3 --version
You will also need streamlit 

      pip install streamlit
If you are using python 3 run this command:

      pip3 install streamlit

## Main.py

This is the main module forming the central organiser of all modules  It coordinates navigation, initialises core objects, and manages application state using Streamlit’s session system. When the app runs, this file decides what happens next.

To access the full code, please navigate to the repo and work your way through the .py files.

This is the desired flow:

     Welcome → Quiz → End

Imported dependencies 

      import streamlit as st
      from welcome_page import show_welcome_screen
      from quiz_manager import QuizManager
      from quiz_page import show_quiz_screen
      from quiz_complete import show_end_screen

Within the code, you will notice this command line:

     if st.session_state.screen == "welcome":
        show_welcome_screen()

The st.session_state is needed to maintain objects across reruns. Since Streamlit reruns the script on every interaction, session state is critical for maintaining continuity and ensuring all data is safe despite reruns. 


## Question Class (question_class.py)
Represents a single quiz question with its answer options.

Key Features:

- Stores question text, multiple-choice options, and the correct answer index
- Provides a method to validate user answers
- Encapsulates question logic in a reusable object

Example:

     question = Question(
       text="What is phishing?",
       options=["A type of malware", "A social engineering attack", "Fishing activity"],
       correct_index=1
      )
      
## Quiz Class (quiz.py)
Manages the entire quiz session, including questions, user answers, and scoring.

Key Features:

- Stores a collection of Question objects
- Tracks user answers throughout the quiz
- Calculates scores and validates completion
- Saves results to CSV for record-keeping
- Provides detailed feedback for each question

Core Methods:

- answer_question() - Records user's answer
- calculate_score() - Computes total correct answers
- is_complete() - Checks if all questions are answered
- save_results_to_csv() - Persists quiz results with timestamp


## User Class (user.py)
Represents a quiz participant with built-in validation.

Key Features:

Encapsulates user data (name)
Validates user input according to business rules:
 - Name must be 3-19 characters
 - Cannot contain numbers
 - Cannot be blank
   
Demonstrates encapsulation by keeping validation logic within the class


## QuizManager Class (quiz_manager.py)
Acts as a factory for creating quiz instances and managing question data.

Key Features:

- Loads questions from CSV file
- Creates Question objects from raw data
- Provides Quiz instances on demand
- Centralises data loading logic
Workflow:

manager = QuizManager("questions.csv")
quiz = manager.create_quiz()  # Returns a Quiz with loaded questions


## UI Modules
The application uses separate modules for each screen:

- welcome_page.py - User registration and validation
- quiz_page.py - Main quiz interface with question display
- quiz_complete.py - Results screen with detailed feedback
- main.py - Application controller managing screen flow


## OOP Principles Applied

Encapsulation
Each class manages its own data and provides methods to interact with it:

- User class handles name validation internally
- Question class knows how to check if an answer is correct
- Quiz class manages its own scoring logic
- Single Responsibility

Each module has one clear purpose:

- QuizManager handles data loading
- Quiz manages quiz state
- UI modules handle display logic only
- Separation of Concerns
- Business logic (classes) is separated from presentation logic (Streamlit UI), making the code easier to test and maintain.

**Data Flow**

- Initialisation: QuizManager loads questions from CSV
- User Input: User object validates participant name
- Quiz Creation: QuizManager creates a Quiz instance
- Answer Collection: Quiz stores user responses
- Scoring: Quiz calculates results using Question.is_correct()
- Persistence: Results saved to quiz_results.csv


File Structure

    ├── main.py                 # Application entry point
    ├── question_class.py       # Question model
    ├── quiz.py                 # Quiz logic and scoring
    ├── quiz_manager.py         # Data loading and quiz creation
    ├── user.py                 # User model with validation
    ├── welcome_page.py         # Welcome screen UI
    ├── quiz_page.py            # Quiz interface UI
    ├── quiz_complete.py        # Results screen UI
    ├── questions.csv           # Question database
    ├── quiz_results.csv        # Results storage (auto-generated)
    └── test_smoke_etc.py       # Test suite


 


Key Technologies
- Python 3.x - Core programming language
- Streamlit - Web framework for rapid UI development
- CSV Module - Data persistence and loading
- unittest - Testing framework
## TESTING

The application includes comprehensive tests in test_smoke_etc.py covering all core functionality.

Running Tests
Execute the test suite with:

python test_smoke_etc.py


Test Categories
1. Unit Tests
Question Class Tests:

Verifies correct answer validation
Tests incorrect answer detection
Quiz Class Tests:

Validates answer recording
Tests completion detection
Verifies score calculation
User Class Tests:

Tests name validation rules
Checks valid/invalid name scenarios
QuizManager Tests:

Verifies CSV loading
Tests quiz creation
2. Smoke Tests
Basic checks to ensure the application can start:

CSV file existence
Basic workflow execution
Data loading functionality
Test Coverage
The test suite covers:

✅ All core classes (Question, Quiz, User, QuizManager)
✅ Critical business logic (validation, scoring)
✅ Data loading and persistence
✅ Basic integration workflows
Expected Test Output

        ......
            ----------------------------------------------------------------------
            Ran 6 tests in 0.XXXs

        OK


## DOCUMENTATION

## EVALUATION
