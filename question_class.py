
"""
   This module defines a Question class that represents a single quiz question, 
   storing the question text, a list of answer options, and the index of the correct answer. 
   It provides a simple method, is_correct, which checks whether the user’s chosen answer matches the correct option.
"""



class Question:
    def __init__(self, text, options, correct_index):
        self.text = text
        self.options = options
        self.correct_index = correct_index

    def is_correct(self, answer):
        return answer == self.options[self.correct_index]

