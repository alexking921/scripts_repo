#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3
import os

def get_last_20_commands():
    # Execute the history command and capture its output
    history_output = os.popen('history').read()
    
    # Split the output into lines
    history_lines = history_output.splitlines()
    
    # Get the last 20 commands
    last_20_commands = history_lines[-20:]
    
    # Print the last 20 commands
    for command in last_20_commands:
        print(command)

if __name__ == "__main__":
    get_last_20_commands()