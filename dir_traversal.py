import os


def find_text_files(root_directory: str):
    """
    Scans a directory tree and returns a list of paths to all .txt files.

    Args:
        root_directory (str): The path to the starting directory.

    Returns:
        list: A list of full file paths.
    """
    text_file_paths = []
    for dirpath, _, filenames in os.walk(root_directory):
        for filename in filenames:
            if filename.endswith(".txt"):
                full_path = os.path.join(dirpath, filename)
                text_file_paths.append(full_path)
    return text_file_paths


def main():
    path_lst=find_text_files("students_materials/Archive")
    for path in path_lst:
        print(path)

main()


