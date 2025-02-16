"""vaidhi - Exception Handling
Responsible for handling errors and network connectivity issues."""

import socket
from googletrans import Translator, LANGUAGES

translator = Translator()

# Function to check internet connectivity
def check_internet():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=2)  # Google's public DNS
        return True
    except OSError:
        return False

# Function to translate text
def Translate():
    if not check_internet():
        messagebox.showerror("Network Error", "No Internet Connection! Please check your connection.")
        return

    input_text = Input_text.get(1.0, END).strip()
    source_lang = src_lang.get().strip().lower()
    target_lang = dest_lang.get().strip().lower()

    if not input_text:
        messagebox.showwarning("Warning", "Please enter text to translate!")
        return

    if source_lang not in lang_map or target_lang not in lang_map:
        messagebox.showerror("Error", "Please check selection of Input/Output Language.")
        return

    try:
        translated = translator.translate(text=input_text, src=lang_map[source_lang], dest=lang_map[target_lang])
        Output_text.delete(1.0, END)
        Output_text.insert(END, translated.text)  
    except Exception as e:
        messagebox.showerror("Translation Error", f"Error: {str(e)}")

# Copy text to clipboard
def copy_text(text_widget):
    root.clipboard_clear()
    root.clipboard_append(text_widget.get(1.0, END))
    root.update()

# Paste text from clipboard
def paste_text(text_widget):
    text_widget.insert(INSERT, root.clipboard_get())