#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3
# import sys
import os

def count_files_in_directories():
    current_directory = os.getcwd()
    directories = [d for d in os.listdir(current_directory) if os.path.isdir(d)]
    
    for directory in directories:
        total_file_count = 0
        for root, dirs, files in os.walk(directory):
            total_file_count += len(files)
        print(f"Directory '{directory}' contains {total_file_count} files.")

count_files_in_directories()
