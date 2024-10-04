import random

# Load the contents of the file
file_path = 'Goethe-Zertifikat_B1_Wortliste_Teil_2.txt'

# Read the file content
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# Split the content by five newlines to identify the flashcards
flashcards = content.split('\n\n\n\n\n')

# Shuffle the flashcards
random.shuffle(flashcards)

# Join the shuffled flashcards back into a single string
shuffled_content = '\n\n\n\n\n'.join(flashcards)

# Save the shuffled content into a new file
shuffled_file_path = 'Goethe-Zertifikat_B1_Wortliste_Teil_2_gemischt.txt'
with open(shuffled_file_path, 'w', encoding='utf-8') as file:
    file.write(shuffled_content)
