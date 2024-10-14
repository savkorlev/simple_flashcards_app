# Read the file
with open('Goethe-Zertifikat_B1_Wortliste_gemischt.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# Split the content into individual elements
elements = content.split('\n\n\n\n')

# Initialize a list to store verbs
verbs = []

# Iterate through the elements to find the ones with verbs
for element in elements:
    german_part, english_part = element.split('\n\n\n')
    german_word, german_usage = german_part.split('\n\n')
    english_word, english_usage = english_part.split('\n\n')
    if english_word.startswith('to '):  # Check if it's a verb
        verbs.append(f'{german_word}\n{english_word}')

# Join the verbs with two new lines between them
verbs_text = '\n\n'.join(verbs)

# Save the result to a txt file
with open('misc/verbs/B1_German_Verbs.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(verbs_text)
