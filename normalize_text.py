import re
import string


def normalize_text(text: str) -> list:
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

    return text.split()

# example:
# text = "היום 3945הוא. .יום     111 יפה"
# tokens = normalize_text(text)
# print(tokens)
# # Output: ['היום', 'הוא', 'יום', 'יפה']
