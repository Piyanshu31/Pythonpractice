# Using build in module make find file present
import os

# Function to print contents of a directory
def list_directory_contents(path='/'):
    try:
        contents = os.listdir(path)
        print(f"Contents of directory '{path}'.")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access '{path}'.")

# Provide the directory path here
directory_path = '/windows'  

# Call the function to list directory contents
list_directory_contents(directory_path)
