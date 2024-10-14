with open('trashcan/verbs.txt', 'r', encoding='utf-8') as input_file:
    input_data = input_file.read()

# Split the input list by 5 new lines
sections = input_data.strip().split("\n\n\n\n\n")

# Sort sections based on the number of "\n\n" splits within each section
sorted_sections = sorted(sections, key=lambda s: len(s.split("\n\n")))

# Join them back together with the required separators
sorted_output = "\n\n\n\n\n".join(sorted_sections)

# Save the result to a txt file
with open('trashcan/verbs_sorted.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(sorted_output)
