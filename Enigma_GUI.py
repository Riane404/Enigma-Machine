import tkinter as tk
from rotor import Rotor
from reflector import Reflector
from plugboard import Plugboard
from enigma_machine import EnigmaMachine

# Default rotor wirings and reflector
rotor_wirings = [
    "EKMFLGDQVZNTOWYHXUSPAIBRCJ",  # Rotor I
    "AJDKSIRUXBLHWTMCQGZNPYFVOE",  # Rotor II
    "BDFHJLCPRTXVZNYEIWGAKMUSQO"   # Rotor III
]
reflector_wiring = "YRUHQSLDPXNGOKMIEBFZCWVJAT"  # Reflector B
notches = ['Q', 'E', 'V']  # Notch positions for the rotors

# Initialize rotors, reflector, plugboard
rotors = [Rotor(rotor_wirings[i], notches[i]) for i in range(3)]
reflector = Reflector(reflector_wiring)
plugboard = Plugboard([('A', 'M'), ('F', 'I'), ('N', 'V'), ('P', 'S'), ('T', 'U')])  # Example plugboard config

# Create the Enigma machine instance
machine = EnigmaMachine(rotors, reflector, plugboard)

# Create GUI
root = tk.Tk()
root.title("Enigma Machine")

input_label = tk.Label(root, text="Enter a letter:")
input_label.grid(row=0, column=0, padx=10, pady=10)

entry = tk.Entry(root, width=2, font=("Courier", 24))
entry.grid(row=0, column=1)

output_label = tk.Label(root, text="Encrypted Output:")
output_label.grid(row=1, column=0, padx=10, pady=10)

output_display = tk.Label(root, text="", font=("Courier", 24), fg="green")
output_display.grid(row=1, column=1)

rotor_pos_label = tk.Label(root, text="Rotor Positions:")
rotor_pos_label.grid(row=2, column=0, padx=10)

rotor_display = tk.Label(root, text=machine.get_rotor_positions(), font=("Courier", 14))
rotor_display.grid(row=2, column=1)

def encrypt_letter(event=None):
    letter = entry.get().upper()
    entry.delete(0, tk.END)
    if len(letter) == 1 and letter.isalpha():
        encrypted = machine.encrypt(letter)
        output_display.config(text=encrypted)
        rotor_display.config(text=machine.get_rotor_positions())
    else:
        output_display.config(text="Invalid")

encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_letter)
encrypt_button.grid(row=0, column=2, padx=10)

entry.bind("<Return>", encrypt_letter)

root.mainloop()
