# Cyber-Security-quiz

## Introduction


This cybersecurity quiz is a minimum viable product (MVP) designed for early‑career professionals joining the organisation. Its purpose is to introduce new hires to essential cybersecurity practices, reinforce internal standards, and promote strong data protection and privacy habits across all levels of the organisation.

All new employees are required to complete a mandatory cybersecurity awareness training course during onboarding. This course introduces internal security standards, acceptable use policies, and best practices for protecting company assets. A formal assessment at the end of the course requires participants to achieve a minimum passing score of 80%, reinforcing the importance of understanding and applying security principles from the outset of their employment.

The proposed MVP supports this existing requirement by providing an accessible, low-pressure preparation tool for early-career professionals before they complete the official training assessment. Rather than replacing the formal course, the quiz acts as a preparatory learning aid that familiarises users with key concepts, terminology, and scenarios they will encounter later. Importantly, this MVP does not include a pass mark. The intention is to encourage engagement, build confidence, and promote knowledge retention without the stress of formal evaluation.

Whilst this quiz is intended to be a replica of the mandatory course, the questions used in this quiz are of general knowledge and not entirely specific to our organisation's internal guidelines. This is to make sure the application protects the integrity of our standards and does not expose any sensitive guidelines to the public.

By introducing cybersecurity principles early and interactively, this MVP aligns directly with the organisation’s onboarding objectives and contributes to strengthening overall security awareness across the workforce.

