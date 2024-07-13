Description
This Python script utilizes the Pygame library to translate text input into Morse code audio signals. It supports both English and Arabic characters through predefined mappings (morse_code_en and morse_code_ar). The Morse code translations trigger audio playback of predefined dot and dash sounds (morse1.wav and morse.wav). The program continuously prompts the user to input text and translates it into Morse code until the user types "EXIT".

Morse Code Translator
This Python script converts text input into Morse code and plays the corresponding audio signals using the Pygame library.

Requirements
Python 3.x
Pygame library (pip install pygame)
How to Use
Installation

Ensure Python 3.x is installed on your system.
Install the Pygame library using pip:
نسخ الكود
pip install pygame
Running the Script

Download the script and save it to your local machine.
Open a terminal or command prompt.
Navigate to the directory where the script is saved.
Run the script by typing:
نسخ الكود
python morse_code_translator.py
Using the Program

Enter text when prompted ("TYPE YOUR TEXT: ").
The program will convert each character to Morse code and play the corresponding audio signals.
Characters that are not recognized will be ignored.
To exit the program, type "EXIT" and press Enter.
Customization

You can customize the Morse code mappings (morse_code_en and morse_code_ar) or the audio files (dotSound and dashSound) as needed.
Notes
Ensure your system's audio is enabled and speakers/headphones are connected to hear the Morse code signals.
The script includes basic error handling for empty input and unrecognized characters.
The translation process is case-insensitive and treats all input as uppercase for consistency.
Acknowledgments
Pygame library for audio playback functionality.
The script was created for educational purposes and Morse code enthusiasts.
Author
Created by [Your Name]
GitHub: [Your GitHub URL]
Feel free to modify and use this script according to your needs. If you encounter any issues or have suggestions, please contact [Your Email Address].
