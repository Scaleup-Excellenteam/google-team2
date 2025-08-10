import re
import string


def normalize_text(text: str) -> str:
    """
    Normalizes a given string by performing several cleaning steps.

    Args:
        text: The input string to normalize.

    Returns:
        The normalized string.
    """
    # 1. Convert to lowercase
    text = text.lower()

    # 2. Remove punctuation
    # string.punctuation holds all standard punctuation characters
    text = text.translate(str.maketrans('', '', string.punctuation))

    # 3. Remove numbers (optional, depending on your needs)
    text = re.sub(r'\d+', '', text)

    # 4. Remove extra whitespace
    text = " ".join(text.split())

    return text


# # Example usage:
# my_sentence = "היי! היום ה-13 במאי, 2024, הוא יום יפה... מאוד."
# normalized_sentence = normalize_text(my_sentence)
# print(f"Original: '{my_sentence}'")
# print(f"Normalized: '{normalized_sentence}'")

# Expected output:
# Original: 'היי! היום ה-13 במאי, 2024, הוא יום יפה... מאוד.'
# Normalized: 'היי היום ה במאי הוא יום יפה מאוד'


def tokenize_text(text: str) -> list[str]:
    """
    Splits a normalized string into a list of individual words (tokens).

    Args:
        text: The normalized input string.

    Returns:
        A list of words.
    """
    return normalize_text(text).split()


# דוגמה לשימוש:
normalized_text = "היום 3945הוא. .יום     111 יפה"
tokens = tokenize_text(normalized_text)
print(tokens)
# Output: ['היום', 'הוא', 'יום', 'יפה']