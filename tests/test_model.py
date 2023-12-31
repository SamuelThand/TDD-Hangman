import os
import sys
import unittest

from src.models.GameEngine import GameEngine

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class TestGameEngine(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        """Creates a GameEngine instance for the tests"""
        cls.game_engine = GameEngine()
        cls.character_r = 'r'
        cls.character_t = 't'
        cls.character_z = 'z'
        cls.character_w = 'w'
        cls.word_letter = 'letter'
        cls.word_west = 'west'
        cls.number_1 = '1'
        cls.word_letter_clean_progress = ["_", "_", "_", "_", "_", "_"]

    def test_has_target_word(self):
        """Tests that the target_word field exists."""
        self.assertTrue(hasattr(self.game_engine, 'target_word'))

    def test_has_word_progress(self):
        """Tests that the word_progress field exists."""
        self.assertTrue(hasattr(self.game_engine, 'word_progress'))

    def test_has_guessed_characters(self):
        """Tests that the guessed_characters field exists."""
        self.assertTrue(hasattr(self.game_engine, 'guessed_characters'))

    def test_has_max_guesses(self):
        """Tests that the max_guesses field exists."""
        self.assertTrue(hasattr(self.game_engine, 'max_guesses'))

    def test_has_guesses(self):
        """Tests that the guesses field exists."""
        self.assertTrue(hasattr(self.game_engine, 'guesses'))

    def test_start_game(self):
        """Tests that the start_game method exists."""
        self.assertTrue(hasattr(self.game_engine, 'start_game') and
                        callable(getattr(self.game_engine, 'start_game')))

    def test_game_over(self):
        """Tests that the game_over method exists."""
        self.assertTrue(hasattr(self.game_engine, 'game_over') and
                        callable(getattr(self.game_engine, 'game_over')))

    def test_victory(self):
        """Tests that the victory method exists."""
        self.assertTrue(hasattr(self.game_engine, 'victory') and
                        callable(getattr(self.game_engine, 'victory')))

    def test_game_over_works(self):
        """Tests that the game over method returns true for 8 guesses."""
        self.game_engine.guesses = 8
        self.assertTrue(self.game_engine.game_over())

    def test_victory_works(self):
        """Tests that the victory method returns true if the target_word and word_progress joined matches."""
        self.game_engine.start_game()
        self.game_engine.word_progress = list(self.game_engine.target_word)

        self.assertTrue(self.game_engine.victory())

    def test_get_word_returns_word(self):
        """Tests that get_word returns a string"""
        game_engine = GameEngine()
        self.assertIsInstance(game_engine.get_word(), str)

    def test_get_word_length_nonempty_non_negative(self):
        """Tests that get_word returns a word that is nonempty/non-negative"""
        game_engine = GameEngine()
        self.assertFalse(len(game_engine.get_word()) <= 0)

    def test_instance(self):
        game_engine_instance = GameEngine()
        self.assertIsInstance(game_engine_instance, GameEngine)

    def test_find_char_index(self):
        """Tests that find_char_index returns a list"""
        self.assertIsInstance(self.game_engine.find_char_index(self.character_t), list)

    def test_find_char_index_returns_single_match(self):
        """Tests that find_char_index returns a list with a single index"""
        self.game_engine.target_word = self.word_letter
        self.assertEqual(self.game_engine.find_char_index(self.character_r), [5])

    def test_find_char_index_returns_multiple_matches(self):
        """Tests that find_char_index returns a list with multiple indexes"""
        self.game_engine.target_word = self.word_letter
        self.assertEqual(self.game_engine.find_char_index(self.character_t), [2, 3])

    def test_find_char_index_returns_empty_list(self):
        """Tests that find_char_index returns an empty list"""
        self.game_engine.target_word = self.word_letter
        self.assertEqual(self.game_engine.find_char_index(self.character_z), [])

    def test_char_in_target_word(self):
        """Tests that char_in_target_word returns a boolean"""
        result = self.game_engine.char_in_target_word(self.character_t)
        self.assertIsInstance(result, bool, "char_in_target_word should return a boolean")

    def test_char_in_target_word_correct(self):
        """Tests that char_in_target_word returns True if the character is in the target word"""
        self.game_engine.target_word = self.word_letter
        result = self.game_engine.char_in_target_word(self.character_t)
        self.assertTrue(result, "char_in_target_word should return True if the character is in the target word")

    def test_char_in_target_word_incorrect(self):
        """Tests that char_in_target_word returns False if the character is not in the target word"""
        self.game_engine.target_word = self.word_letter
        result = self.game_engine.char_in_target_word(self.character_w)
        self.assertFalse(result or result is None,
                         "char_in_target_word should return False if the character is not in the target word")

    def test_word_matches_target_word(self):
        """Tests that word_matches_target_word returns a boolean"""
        result = self.game_engine.word_matches_target_word(self.word_letter)
        self.assertIsInstance(result, bool, "word_matches_target_word should return a boolean")

    def test_word_matches_target_word_correct(self):
        """Tests that word_matches_target_word returns True if the word matches the target word"""
        self.game_engine.target_word = self.word_letter
        result = self.game_engine.word_matches_target_word(self.word_letter)
        self.assertTrue(result, "word_matches_target_word should return True if the word matches the target word")

    def test_word_matches_target_word_incorrect(self):
        """Tests that word_matches_target_word returns False if the word does not match the target word"""
        self.game_engine.target_word = self.word_letter
        result = self.game_engine.word_matches_target_word(self.word_west)
        self.assertFalse(result or result is None,
                         "word_matches_target_word should return False if the word does not match the target word")

    def test_char_validation_positive(self):
        """ Valid single-character input should return true. """
        value = self.character_t
        result = self.game_engine.char_validation(value)
        self.assertTrue(result, "a should be a valid input.")

    def test_char_validation_negative(self):
        """ Invalid single-character input should throw ValueError"""
        self.assertRaises(ValueError, self.game_engine.char_validation, self.number_1)

    def test_word_validation_positive(self):
        """ Valid words with the same length as target_word returns true """
        self.game_engine.target_word = self.word_letter
        result = self.game_engine.word_validation(self.word_letter)
        self.assertTrue(result,
                        f"{self.word_letter} should be valid "
                        f"because it is same length as {self.game_engine.target_word}.")

    def test_number_word_validation_negative(self):
        """ Invalid words including numbers throws ValueError """
        self.assertRaises(ValueError, self.game_engine.char_validation, self.word_letter + self.number_1)

    def test_short_word_validation_negative(self):
        """ Invalid words of the wrong length throws exception """
        self.game_engine.target_word = self.word_letter
        self.assertRaises(Exception, self.game_engine.word_validation, self.word_letter[:-1])

    def test_generate_word_list(self):
        """Generated word_progress is the same length as the target_word"""
        self.game_engine.target_word = self.game_engine.get_word()
        self.game_engine.generate_word_list()
        self.assertTrue(len(self.game_engine.word_progress) == len(self.game_engine.target_word))

    def test_store_guessed_char_guessed_contains_letter(self):
        """ Letter gets stored in guessed letters """
        self.game_engine.store_guessed_char(self.character_t, [])
        self.assertTrue(self.character_t in self.game_engine.guessed_characters,
                        "store_guessed_char should insert the letter to guessed_characters.")

    def test_store_guessed_char_matched_contains_letter(self):
        """ Letter gets stored in word_progress """
        self.game_engine.word_progress = self.word_letter_clean_progress
        self.game_engine.store_guessed_char(self.character_t, [2, 3])
        self.assertTrue(self.character_t in self.game_engine.word_progress,
                        "store_guessed_char should insert the letter to word_progress.")

    def test_store_guessed_char_matched_letter_count(self):
        """ Letter gets stored in word_progress the correct amount of times """
        self.game_engine.word_progress = self.word_letter_clean_progress
        self.game_engine.store_guessed_char(self.character_t, [2, 3])
        result = self.game_engine.word_progress.count(self.character_t)
        self.assertEqual(2, result, "store_guessed_char should insert the letter two times.")

    def test_store_guessed_char_matched_letter_count_none(self):
        """ Letter is not stored in word_progress if empty list is provided """
        self.game_engine.store_guessed_char(self.character_t, [])
        result = self.game_engine.word_progress.count(self.character_t)
        self.assertEqual(0, result, "store_guessed_char should insert the letter two times.")

    def test_store_guessed_char_matched_letter_index(self):
        """ Letter gets stored in the correct position in word_progress """
        self.game_engine.word_progress = self.word_letter_clean_progress
        self.game_engine.store_guessed_char(self.character_t, [2, 3])
        result = \
            self.game_engine.word_progress[2] == \
            self.character_t and self.game_engine.word_progress[3] == self.character_t
        self.assertTrue(result, "store_guessed_char should insert the letter to word_progress index 2 and 3.")

    def test_make_guess_char_returns_word_progress_no_match(self):
        """ Non-matching char returns non-modified version of word progress """
        clean_progress = self.word_letter_clean_progress
        self.game_engine.target_word = self.word_letter
        self.game_engine.word_progress = clean_progress.copy()
        result = self.game_engine.make_guess(self.character_w)
        self.assertEqual(result, clean_progress,
                         "make_guess should not return modified word progress on non-matching chars")

    def test_make_guess_char_increments_guesses_counter_no_match(self):
        """ The guesses counter should be incremented on no match guesses """
        self.game_engine.target_word = self.word_letter
        self.game_engine.guesses = 0
        self.game_engine.make_guess(self.character_w)
        self.assertEqual(1, self.game_engine.guesses, "make_guess should increment guesses counter if no match")

    def test_make_guess_char_returns_updated_word_progress_match(self):
        """ Matching char returns modified version of word progress """
        clean_progress = self.word_letter_clean_progress
        self.game_engine.target_word = self.character_t
        self.game_engine.word_progress = clean_progress.copy()
        result = self.game_engine.make_guess(self.character_t)
        self.assertNotEqual(result, clean_progress, "make_guess should return modified word progress on matching chars")

    def test_make_guess_char_guesses_counter_match(self):
        """ The guesses counter should be incremented on no match guesses """
        clean_progress = self.word_letter_clean_progress
        self.game_engine.target_word = self.word_letter
        self.game_engine.word_progress = clean_progress.copy()
        self.game_engine.make_guess(self.character_t)
        self.assertEqual(0, self.game_engine.guesses, "make_guess should not increment guesses counter if match")

    def test_make_guess_word_set_guesses_counter_to_max_on_no_match(self):
        """Guesses counter should have the same value as the max guesses if non-matching word is guessed """
        max_guesses = self.game_engine.max_guesses
        self.game_engine.target_word = self.word_letter
        self.game_engine.make_guess(self.word_west + self.character_t * 2)
        self.assertEqual(max_guesses, self.game_engine.guesses,
                         "make_guess should set guesses counter to max if given non-matching word")

    def test_make_guess_word_fills_word_progress_on_match(self):
        """make_guess should return complete word progress on matching word """
        self.game_engine.word_progress = self.word_letter_clean_progress.copy()
        self.game_engine.target_word = self.word_letter
        result = self.game_engine.make_guess(self.word_letter)
        self.assertEqual(list(self.word_letter), result,
                         "make_guess should return complete word progress on matching word")

    def test_make_guess_char_already_guessed(self):
        """ Already guessed characters should not be used again """
        guesses = [self.character_t]
        self.game_engine.guessed_characters = guesses
        self.assertRaises(Exception, self.game_engine.make_guess, self.character_t)

    def tearDown(self) -> None:
        """Clean up the game_engine object after each test"""
        self.game_engine.target_word = ""
        self.game_engine.word_progress = []
        self.game_engine.guesses = 0
        self.game_engine.guessed_characters = []

    @classmethod
    def tearDownClass(cls) -> None:
        """Clean up the test class after testing"""
        cls.game_engine = None
        cls.character_r = None
        cls.character_t = None
        cls.character_z = None
        cls.character_w = None
        cls.word_letter = None
        cls.word_west = None
        cls.number_1 = None
        cls.word_letter_clean_progress = None
