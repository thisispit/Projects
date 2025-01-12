# Read the words from words_list.txt
with open('words.txt', 'r') as input_file:
    # Read all lines and strip whitespace
    words = [line.strip() for line in input_file.readlines()]

# Save the words as a list in a new text file
with open('words_list_output.txt', 'w') as output_file:
    # Write the Python list format to the file
    output_file.write(str(words))

print("List saved successfully to words_list_output.txt!")
with open('words.txt', 'w') as txt_file:
    txt_file.write("\n".join(words))

print("Files saved successfully!")
