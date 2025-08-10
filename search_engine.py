import os
from typing import Dict, List
from normalize_text import normalize_text
from data_structure import AutoCompleteData


class SearchEngine:
    def __init__(self):
        self.inverted_index: Dict[str, List[AutoCompleteData]] = {}

    def initialize_index(self, folder_path: str):
        """
        Initializes the inverted index by processing all text files in a given folder.

        Args:
            folder_path: The path to the folder containing the text files.
        """
        print("Starting index initialization...")
        for root, _, files in os.walk(folder_path):
            for filename in files:
                if filename.endswith(".txt"):
                    file_path = os.path.join(root, filename)
                    self._process_file(file_path)
        print("Index initialization completed.")

    def _process_file(self, file_path: str):
        """
        Processes a single file, line by line, to populate the inverted index.
        """
        print(f"Processing file: {file_path}")
        with open(file_path, 'r', encoding='utf-8') as current_file:
            for offset, line in enumerate(current_file):
                line = line.strip()
                if line:  # Skip empty lines
                    tokens = normalize_text(line)

                    # Create object AutoCompleteData
                    data_entry = AutoCompleteData(
                        completed_sentence=line,
                        source_text=file_path,
                        offset=offset,
                        score=0  # Score can be calculated based on your criteria
                    )

                    # Add tokens to the inverted index
                    for token in tokens:
                        if token not in self.inverted_index:
                            self.inverted_index[token] = []
                        self.inverted_index[token].append(data_entry)


if __name__ == "__main__":
    search_engine = SearchEngine()

    search_engine.initialize_index("students_materials/temp")

    # כעת, האינדקס ההפוך מוכן לשימוש!
    print("\n--- Inverted Index Sample ---")
    print("Tokens for 'mendel':")
    for item in search_engine.inverted_index.get('mendel', []):
        print(f"  - Sentence: '{item.completed_sentence}', File: '{item.source_text}', Offset: {item.offset}")

    print("\n--- Inverted Index Sample ---")
    print("Tokens for 'לבחון':")
    # To demonstrate that the word "examine" is not here
    print(search_engine.inverted_index.get('לבחון', 'Not found'))
