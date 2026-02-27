import csv
from question_class import Question
from quiz import Quiz


class QuizManager:
    """
    QuizManager class acts as the “manager” for all quiz‑related data and is responsible for loading questions, creating quiz objects, and keeping track of how many questions are available.
    """
    
    def __init__(self, csv_file="questions.csv"):
        """
        Initialize QuizManager with a CSV file path.
        
        Args:
            csv_file: Path to the CSV file containing questions
        """
        self.csv_file = csv_file
        self.questions = []
    
    def load_questions(self):
        """
        Load questions from CSV file and create Question objects.
        
        Returns:
            list: List of Question objects
        """
        self.questions = []
        
        with open(self.csv_file, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                question_obj = Question(
                    text=row["question"],
                    options=[
                        row["option_a"],
                        row["option_b"],
                        row["option_c"]
                    ],
                    correct_index=int(row["correct"]) - 1
                )
                
                self.questions.append(question_obj)
        
        return self.questions
    
    def create_quiz(self):
        """
        Create a new Quiz instance with loaded questions.
        
        Returns:
            Quiz: A new Quiz object
        """
        if not self.questions:
            self.load_questions()
        
        return Quiz(self.questions)
    
    def get_question_count(self):
        """
        Get the total number of questions available.
        
        Returns:
            int: Number of questions
        """
        if not self.questions:
            self.load_questions()
        
        return len(self.questions)


