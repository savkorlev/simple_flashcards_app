import tkinter as tk

# Function to read the file and create flashcards
def load_flashcards(file_path):
    flashcards = []
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

        # Split the content based on five newlines for words and three newlines for translations
        entries = content.split('\n\n\n\n\n')
        for entry in entries:
            parts = entry.split('\n\n\n')
            if len(parts) == 2:
                word = parts[0].strip()
                translation = parts[1].strip()
                flashcards.append((word, translation))
    return flashcards

# Function to display the next flashcard
def next_flashcard():
    global current_flashcard_index, current_language_mode
    current_flashcard_index = (current_flashcard_index + 1) % len(flashcards)
    current_language_mode = default_language_mode  # Set the display to default language mode
    display_flashcard()

# Function to display the previous flashcard
def prev_flashcard():
    global current_flashcard_index, current_language_mode
    current_flashcard_index = (current_flashcard_index - 1) % len(flashcards)
    current_language_mode = default_language_mode  # Set the display to default language mode
    display_flashcard()

# Function to reveal the translation
def reveal_translation():
    global current_flashcard, current_language_mode
    if current_flashcard:
        if current_language_mode == "German-English":
            translation_label.config(text=current_flashcard[1])
        else:
            translation_label.config(text=current_flashcard[0])

# Function to toggle the language mode
def toggle_language():
    global current_language_mode
    if current_language_mode == "German-English":
        current_language_mode = "English-German"
    else:
        current_language_mode = "German-English"
    display_flashcard()

# Function to display the current flashcard based on the language mode
def display_flashcard():
    global current_flashcard, current_language_mode
    current_flashcard = flashcards[current_flashcard_index]
    
    if current_language_mode == "German-English":
        word_label.config(text=current_flashcard[0])
    else:
        word_label.config(text=current_flashcard[1])
    translation_label.config(text="")  # Clear the translation
    word_number_label.config(text=f"Word {current_flashcard_index + 1} of {len(flashcards)}")

# Function to handle key presses for navigation and toggling language
def handle_keypress(event):
    if event.keysym == 'Right':
        next_flashcard()
    elif event.keysym == 'Left':
        prev_flashcard()
    elif event.keysym == 'Up' or event.keysym == 'Down':
        toggle_language()

# Function to go to the specified word index from the input field
def go_to_word():
    global current_flashcard_index, current_language_mode
    try:
        index = int(index_input.get()) - 1  # Convert to 0-based index
        if 0 <= index < len(flashcards):
            current_flashcard_index = index
            current_language_mode = default_language_mode  # Set the display to default language mode
            display_flashcard()
            index_input.delete(0, 'end')  # Clear input after successful go
            root.focus()  # Move focus away from input field to avoid blinking
        else:
            error_label.config(text="Index out of range")
    except ValueError:
        error_label.config(text="Please enter a valid number")

# Function to toggle full screen mode
def toggle_fullscreen(event=None):
    global fullscreen
    fullscreen = not fullscreen
    root.attributes("-fullscreen", fullscreen)

# Function to exit full screen mode
def exit_fullscreen(event=None):
    global fullscreen
    fullscreen = False
    root.attributes("-fullscreen", False)

# Load flashcards from the provided text file
file_path = 'Goethe-Zertifikat_B1_Wortliste_gemischt.txt'
flashcards = load_flashcards(file_path)

# Initialize the GUI application
root = tk.Tk()
root.title("Flashcard App")

# Start without full screen mode
fullscreen = False

# Set dark mode colors
bg_color = "#2E2E2E"      # Dark background
fg_color = "#F5F5F5"      # Light text color
input_bg_color = "#505050"  # Darker background for input fields
button_bg_color = "#404040"  # Darker background for buttons
button_fg_color = "#F5F5F5"  # Light text color for buttons

# Set window background color
root.configure(bg=bg_color)

# Top frame for word number display
top_frame = tk.Frame(root, bg=bg_color)
top_frame.pack(side=tk.TOP, fill=tk.X)

# Center frame for word and translation
center_frame = tk.Frame(root, bg=bg_color)
center_frame.pack(expand=True)

# Bottom frame for "Go to word number" part
bottom_frame = tk.Frame(root, bg=bg_color)
bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)

# Word number display at the top
word_number_label = tk.Label(top_frame, text="", font=("Helvetica", 18), bg=bg_color, fg=fg_color)
word_number_label.pack(pady=10)

# Displaying Word in the center
word_label = tk.Label(top_frame, text="", font=("Helvetica", 36), wraplength=root.winfo_screenwidth(), bg=bg_color, fg=fg_color)
word_label.pack(pady=10)

# Displaying Translation (hidden at first) in the center
translation_label = tk.Label(center_frame, text="", font=("Helvetica", 28), fg=fg_color, wraplength=root.winfo_screenwidth(), bg=bg_color)
translation_label.pack(pady=20)

# Input field to go to a specific word index at the bottom
index_input_label = tk.Label(bottom_frame, text="Go to word number:", font=("Helvetica", 14), bg=bg_color, fg=fg_color)
index_input_label.pack(pady=5)
index_input = tk.Entry(bottom_frame, font=("Helvetica", 14), width=10, bg=input_bg_color, fg=fg_color)
index_input.pack(pady=5)

# Button to go to the entered word index
go_button = tk.Button(bottom_frame, text="Go", command=go_to_word, font=("Helvetica", 14), bg=button_bg_color, fg=button_fg_color)
go_button.pack(pady=5)

# Dropdown to select default language mode
def change_language_mode(selected_mode):
    global default_language_mode
    default_language_mode = selected_mode
    display_flashcard()

language_mode_var = tk.StringVar(root)
language_mode_var.set("German-English")  # Default value

language_dropdown = tk.OptionMenu(bottom_frame, language_mode_var, "German-English", "English-German", command=change_language_mode)
language_dropdown.config(font=("Helvetica", 14), bg=button_bg_color, fg=button_fg_color)
language_dropdown.pack(pady=10)


# Error message label
error_label = tk.Label(bottom_frame, text="", font=("Helvetica", 12), fg="red", bg=bg_color)
error_label.pack(pady=5)

# Initialize variables
current_flashcard_index = 0
current_flashcard = None
default_language_mode = "German-English"  # Set a constant to show the default language first
current_language_mode = default_language_mode  # Start with default language mode

# Load the first flashcard
display_flashcard()

# Bind arrow keys for navigation and toggling language mode
root.bind('<Right>', handle_keypress)
root.bind('<Left>', handle_keypress)
root.bind('<Up>', handle_keypress)
root.bind('<Down>', handle_keypress)

# Fullscreen controls
root.bind('<F11>', toggle_fullscreen)  # Press F11 to toggle fullscreen
root.bind('<Escape>', exit_fullscreen)  # Press Escape to exit fullscreen

# Run the application
root.mainloop()
