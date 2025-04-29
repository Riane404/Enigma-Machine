import tkinter as tk
from rotor import Rotor
from reflector import Reflector
from plugboard import Plugboard
from enigma_machine import EnigmaMachine

# --- Enigma components setup ---
rotor_wirings = [
    "EKMFLGDQVZNTOWYHXUSPAIBRCJ",  # Rotor I
    "AJDKSIRUXBLHWTMCQGZNPYFVOE",  # Rotor II
    "BDFHJLCPRTXVZNYEIWGAKMUSQO"   # Rotor III
]
notches = ['Q', 'E', 'V']  # Notch positions for rotors
reflector_wiring = "YRUHQSLDPXNGOKMIEBFZCWVJAT"  # Reflector B

# Initialize rotors, reflector, plugboard
rotors = [Rotor(rotor_wirings[i], notches[i]) for i in range(3)]
reflector = Reflector(reflector_wiring)
plugboard = Plugboard([('A', 'M'), ('F', 'I'), ('N', 'V'), ('P', 'S'), ('T', 'U')])  # Example plugboard

# Create Enigma machine
machine = EnigmaMachine(rotors, reflector, plugboard)

# --- GUI Setup ---
root = tk.Tk()
root.title("Enigma Machine Simulator")

# Input label and field
input_label = tk.Label(root, text="Enter a letter:", font=("Courier", 14))
input_label.grid(row=0, column=0, padx=10, pady=10)

entry = tk.Entry(root, width=2, font=("Courier", 24), justify='center')
entry.grid(row=0, column=1, padx=5)
entry.focus()

# Encrypt button
def encrypt_letter(event=None):
    letter = entry.get().upper()
    entry.delete(0, tk.END)
    if len(letter) == 1 and letter.isalpha():
        encrypted = machine.encrypt(letter)
        output_display.config(text=encrypted)
        rotor_positions = machine.get_rotor_positions()
        for i in range(3):
            rotor_labels[i].config(text=rotor_positions[i])
    else:
        output_display.config(text="Invalid")

encrypt_button = tk.Button(root, text="Encrypt", font=("Courier", 12), command=encrypt_letter)
encrypt_button.grid(row=0, column=2, padx=10)

entry.bind("<Return>", encrypt_letter)

# Output display
output_label = tk.Label(root, text="Encrypted Output:", font=("Courier", 14))
output_label.grid(row=1, column=0, padx=10)

output_display = tk.Label(root, text="", font=("Courier", 24), fg="green", width=2)
output_display.grid(row=1, column=1, padx=5)

# Rotor window labels
rotor_title = tk.Label(root, text="Rotor Positions:", font=("Courier", 14))
rotor_title.grid(row=2, column=0, pady=10)

rotor_labels = []
for i in range(3):
    lbl = tk.Label(root, text="A", font=("Courier", 32), width=2,
                   relief="ridge", bd=4, bg="lightgrey")
    lbl.grid(row=2, column=i+1, padx=5)
    rotor_labels.append(lbl)

# Start the GUI
root.mainloop()
