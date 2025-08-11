import re


def normalize_text(text):
    """
    Cleans a string by lowercasing, removing punctuation, and standardizing whitespace.

    Args:
        text (str): The input sentence.

    Returns:
        list: A list of cleaned, normalized words.
    """
    # Convert to lowercase
    text = text.lower()

    # Remove all characters that are not letters, numbers, or whitespace
    text = re.sub(r'[^\w\s]', '', text)

    # Split the text into a list of words, which also handles all whitespace issues
    return text.split()