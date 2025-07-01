
def write_append_read_file(filename="output.txt"):
    """
    Takes user input, writes it to a file, appends more data,
    and then reads and displays the final content.

    Args:
        filename (str): The name of the file to operate on.
    """

    # --- 1. Take user input and write it to the file ---
    try:
        initial_input = input("Enter text to write to the file: ")
        with open(filename, 'w') as file:  # 'w' mode opens for writing (creates if not exists, truncates if exists)
            file.write(initial_input + "\n")  # Add a newline for better readability
        print(f"Data successfully written to {filename}.")
    except IOError as e:
        print(f"Error writing to file: {e}")
        return # Exit if initial write fails

    # --- 2. Append additional data to the same file ---
    try:
        additional_input = input("Enter additional text to append: ")
        with open(filename, 'a') as file:  # 'a' mode opens for appending (creates if not exists)
            file.write(additional_input + "\n") # Add a newline
        print("Data successfully appended.")
    except IOError as e:
        print(f"Error appending to file: {e}")
        return # Exit if append fails

    # --- 3. Read and display the final content of the file ---
    try:
        print(f"\nFinal content of {filename}:")
        with open(filename, 'r') as file:  # 'r' mode opens for reading
            content = file.read()
            print(content.strip()) # Use strip to remove any extra newlines at the end
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found after operations.")
    except IOError as e:
        print(f"Error reading from file: {e}")

# Call the function to execute the task
write_append_read_file()