# Module for smoke tests and unit tests to check if code works
import unittest
import os
from question_class import Question
from quiz import Quiz
from quiz_manager import QuizManager
from user import User


class TestQuestion(unittest.TestCase):
    """Test the Question class"""
    
    def test_question_works(self):
        """Test that Question class works"""
        q = Question("What is 2+2?", ["3", "4", "5"], 1)
        self.assertTrue(q.is_correct("4"))
        self.assertFalse(q.is_correct("3"))


class TestQuiz(unittest.TestCase):
    """Test the Quiz class"""
    
    def test_quiz_works(self):
        """Test that Quiz class works"""
        questions = [
            Question("Q1?", ["A", "B", "C"], 0),
            Question("Q2?", ["X", "Y", "Z"], 1)
        ]
        quiz = Quiz(questions)
        
        quiz.answer_question(0, "A")
        quiz.answer_question(1, "Y")
        
        self.assertTrue(quiz.is_complete())
        self.assertEqual(quiz.calculate_score(), 2)


class TestQuizManager(unittest.TestCase):
    """Test the QuizManager class"""
    
    def test_quiz_manager_works(self):
        """Test that QuizManager loads questions"""
        if os.path.exists("questions.csv"):
            manager = QuizManager()
            quiz = manager.create_quiz()
            self.assertGreater(len(quiz.questions), 0)


class TestUser(unittest.TestCase):
    """Test the User class"""
    
    def test_user_validation_works(self):
        """Test that User validation works"""
        valid_user = User("Alice")
        invalid_user = User("Al")
        
        self.assertTrue(valid_user.is_valid())
        self.assertFalse(invalid_user.is_valid())


class TestSmoke(unittest.TestCase):
    """Basic smoke tests"""
    
    def test_csv_exists(self):
        """Test that questions.csv exists"""
        self.assertTrue(os.path.exists("questions.csv"))
    
    def test_basic_workflow(self):
        """Test basic quiz workflow"""
        if os.path.exists("questions.csv"):
            manager = QuizManager()
            quiz = manager.create_quiz()
            
            # Answer first question
            quiz.answer_question(0, quiz.questions[0].options[0])
            
            # Check it works
            self.assertGreater(len(quiz.user_answers), 0)


if __name__ == "__main__":
    unittest.main()


