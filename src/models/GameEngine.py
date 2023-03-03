class GameEngine:

    def __init__(self):
        self.target_word = ""

    def char_validation(self, entered_input: str) -> bool:
        """
        Validates that the input is alphabetical.
        :param entered_input: char to validate
        :raises ValueError: if non-alphabetical input is provided
        :return: True if the char is alphabetical
        """
        if entered_input.isalpha():
            return True
        raise ValueError

    def word_validation(self, entered_input: str) -> bool:
        """

        :param entered_input: word to validate
        :return: True if word is valid, else False
        """
        target_word_length = len(self.target_word)
        if len(entered_input) == target_word_length:
            if not entered_input.isalpha():
                raise ValueError
            return True
        return False
