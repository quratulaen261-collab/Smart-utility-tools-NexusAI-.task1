from file_manager import rename_files, organize_files
from file_reader import read_file
from utils import log
import os

folder = "test_files"
file_path = os.path.join(folder, "file.txt")

# Make sure the file exists before doing anything
if os.path.exists(file_path):
    rename_files(folder, "file")
    organize_files(folder)
    content = read_file("E:\\smart utility tools\\test_files")
    log("Files organized successfully.")
    print("File Content:\n", content)
    print("Done")
else:
    print("Error: file.txt not found in test_files folder.")


