import csv
from datetime import datetime


class Quiz:
    """
    Quiz class to manage quiz state, questions, and user answers.
    Encapsulates all quiz logic in one place.
    """
    
    def __init__(self, questions):
        """
        Initialize a Quiz with a list of Question objects.
        
        Args:
            questions: List of Question objects
        """
        self.questions = questions
        self.user_answers = {}
    
    def answer_question(self, question_index, answer):
        """
        Store a user's answer for a specific question.
        
        Args:
            question_index: Index of the question being answered
            answer: The user's selected answer
        """
        self.user_answers[question_index] = answer
    
    def calculate_score(self):
        """
        Calculate the total score based on correct answers.
        
        Returns:
            int: Number of correct answers
        """
        score = 0
        for index, question in enumerate(self.questions):
            user_answer = self.user_answers.get(index)
            if user_answer and question.is_correct(user_answer):
                score += 1
        return score
    
    def get_total_questions(self):
        """
        Get the total number of questions in the quiz.
        
        Returns:
            int: Total number of questions
        """
        return len(self.questions)
    
    def is_complete(self):
        """
        Check if all questions have been answered.
        
        Returns:
            bool: True if all questions answered, False otherwise
        """
        return len(self.user_answers) == len(self.questions)
    
    def get_result_for_question(self, question_index):
        """
        Get the result (correct/incorrect) for a specific question.
        
        Args:
            question_index: Index of the question
            
        Returns:
            dict: Contains 'is_correct', 'user_answer', and 'correct_answer'
        """
        question = self.questions[question_index]
        user_answer = self.user_answers.get(question_index)
        correct_answer = question.options[question.correct_index]
        
        return {
            'is_correct': question.is_correct(user_answer) if user_answer else False,
            'user_answer': user_answer,
            'correct_answer': correct_answer
        }
    
    def save_results_to_csv(self, username, csv_file="quiz_results.csv"):
        """
        Save quiz results to a CSV file.
        
        Args:
            username: Name of the user who took the quiz
            csv_file: Path to the CSV file (default: quiz_results.csv)
        """
        score = self.calculate_score()
        total = self.get_total_questions()
        percentage = (score / total * 100) if total > 0 else 0
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Check if file exists to determine if we need to write headers
        file_exists = False
        try:
            with open(csv_file, 'r'):
                file_exists = True
        except FileNotFoundError:
            pass
        
        # Write results to CSV
        with open(csv_file, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            
            # Write header if file is new
            if not file_exists:
                writer.writerow(['Timestamp', 'Username', 'Score', 'Total Questions', 'Percentage'])
            
            # Write result row
            writer.writerow([timestamp, username, score, total, f"{percentage:.1f}%"])


