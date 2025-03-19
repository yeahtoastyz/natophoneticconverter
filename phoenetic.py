import tkinter as tk
from tkinter import ttk
import tkinter.font as tkfont

# Dictionary of NATO phonetic alphabet
nato_phonetic = {
    'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo',
    'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliet',
    'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November', 'O': 'Oscar',
    'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
    'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray', 'Y': 'Yankee',
    'Z': 'Zulu'
}

# Dictionary for numbers
number_phonetic = {
    '0': 'Zero', '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four',
    '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine'
}

# Dictionary for common symbols
symbol_phonetic = {
    '.': 'Point', ',': 'Comma', '!': 'Exclamation Mark', '?': 'Question Mark',
    '@': 'At Symbol', '#': 'Hash', '$': 'Dollar', '%': 'Percent',
    '&': 'Ampersand', '*': 'Asterisk', '+': 'Plus', '-': 'Minus',
    '=': 'Equals', '/': 'Forward Slash', '\\': 'Back Slash', '|': 'Vertical Bar',
    '(': 'Open Parenthesis', ')': 'Close Parenthesis', '[': 'Open Bracket',
    ']': 'Close Bracket', '{': 'Open Brace', '}': 'Close Brace',
    '<': 'Less Than', '>': 'Greater Than', ':': 'Colon', ';': 'Semicolon',
    '"': 'Double Quote', "'": 'Single Quote', '`': 'Backtick', '~': 'Tilde',
    ' ': 'Space'
}

# Color scheme
COLORS = {
    'bg': '#1e1e1e',
    'fg': '#00ff00',
    'entry_bg': '#2d2d2d',
    'entry_fg': '#00ff00',
    'button_bg': '#2d2d2d',
    'button_fg': '#00ff00',
    'button_active_bg': '#3d3d3d'
}

def convert_to_phonetic(*args):
    text = input_entry.get().upper()
    result = []
    for char in text:
        if char.isalpha():
            result.append(nato_phonetic.get(char, char))
        elif char.isdigit():
            result.append(number_phonetic.get(char, char))
        else:
            result.append(symbol_phonetic.get(char, char))
    output_label.config(text=' '.join(result))

# Create main window
root = tk.Tk()
root.title("NATO Phonetic Converter")
root.geometry("500x300")
root.configure(bg=COLORS['bg'])

# Configure style
style = ttk.Style()
style.configure('Custom.TFrame', background=COLORS['bg'])
style.configure('Custom.TLabel', 
                background=COLORS['bg'],
                foreground=COLORS['fg'],
                font=('Consolas', 12))
style.configure('Custom.TButton',
                background=COLORS['button_bg'],
                foreground=COLORS['button_fg'])

# Create and pack widgets
frame = ttk.Frame(root, padding="20", style='Custom.TFrame')
frame.pack(fill=tk.BOTH, expand=True)

# Title
title_label = ttk.Label(frame, 
                       text="NATO Phonetic Converter",
                       style='Custom.TLabel',
                       font=('Consolas', 16, 'bold'))
title_label.pack(pady=(0, 20))

# Input section
input_frame = ttk.Frame(frame, style='Custom.TFrame')
input_frame.pack(fill=tk.X, pady=10)

ttk.Label(input_frame, 
          text="Enter text:",
          style='Custom.TLabel').pack(side=tk.LEFT)

input_entry = tk.Entry(input_frame,
                      bg=COLORS['entry_bg'],
                      fg=COLORS['entry_fg'],
                      insertbackground=COLORS['fg'],
                      font=('Consolas', 12),
                      relief=tk.FLAT)
input_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(10, 0))

# Output section
output_frame = ttk.Frame(frame, style='Custom.TFrame')
output_frame.pack(fill=tk.BOTH, expand=True, pady=10)

ttk.Label(output_frame,
          text="Phonetic:",
          style='Custom.TLabel').pack(anchor=tk.W)

output_label = ttk.Label(output_frame,
                        text="",
                        style='Custom.TLabel',
                        wraplength=450)
output_label.pack(fill=tk.BOTH, expand=True, pady=(5, 0))

# Bind the input entry to update in real-time
input_entry.bind('<KeyRelease>', convert_to_phonetic)

# Start the application
root.mainloop()
