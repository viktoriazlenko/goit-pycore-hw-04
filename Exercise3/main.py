# Exercise 3: Directory Structure Printer
# Write a Python script that takes a directory path as input and prints the structure of the directory in a tree-like format. 
# The script should handle cases where the provided path does not exist or is not a directory, and it should display appropriate error messages in red color. 
# The directory names should be printed in blue color, while file names should be printed in green color.

import sys

from pathlib import Path
from colorama import init, Fore, Style

def print_directory_structure(path: Path, indent: int = 0):
    if not path.exists():
        print(f"{Fore.RED}Error: The path '{path}' does not exist.{Fore.RESET}") # Message in red color if the path does not exist
        return
    if not path.is_dir():
        print(f"{Fore.RED}Error: The path '{path}' is not a directory.{Fore.RESET}") # Message in red color if the path is not a directory
        return

    for item in path.iterdir(): # Iterate through the items in the directory
        if item.is_dir():
            print(f"{' ' * indent}{Fore.BLUE}{item.name}/ {Style.RESET_ALL}")  # Print the directory name in blue color
            print_directory_structure(item, indent + 4)
        else:
            print(f"{' ' * indent}{Fore.GREEN}{item.name} {Fore.RESET}") # Print the file name in green color

if __name__ == "__main__": # Main block to execute the script from console
    # init(autoreset=True)  # Initialize colorama
    if len(sys.argv) != 2: # Check if the user provided the correct number of arguments
        print(f"{Fore.RED}Usage: python hw03.py <directory_path>{Fore.RESET}") 
        sys.exit(1)

    directory_path = Path(sys.argv[1]) # Get the directory path from the command line argument
    print_directory_structure(directory_path)

