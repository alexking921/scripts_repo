#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3
import sys
import os

def count_files():
    directory = os.getcwd()
    file_count = 0

    for _, _, files in os.walk(directory):
        file_count += len(files)

    return file_count

print(count_files())
