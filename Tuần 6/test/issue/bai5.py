import os

# Define a function 'file_exists' to check if a file exists in a specified directory.
def file_exists(directory, filename):
    # Create the full file path by joining the directory and filename.
    file_path = os.path.join(directory, filename)
    # Check if the file exists at the specified path.
    return os.path.exists(file_path)