import os
import sys

def calculate_total_size(directory):
    total_size = 0

    try:
        if not os.path.isdir(directory):
            raise FileNotFoundError("Invalid directory path")

        # iterare prin files din dir
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                total_size += os.path.getsize(file_path)

        print(f"Total size of all files in {directory}: {total_size} bytes")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
    else:
        directory_path = sys.argv[1]
        calculate_total_size(directory_path)
