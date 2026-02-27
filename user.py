class User:
    """
    User class to represent a quiz participant.
   This module defines a User class that represents a quiz participant and stores their name securely.
    It includes built‑in validation rules to ensure the name is acceptable, such as checking length and preventing numbers. 
    The class also provides clean string representations, making it easy to display or debug user information throughout the application.

    This module represents encapsulation as a method of OOP as user validation logic is under this class.
    """
    
    def __init__(self, name=""):
        """
        Initialize a User with a name.
        
        Args:
            name: The user's name (default: empty string)
        """
        self._name = name
    

    def validate_name(self):
        """
        Validate the user's name according to business rules.
        
        Returns:
            tuple: (is_valid: bool, error_message: str)
        """
        if not self._name:
            return False, "Name cannot be blank."
        
        if len(self._name) < 3 or len(self._name) > 19:
            return False, "Name must be between 3 and 19 characters."
        
        if any(char.isdigit() for char in self._name):
            return False, "Name cannot contain numbers."
        
        return True, ""
    
    def is_valid(self):
        """
        Check if the user's name is valid.
        
        Returns:
            bool: True if valid, False otherwise
        """
        is_valid, _ = self.validate_name()
        return is_valid
    
  

