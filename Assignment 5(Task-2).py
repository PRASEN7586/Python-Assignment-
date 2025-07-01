
def demonstrate_list_slicing():
    """
    Demonstrates list slicing by creating a list, extracting the first five elements,
    reversing them, and printing both the extracted and reversed lists.
    """

    # 1. Creates a list of numbers from 1 to 10.
    original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Original list: {original_list}")

    # 2. Extracts the first five elements from the list.
    # List slicing syntax: list[start:end]
    # start is inclusive, end is exclusive.
    # If start is omitted, it defaults to 0.
    extracted_elements = original_list[0:5] # or simply original_list[:5]
    print(f"Extracted first five elements: {extracted_elements}")

    # 3. Reverses these extracted elements.
    # There are a few ways to reverse a list:
    # a) Using slicing with a step of -1: list[::-1] (creates a new reversed list)
    # b) Using the .reverse() method (reverses the list in-place)
    # We will use slicing for this example as it's common in competitive programming
    # and directly creates a new reversed list.
    reversed_extracted_elements = extracted_elements[::-1]
    # Alternatively, to reverse in-place: extracted_elements.reverse()

    # 4. Prints both the extracted list and the reversed list
    print(f"Reversed extracted elements: {reversed_extracted_elements}")

# Call the function to execute the demonstration
demonstrate_list_slicing()