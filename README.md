# NATO Phonetic Converter

A modern, dark-themed application that converts text to NATO phonetic alphabet in real-time.

## Features
- Real-time conversion as you type
- Modern dark theme with green accents
- Clean and intuitive interface
- No installation required (portable executable)

## Usage
1. Run the executable (NATO_Phonetic_Converter.exe)
2. Type any text in the input field
3. See the NATO phonetic conversion appear instantly below

## Building from Source
1. Install the requirements:
   ```
   pip install -r requirements.txt
   ```
2. Build the executable:
   ```
   pyinstaller --onefile --windowed --name NATO_Phonetic_Converter phoenetic.py
   ```
3. The executable will be created in the `dist` folder

## Requirements
- Python 3.6 or higher
- PyInstaller (for building the executable) 
