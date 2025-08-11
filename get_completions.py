from normalize_text import normalize_text
from data_structure import AutoCompleteData
from scoring import find_best_match_in_sentence


def get_completions(user_input, sentence_store, inverted_index):
    """
    Finds and scores the top 5 completions for the user's input.
    This is the complete, working version.
    """
    # 1. Normalize the user's input
    clean_user_input = " ".join(normalize_text(user_input))
    if not clean_user_input:
        return []

    # 2. Find candidate sentences using the inverted index
    # We use the first word of the query to get a list of potential sentences.
    first_word = clean_user_input.split()[0]
    candidate_ids = inverted_index.get(first_word, [])

    # 3. Iterate through candidates, score them, and collect results
    results = []
    for sentence_id in candidate_ids:
        file_path, line_num, original_sentence = sentence_store[sentence_id]

        # This helper function finds the best match (perfect or fuzzy)
        # within the current sentence.
        score, matched_substring = find_best_match_in_sentence(clean_user_input, original_sentence)

        # If a match was found (score is not -1), add it to our results
        if score != -1:
            results.append(AutoCompleteData(original_sentence, file_path, line_num, score))

    # 4. Sort all found results and return the top 5
    # Sort by score (high to low), then alphabetically for ties
    results.sort(key=lambda item: (-item.score, item.completed_sentence))

    # Return only the top 5 results
    return results[:5]