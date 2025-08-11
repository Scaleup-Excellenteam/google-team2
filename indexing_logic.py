
def add_to_sentence_store(sentence_store_list, file_path, line_num, original_sentence):
    """Adds sentence data to the store and returns its new ID."""
    new_id = len(sentence_store_list)
    sentence_store_list.append((file_path, line_num, original_sentence))
    return new_id


def update_inverted_index(inverted_index_dict, normalized_words, sentence_id):
    """Updates the inverted index using sets for high performance."""
    for word in normalized_words:
        inverted_index_dict[word].add(sentence_id)

