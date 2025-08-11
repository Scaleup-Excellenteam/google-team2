from build_index import run_indexing
from get_completions import get_completions


def run():
    """The main application loop for user interaction."""

    # 1. Load the data structures from the files
    #sentence_store, inverted_index = load_data()
    sentence_store, inverted_index = run_indexing("students_materials/archive")
    if sentence_store is None:
        return  # Exit if data files aren't found

    current_input = ""
    while True:
        # 2. Get user input
        # We show the current input and wait for more
        new_char = input(f"Enter text: {current_input}")

        # If the user just hits Enter, we process the current input
        if not new_char:
            if current_input:
                # 3. Call the search function
                completions = get_completions(current_input, sentence_store, inverted_index)

                # 4. Print the results
                print("\n--- Top 5 Completions ---")
                if completions:
                    for i, result in enumerate(completions, 1):
                        print(f"{i}. {result.completed_sentence} (Score: {result.score})")
                        print(f"   Source: {result.source_text}, Line: {result.offset}\n")
                else:
                    print("No completions found.")
                print("-------------------------\n")
            continue

        # 5. Handle the reset command
        if new_char == '#':
            print("Input reset.")
            current_input = ""
            continue

        # Append the new character(s) to the current input string
        current_input += new_char


if __name__ == '__main__':
    run()