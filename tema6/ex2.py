import os

def rename_files(directory):
    try:
        if not os.path.isdir(directory):
            raise FileNotFoundError("Invalid directory path")

        # lista fisiere din dir
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

        for index, filename in enumerate(files, start=1):
            old_path = os.path.join(directory, filename)
            new_filename = f"file{index}{os.path.splitext(filename)[1]}"
            new_path = os.path.join(directory, new_filename)

            try:
                # rename
                os.rename(old_path, new_path)
                print(f"Renamed: {filename} -> {new_filename}")
            except Exception as e:
                print(f"Error renaming file {filename}: {e}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    directory_path = "/path/to/directory"
    rename_files(directory_path)