This cyber security app is a desktop application that uses [Python](https://www.python.org/0), [Streamlit](https://docs.streamlit.io/develop/concepts) and [Figma](https://www.figma.com/files/902667414815738345/recents-and-sharing?fuid=1560570689866732652). The quiz collects the user’s unique ID passcode to generate a personalised set of security questions. This helps new joiners learn how to stay safe online and protect the organisation’s assets through practical, beginner‑friendly scenarios.


This readme will cover both technical and user documentation.
For technical documentation this readme cover:
- Designing the quiz
- Coding 
- Testing 
- Deploying the code 
- Implementing GUI/UI design 



## DESIGN

In this section, we focus on the design of the quiz interface. The graphical user interface (GUI) was created using [Figma](https://www.figma.com/files/902667414815738345/recents-and-sharing?fuid=1560570689866732652) , which was used to plan and organise how the quiz looks and behaves before development. The design shows the layout, button placement, question screens, and overall structure to ensure the experience is clear and easy to follow. Figure 1 illustrates the user flow from a front-end perspective, meaning it represents what users will actually see and interact with in the final version. This includes how users move between questions, enter their answers, receive validation messages, and progress through the quiz in a logical and structured way. The aim of the design is to provide a simple, intuitive, and user-friendly experience for all users.

<img width="1005" height="620" alt="Screenshot 2026-02-27 at 09 31 12" src="https://github.com/user-attachments/assets/2afde016-1704-406c-9fdb-3ff689940aba" />
<img width="679" height="522" alt="Screenshot 2026-02-27 at 09 33 57" src="https://github.com/user-attachments/assets/6cdab6d3-93ed-4788-9641-d2764d353ed0" />

**Functional Requirements**
This covers what the system does defining the features, behaviours, and tasks the application must perform.

- Screen 1: The application allows users to input their name and start the quiz
- Screen 2: The application allows users to select one answer per question as well as navigate to the next page of questions
- Screen 3: The application allows users to finish the set of multiple choice questions and provide the option to submit the quiz
- Screen 4: The application generates the overall score out of 5 as well as providing a result breakdown. Users are also given the option to restart the quiz.

**Non-Functional Requirements**
This describes how the system performs

- Screen 1: The application must ensure user input meets the expected requirements e.g, contains 3-19 characters.
- Screen 2: The application should load within 2 seconds and be easy to use for beginners
- Screen 4: The application must store data securely in a csv file
- Screen 5: The system should allow the application to be run again.

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

### Main.py

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


### Question Class (question_class.py)
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
      
### Quiz Class (quiz.py)
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


### User Class (user.py)
Represents a quiz participant with built-in validation.

Key Features:

Encapsulates user data (name)
Validates user input according to business rules:
 - Name must be 3-19 characters
 - Cannot contain numbers
 - Cannot be blank
   
Demonstrates encapsulation by keeping validation logic within the class


### QuizManager Class (quiz_manager.py)
Acts as a factory for creating quiz instances and managing question data.

Key Features:

- Loads questions from CSV file
- Creates Question objects from raw data
- Provides Quiz instances on demand
- Centralises data loading logic
Workflow:

manager = QuizManager("questions.csv")
quiz = manager.create_quiz()  # Returns a Quiz with loaded questions


### UI Modules
The application uses separate modules for each screen:

- welcome_page.py - User registration and validation
- quiz_page.py - Main quiz interface with question display
- quiz_complete.py - Results screen with detailed feedback
- main.py - Application controller managing screen flow


### OOP Principles Applied

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

The tests are organised into two main categories:

**1. Unit Tests**

These tests focus on individual classes and their core behaviour.

Question Class

- Validates correct answer checking
- Confirms incorrect answers are properly detected

Quiz Class

- Verifies answers are recorded accurately
- Tests quiz completion logic
Confirms score calculation is correct

User Class

- Enforces name validation rules
- Tests both valid and invalid input scenarios

QuizManager

- Verifies CSV data loading
- Tests quiz instance creation

**2. Smoke Tests**

These tests confirm that the application can start and run without critical failures.

They check:

- CSV file availability
- Data loading functionality
- Basic end-to-end workflow execution

**Test Coverage**

The test suite provides coverage for:

- All core classes (Question, Quiz, User, QuizManager)
- Key business logic (validation rules, scoring, completion checks)
- Data loading and handling
- Basic integration across components

Together, these tests help ensure reliability, prevent regressions, and confirm that major features work as intended.

    Expected Test Output
    ......
    ----------------------------------------------------------------------
    Ran 6 tests in 0.XXXs

    OK



## DOCUMENTATION

This guide will help you run the Cyber Security Quiz application on your local computer.

Prerequisites
You need Python installed on your computer. 
Check if you have it by opening your terminal (Command Prompt on Windows, Terminal on Mac/Linux) and typing:

    python --version
    
You should see something like Python 3.8.0 or higher. If not, download Python from python.org.

### Installation Steps

Step 1: Download the Application
Download all the project files to a folder on your computer.

Step 2: Open Terminal in Project Folder
Windows: Open the folder, then type cmd in the address bar and press Enter
Mac/Linux: Right-click the folder and select "Open Terminal Here" (or navigate using cd command)

Step 3: Install Required Packages
Copy and paste this command into your terminal and press Enter:

    pip install streamlit
    
Wait for the installation to complete. You'll see a success message when it's done.

Running the Application

## Start the Quiz

In your terminal, type this command and press Enter:

    streamlit run main.py

What Happens Next:

- Your web browser will automatically open
- You'll see the quiz welcome screen
- If the browser doesn't open automatically, look for a URL in the terminal (usually http://localhost:8501) and copy it into your browser


## Using the Quiz

Step 1: Enter Your Name in the text box
    Your name must be between 3 and 19 characters
    No numbers allowed
    Click "Start Quiz" when ready
   
Step 2: Answer Questions
    Read each question carefully
    Select one answer by clicking the radio button
    You must answer all questions before submitting
    
Step 3: Submit and View Results
    Click "Submit Quiz" when you've answered all questions
    See your score and percentage
    Review which questions you got right or wrong
    Your results are automatically saved to quiz_results.csv
    
Step 4: Restart (Optional)
    Click "Restart Quiz" to take the quiz again
    You can take the quiz as many times as you like
    Stopping the Application
    
To stop the quiz application:

Go back to your terminal window
Press Ctrl + C (Windows/Linux) or Cmd + C (Mac)
The application will shut down

## EVALUATION

This README is designed for two types of readers:

- Developers who want to understand how the code works and possibly extend it.
- End users who want clear instructions on how to run the application.

The Development section explains the structure of the project and how the parts fit together, without going too deep into unnecessary technical detail.

The Documentation section focuses on clarity. It uses simple language and step-by-step guidance so anyone — regardless of technical experience — can get the app up and running.

The Testing section connects both groups. It explains what is being tested and how to run the tests, so developers can verify functionality and users can confirm everything works properly.

Overall, this documentation walks through the entire lifecycle of the project — from setup and development to testing and usage — giving a clear and practical guide for anyone using or building on this application.

Please refer to each file to gage a better understanding of the contents of the application.

**Thank you for taking the time to read through this documentation — your interest and time are truly appreciated!**
