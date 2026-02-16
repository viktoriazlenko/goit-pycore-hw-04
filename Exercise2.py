# Exercise 2: Reading Cat Information from a File
# The function reads a file with cat information (id, name, age), creates a list of dictionaries where each dictionary contains the id, name, and age of a cat, and returns this list.
# The function also includes error handling for file not found, invalid data, and other exceptions.

path = "cats_info.txt" # The path to the file with cat information. The file should contain lines in the format: id,name,age (e.g., 1,Whiskers,3)
def get_cats_info(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = [el.strip() for el in file.readlines()] # Read the lines from the file and strip any leading/trailing whitespace
            cats_info = []
            for line in lines: # Process each line to extract cat information
                cat_id, name, age = line.split(',')
                cat_dict = {"id": cat_id, "name": name, "age": age}
                cats_info.append(cat_dict) # Append the cat information dictionary to the list of cats
        return cats_info
    except FileNotFoundError:
        print(f"File {path} not found.")
    except ValueError:
        print(f"File {path} contains invalid data.")
    except Exception as e:
        print(f"An error occurred: {e}")

print(get_cats_info(path))

