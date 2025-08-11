def calculate_score(input_len, change_type, change_pos):
    """Calculates the score based on the type and position of a change."""
    base_score = input_len * 2

    # No change needed
    if change_type == 'perfect':
        return base_score

    # Penalties for substitution
    if change_type == 'substitute':
        if change_pos < 5:
            penalty = 5 - change_pos
            return base_score - penalty if penalty > 1 else base_score - 1
        return base_score - 1

    # Penalties for deletion or insertion
    if change_type in ('delete', 'insert'):
        if change_pos < 4:
            return base_score - (10 - 2 * change_pos)
        return base_score - 2

    return 0  # Should not happen


def find_best_match_in_sentence(user_input, sentence_text):
    """
    Finds the best possible match for the user_input within a single sentence.
    Checks for a perfect match first, then for a 1-mistake fuzzy match.
    Returns the score and the matched substring.
    """
    lower_sentence = sentence_text.lower()

    # 1. Check for a perfect match
    if user_input in lower_sentence:
        return calculate_score(len(user_input), 'perfect', -1), user_input

    # 2. If no perfect match, check for fuzzy matches (1 mistake)
    best_fuzzy_score = -1
    best_fuzzy_match = ""

    # Generate all possible 1-mistake variations
    alphabet = 'abcdefghijklmnopqrstuvwxyz '

    # Deletions
    for i in range(len(user_input)):
        variation = user_input[:i] + user_input[i + 1:]
        if variation in lower_sentence:
            score = calculate_score(len(user_input), 'delete', i)
            if score > best_fuzzy_score:
                best_fuzzy_score = score
                best_fuzzy_match = variation

    # Substitutions
    for i in range(len(user_input)):
        for char in alphabet:
            variation = user_input[:i] + char + user_input[i + 1:]
            if variation in lower_sentence:
                score = calculate_score(len(user_input), 'substitute', i)
                if score > best_fuzzy_score:
                    best_fuzzy_score = score
                    best_fuzzy_match = variation

    # Insertions
    for i in range(len(user_input) + 1):
        for char in alphabet:
            variation = user_input[:i] + char + user_input[i:]
            if len(variation) > len(user_input) + 1: continue  # Should not happen, but for safety
            if variation in lower_sentence:
                score = calculate_score(len(user_input), 'insert', i)
                if score > best_fuzzy_score:
                    best_fuzzy_score = score
                    best_fuzzy_match = variation

    if best_fuzzy_score != -1:
        return best_fuzzy_score, best_fuzzy_match

    return -1, ""  # No match found