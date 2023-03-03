import json
from random import randrange


class GameEngine:

    def get_word(self) -> str:
        """Get a random word from other/words.json"""
        try:
            with open('../src/other/words.json') as file_handle:
                words = json.load(file_handle)
                return words[f'{randrange(len(words) - 1)}']
        except IOError as e:
            print(f'Error opening file: {e}')
