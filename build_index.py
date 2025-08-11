from collections import defaultdict

from dir_traversal import find_text_files
from normalize_text import normalize_text
from indexing_logic import add_to_sentence_store, update_inverted_index


def run_indexing(root_directory: str):
    """Finds all text files, processes them, and builds the search index and sentence store."""
    print("--- Starting Live Indexing Process (this may take a few minutes) ---")

    sentence_store = []
    inverted_index = defaultdict(set)  # Use set for performance

    file_paths = find_text_files(root_directory)
    total_files = len(file_paths)
    print(f"Found {total_files} files to index.")
    files_processed_count = 0

    for path in file_paths:
        try:
            with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                for line_num, line_content in enumerate(f, 1):
                    original_sentence = line_content.strip()
                    if not original_sentence:
                        continue
                    sentence_id = add_to_sentence_store(sentence_store, path, line_num, original_sentence)
                    normalized_words = normalize_text(original_sentence)
                    update_inverted_index(inverted_index, normalized_words, sentence_id)
        except Exception as e:
            print(f"Could not process file {path}: {e}")

        files_processed_count += 1
        if files_processed_count > 0 and files_processed_count % 100 == 0:
            print(f"  -> Processed {files_processed_count} / {total_files} files...")

    # Convert sets to lists for easier use in the online stage
    final_inverted_index = {word: list(ids) for word, ids in inverted_index.items()}

    print(f"--- Indexing Complete: {len(sentence_store)} sentences processed ---")
    return sentence_store, final_inverted_index




if __name__ == '__main__':
    ARCHIVE_ROOT = "students_materials/Archive"
    s_store, i_index = run_indexing(ARCHIVE_ROOT)
