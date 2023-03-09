import os
import sys
import unittest

from src.models.GameEngine import GameEngine

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class TestGameEngine(unittest.TestCase):

    def setUp(self):
        """ Creates an instance of GameEngine before each test. """
        self.game_engine = GameEngine()

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
        self.assertIsInstance(self.game_engine.find_char_index("r"), list)

    def test_find_char_index_returns_single_match(self):
        """Tests that find_char_index returns a list with a single index"""
        char = "r"
        self.game_engine.target_word = "letter"
        self.assertEqual(self.game_engine.find_char_index(char), [5])

    def test_find_char_index_returns_multiple_matches(self):
        """Tests that find_char_index returns a list with multiple indexes"""
        char = "t"
        self.game_engine.target_word = "letter"
        self.assertEqual(self.game_engine.find_char_index(char), [2, 3])

    def test_find_char_index_returns_empty_list(self):
        """Tests that find_char_index returns an empty list"""
        char = "z"
        self.game_engine.target_word = "letter"
        self.assertEqual(self.game_engine.find_char_index(char), [])

    def test_char_in_target_word(self):
        """Tests that char_in_target_word returns a boolean"""
        result = self.game_engine.char_in_target_word("a")
        self.assertIsInstance(result, bool, "char_in_target_word should return a boolean")

    def test_char_in_target_word_correct(self):
        """Tests that char_in_target_word returns True if the character is in the target word"""
        self.game_engine.target_word = "test"
        result = self.game_engine.char_in_target_word("t")
        self.assertTrue(result, "char_in_target_word should return True if the character is in the target word")

    def test_char_in_target_word_incorrect(self):
        """Tests that char_in_target_word returns False if the character is not in the target word"""
        self.game_engine.target_word = "test"
        result = self.game_engine.char_in_target_word("w")
        self.assertFalse(result or result is None,
                         "char_in_target_word should return False if the character is not in the target word")

    def test_word_matches_target_word(self):
        """Tests that word_matches_target_word returns a boolean"""
        result = self.game_engine.word_matches_target_word("test")
        self.assertIsInstance(result, bool, "word_matches_target_word should return a boolean")

    def test_word_matches_target_word_correct(self):
        """Tests that word_matches_target_word returns True if the word matches the target word"""
        self.game_engine.target_word = "test"
        result = self.game_engine.word_matches_target_word("test")
        self.assertTrue(result, "word_matches_target_word should return True if the word matches the target word")

    def test_word_matches_target_word_incorrect(self):
        """Tests that word_matches_target_word returns False if the word does not match the target word"""
        self.game_engine.target_word = "test"
        result = self.game_engine.word_matches_target_word("west")
        self.assertFalse(result or result is None,
                         "word_matches_target_word should return False if the word does not match the target word")

    def test_char_validation_positive(self):
        """ Valid single-character input should return true. """
        value = "a"
        result = self.game_engine.char_validation(value)
        self.assertTrue(result, "a should be a valid input.")

    def test_char_validation_negative(self):
        """ Invalid single-character input should throw ValueError"""
        value = "3"
        self.assertRaises(ValueError, self.game_engine.char_validation, value)

    def test_word_validation_positive(self):
        """ Valid words with the same length as target_word returns true """
        guess_word = "test"
        self.game_engine.target_word = guess_word
        result = self.game_engine.word_validation(guess_word)
        self.assertTrue(result,
                        f"{guess_word} should be valid because it is same length as {self.game_engine.target_word}.")

    def test_number_word_validation_negative(self):
        """ Invalid words including numbers throws ValueError """
        number_word = "tes2"
        target_word = "test"
        self.game_engine.target_word = target_word
        self.assertRaises(ValueError, self.game_engine.char_validation, number_word)

    def test_short_word_validation_negative(self):
        """ Invalid words of the wrong length returns false """
        short_word = "tes"
        target_word = "test"
        self.game_engine.target_word = target_word
        result = self.game_engine.word_validation(short_word)
        self.assertFalse(result, f"{short_word} should be invalid because it is shorter than {target_word}.")

    def test_generate_word_list(self):
        """Generated word_progress is the same length as the target_word"""
        self.game_engine.target_word = self.game_engine.get_word()
        self.game_engine.generate_word_list()
        self.assertTrue(len(self.game_engine.word_progress) == len(self.game_engine.target_word))

    def test_store_guessed_char_guessed_contains_letter(self):
        """ Letter gets stored in guessed letters """
        char = "t"
        self.game_engine.store_guessed_char(char, [])
        self.assertTrue(char in self.game_engine.guessed_characters,
                        "store_guessed_char should insert the letter to guessed_characters.")

    def test_store_guessed_char_matched_contains_letter(self):
        """ Letter gets stored in word_progress """
        char = "t"
        self.game_engine.word_progress = ["_", "_", "_", "_", "_", "_"]
        self.game_engine.store_guessed_char(char, [2, 3])
        self.assertTrue(char in self.game_engine.word_progress,
                        "store_guessed_char should insert the letter to word_progress.")

    def test_store_guessed_char_matched_letter_count(self):
        """ Letter gets stored in word_progress the correct amount of times """
        char = "t"
        self.game_engine.word_progress = ["_", "_", "_", "_", "_", "_"]
        self.game_engine.store_guessed_char(char, [2, 3])
        result = self.game_engine.word_progress.count(char)
        self.assertEqual(2, result, "store_guessed_char should insert the letter two times.")

    def test_store_guessed_char_matched_letter_count_none(self):
        """ Letter is not stored in word_progress if empty list is provided """
        char = "t"
        self.game_engine.word_progress = ["_", "_", "_", "_", "_", "_"]
        self.game_engine.store_guessed_char(char, [])
        result = self.game_engine.word_progress.count(char)
        self.assertEqual(0, result, "store_guessed_char should insert the letter two times.")

    def test_store_guessed_char_matched_letter_index(self):
        """ Letter gets stored in the correct position in word_progress """
        char = "t"
        self.game_engine.word_progress = ["_", "_", "_", "_", "_", "_"]
        self.game_engine.store_guessed_char(char, [2, 3])
        result = self.game_engine.word_progress[2] == char and self.game_engine.word_progress[3] == char
        self.assertTrue(result, "store_guessed_char should insert the letter to word_progress index 2 and 3.")

    def test_make_guess_char_returns_word_progress_no_match(self):
        """ Non-matching char returns non-modified version of word progress """
        char = "m"
        clean_progress = ["_", "_", "_", "_", "_", "_"]
        target_word = "letter"
        self.game_engine.target_word = target_word
        self.game_engine.word_progress = clean_progress.copy()
        result = self.game_engine.make_guess(char)
        self.assertEqual(result, clean_progress,
                         "make_guess should not return modified word progress on non-matching chars")

    def test_make_guess_char_increments_guesses_counter_no_match(self):
        """ The guesses counter should be incremented on no match guesses """
        char = "m"
        target_word = "letter"
        self.game_engine.target_word = target_word
        self.game_engine.guesses = 0
        self.game_engine.make_guess(char)
        self.assertEqual(1, self.game_engine.guesses, "make_guess should increment guesses counter if no match")

    def test_make_guess_char_returns_updated_word_progress_match(self):
        """ Matching char returns modified version of word progress """
        char = "t"
        clean_progress = ["_", "_", "_", "_", "_", "_"]
        target_word = "letter"
        self.game_engine.target_word = target_word
        self.game_engine.word_progress = clean_progress.copy()
        result = self.game_engine.make_guess(char)
        self.assertNotEqual(result, clean_progress, "make_guess should return modified word progress on matching chars")

    def test_make_guess_char_guesses_counter_match(self):
        """ The guesses counter should be incremented on no match guesses """
        char = "t"
        target_word = "letter"
        self.game_engine.target_word = target_word
        self.game_engine.guesses = 0
        self.game_engine.make_guess(char)
        self.assertEqual(0, self.game_engine.guesses, "make_guess should not increment guesses counter if match")

    def test_make_guess_word_set_guesses_counter_to_max_on_no_match(self):
        """
         Guesses counter should have the same value as the max guesses if non-matching word is guessed """
        word = "test"
        target_word = "word"
        max_guesses = self.game_engine.max_guesses
        self.game_engine.target_word = target_word
        self.game_engine.guesses = 0
        self.game_engine.make_guess(word)
        self.assertEqual(max_guesses, self.game_engine.guesses,
                         "make_guess should set guesses counter to max if given non-matching word")

    def test_make_guess_word_fills_word_progress_on_match(self):
        """
         make_guess should return complete word progress on matching word """
        target_word = "word"
        clean_progress = ["_", "_", "_", "_"]
        result_progress = ["w", "o", "r", "d"]
        self.game_engine.word_progress = clean_progress.copy()
        self.game_engine.target_word = target_word
        result = self.game_engine.make_guess(target_word)
        self.assertEqual(result_progress, result, "make_guess should return complete word progress on matching word")

