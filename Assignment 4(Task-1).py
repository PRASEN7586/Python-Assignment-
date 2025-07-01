
def read_and_handle_file(filename="sample.txt"):
    """
    Opens and reads a text file line by line, handling FileNotFoundError.

    Args:
        filename (str): The name of the file to read.
    """
    try:
        with open(filename, 'r') as file:
            print("Reading file content:")
            for i, line in enumerate(file, 1):
                print(f"Line {i}: {line.strip()}")  # .strip() removes trailing newline characters
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# --- Test cases ---

# Test case 1: File exists (you would need to create a sample.txt file for this to work)
# Create a 'sample.txt' file in the same directory as your Python script with the following content:
# This is a sample text file.
# It contains multiple lines.
print("--- Testing when 'sample.txt' exists ---")
read_and_handle_file("sample.txt")
print("\n" + "="*40 + "\n")

# Test case 2: File does not exist
print("--- Testing when 'non_existent_file.txt' does not exist ---")
read_and_handle_file("non_existent_file.txt")