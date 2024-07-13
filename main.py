import pygame
import time

# Morse code mappings for English characters and numbers
morse_code_en = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.'
}

# Morse code mappings for Arabic characters
morse_code_ar = {
    'ا': '.-', 'ب': '-...', 'ت': '-', 'ث': '-.-.', 'ج': '--.', 'ح': '....',
    'خ': '---.', 'د': '-..', 'ذ': '....-', 'ر': '.-.', 'ز': '--..',
    'س': '...', 'ش': '----', 'ص': '-.-.', 'ض': '-..-', 'ط': '..-',
    'ظ': '-.--', 'ع': '..-.', 'غ': '--.-', 'ف': '..-..', 'ق': '--.--',
    'ك': '-.-', 'ل': '.-..', 'م': '--', 'ن': '-.', 'ه': '-..-',
    'و': '.--', 'ي': '-.--'
}

def translate_to_morse(text):
    text = text.upper()
    morse_code = {}
    chShow = []
    
    for char in text:
        chShow.append(char)
        if char in morse_code_en:
            morse_code[char] = morse_code_en[char]
        elif char in morse_code_ar:
            morse_code[char] = morse_code_ar[char]
        elif char == ' ':
            morse_code.append(' \n ')  # Separator for words
    return morse_code

pygame.mixer.init()

dotSound = "sounds/morse1.wav"
dashSound = "sounds/morse.wav"

def playSound(morseCode):
    for symbol in morseCode:
        if symbol == '.':
            pygame.mixer.music.load(dotSound)
            pygame.mixer.music.play()
            time.sleep(0.2)
        elif symbol == '-':
            pygame.mixer.music.load(dashSound)
            pygame.mixer.music.play()
            time.sleep(0.6)
        elif symbol == ' ':
            time.sleep(0.2)
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

while True:
    text = input("TYPE YOUR TEXT: ")
    if text.upper() == "EXIT":
        print("EXIT!")
        break
    else:
        if len(text) > 0:
            result = translate_to_morse(text)
            for cheracter, morseCode in result.items():
                playSound(morseCode)
                print(f"{cheracter} => {morseCode}")
        else:
            print("SORRY YOUR TEXT CAN'T BE EMPTY!")

print(translate_to_morse("boraqff"))