import unittest
from collections import defaultdict


from get_completions import get_completions
from normalize_text import normalize_text


class TestCompletion(unittest.TestCase):

    def setUp(self):
        """
        This method sets up a mini "database" for our tests.
        It runs before each test function.
        """
        self.sentence = "To be or not to be, that is the question."
        self.source = 'hamlet.txt'
        self.offset = 1

        # 1. Create the Sentence Store
        self.sentence_store = [(self.source, self.offset, self.sentence)]

        # 2. Create the Inverted Index
        self.inverted_index = defaultdict(list)
        normalized_words = normalize_text(self.sentence)
        for word in normalized_words:
            if 0 not in self.inverted_index[word]:
                self.inverted_index[word].append(0)  # Sentence ID is 0

    def test_perfect_match(self):
        """Tests a perfect, exact match of a substring."""
        print("\nTesting: Perfect Match")
        query = "that is the question"
        results = get_completions(query, self.sentence_store, self.inverted_index)

        self.assertEqual(len(results), 1)  # Should find exactly one result
        self.assertEqual(results[0].completed_sentence, self.sentence)
        # Score = len(query) * 2 = 20 * 2 = 40
        self.assertEqual(results[0].score, 40)

    def test_substitution_typo(self):
        """Tests a typo with one character substituted."""
        print("Testing: Substitution Typo")
        # 'qeestion' instead of 'question'. Mistake at pos 16 ('e')
        query = "that is the qeestion"
        results = get_completions(query, self.sentence_store, self.inverted_index)

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].completed_sentence, self.sentence)
        # Base score = len(query) * 2 = 20 * 2 = 40
        # Penalty for substitution at pos > 4 is -1
        # Final Score = 40 - 1 = 39
        self.assertEqual(results[0].score, 39)

    def test_deletion_typo(self):
        """Tests a typo with one character deleted."""
        print("Testing: Deletion Typo")
        # 'questin' instead of 'question'. 'o' is missing at pos 16
        query = "that is the questin"
        results = get_completions(query, self.sentence_store, self.inverted_index)

        self.assertEqual(len(results), 1)
        # Base score = len(query) * 2 = 19 * 2 = 38
        # Penalty for deletion at pos > 4 is -2
        # Final Score = 38 - 2 = 36
        self.assertEqual(results[0].score, 36)

    def test_insertion_typo(self):
        """Tests a typo with one character inserted."""
        print("Testing: Insertion Typo")
        # 'questiion' instead of 'question'. Extra 'i' inserted at pos 17
        query = "that is the questiion"
        results = get_completions(query, self.sentence_store, self.inverted_index)

        self.assertEqual(len(results), 1)
        # Base score = len(query) * 2 = 21 * 2 = 42
        # Penalty for insertion at pos > 4 is -2
        # Final Score = 42 - 2 = 40
        self.assertEqual(results[0].score, 40)

    def test_case_insensitivity(self):
        """Tests that the search is case-insensitive."""
        print("Testing: Case-Insensitivity")
        query = "TO BE OR NOT"
        results = get_completions(query, self.sentence_store, self.inverted_index)

        self.assertEqual(len(results), 1)
        # Score = len("to be or not") * 2 = 12 * 2 = 24
        self.assertEqual(results[0].score, 24)

    def test_no_match(self):
        """Tests a query that should not match anything."""
        print("Testing: No Match")
        query = "a midsummer night's dream"
        results = get_completions(query, self.sentence_store, self.inverted_index)

        self.assertEqual(len(results), 0)  # Should find no results


# This makes the script runnable
if __name__ == '__main__':
    unittest.main()