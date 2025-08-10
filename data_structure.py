from dataclasses import dataclass


@dataclass
class AutoCompleteData:
    """
    A container for a single autocomplete suggestion.

    Attributes:
        completed_sentence (str): The full, original sentence from the source file.
        source_text (str): The path to the source file (e.g., 'Archive/folder/file.txt').
        offset (int): The line number where the sentence was found.
        score (int): The calculated score for this match.
    """
    completed_sentence: str
    source_text: str
    offset: int
    score: int
