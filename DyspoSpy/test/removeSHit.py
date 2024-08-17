# Open the file in read mode
with open('DyspoSpy/data/links.txt', 'r') as linkFile:
    # Read all lines from the file
    lines = linkFile.readlines()

# Initialize a variable to store modified lines
modified_lines = []

# Process each line
for line in lines:
    # Find the indices of the first and second quotation marks
    first_quote_index = line.find('"')
    second_quote_index = line.find('"', first_quote_index + 1)

    # If both quotes are found
    if first_quote_index != -1 and second_quote_index != -1:
        # Construct the modified line by keeping the content before the first quote
        # and after the second quote
        modified_line = line[:first_quote_index + 1] + line[second_quote_index:]
        modified_lines.append(modified_line)
    else:
        # If quotes are not found, keep the original line
        modified_lines.append(line)

# Open the file in write mode to save the modified lines
with open('DyspoSpy/data/links.txt', 'w') as linkFile:
    linkFile.writelines(modified_lines)
