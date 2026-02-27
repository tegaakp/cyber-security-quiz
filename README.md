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

# Main.py

This is the main module forming the central organiser of all modules  It coordinates navigation, initialises core objects, and manages application state using Streamlit’s session system. When the app runs, this file decides what happens next.

This is the desired flow:

     Welcome → Quiz → End

Imported dependencies 

      import streamlit as st
      from welcome_page import show_welcome_screen
      from quiz_manager import QuizManager
      from quiz_page import show_quiz_screen
      from quiz_complete import show_end_screen


## TESTING

## DOCUMENTATION

## EVALUATION
