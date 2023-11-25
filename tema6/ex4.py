import os
import sys

def count_files_by_extension(directory):
    extension_counts = {}

    try:
        if not os.path.isdir(directory):
            raise FileNotFoundError("Invalid directory path")

        for root, _, files in os.walk(directory):
            for file in files:
                _, file_extension = os.path.splitext(file)
                file_extension = file_extension.lower() 
                extension_counts[file_extension] = extension_counts.get(file_extension, 0) + 1

        if extension_counts:
            print("File counts by extension:")
            for extension, count in extension_counts.items():
                print(f"{extension}: {count} file(s)")
        else:
            print("No files found in the directory.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
    else:
        directory_path = sys.argv[1]
        count_files_by_extension(directory_path)
