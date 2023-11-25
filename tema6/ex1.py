import os
import sys

def read_files(directory, file_extension):
    try:
        # verif path
        if not os.path.isdir(directory):
            raise FileNotFoundError("Invalid directory path")

        # verif extensie
        if not file_extension.startswith('.'):
            raise ValueError("File extension should start with a dot (.)")

        # cautare files
        for filename in os.listdir(directory):
            if filename.endswith(file_extension):
                file_path = os.path.join(directory, filename)

                try:
                    # citire si printare
                    with open(file_path, 'r') as file:
                        content = file.read()
                        print(f"File: {filename}\nContent:\n{content}\n{'-' * 40}")
                except Exception as e:
                    print(f"Error reading file {filename}: {e}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <directory_path> <file_extension>")
    else:
        directory_path = sys.argv[1]
        file_extension = sys.argv[2]

        read_files(directory_path, file_extension)
