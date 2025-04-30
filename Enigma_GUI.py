import tkinter as tk
from rotor import Rotor
from reflector import Reflector
from plugboard import Plugboard
from enigma_machine import EnigmaMachine

show_wirings = False  # Global toggle state

# --- Enigma components setup ---
rotor_wirings = [
    "EKMFLGDQVZNTOWYHXUSPAIBRCJ",  # Rotor I
    "AJDKSIRUXBLHWTMCQGZNPYFVOE",  # Rotor II
    "BDFHJLCPRTXVZNYEIWGAKMUSQO"   # Rotor III
]
notches = ['Q', 'E', 'V']  # Notch positions for rotors
reflector_wiring = "YRUHQSLDPXNGOKMIEBFZCWVJAT"  # Reflector B

# Plugboard connections (default, non-editable)
plugboard_pairs = [('A', 'M'), ('F', 'I'), ('N', 'V'), ('P', 'S'), ('T', 'U')]
plugboard = Plugboard(plugboard_pairs)

# Initialize rotors, reflector
rotors = [Rotor(rotor_wirings[i], notches[i]) for i in range(3)]
reflector = Reflector(reflector_wiring)

# Store initial positions
initial_positions = ['A', 'A', 'A']

# Rotor display update inside reset_rotors
def reset_rotors():
    for rotor, pos in zip(rotors, initial_positions):
        rotor.position = ord(pos.upper()) - ord('A')
    rotor_positions = machine.get_rotor_positions()  # Get updated rotor positions
    update_rotor_display(rotor_positions)  # Update rotor display
    output_display.config(text="")  # Clear output

# Create Enigma machine
machine = EnigmaMachine(rotors, reflector, plugboard)

# Function to update rotor display based on toggle state
def update_rotor_display(rotor_positions):
    for i in range(3):
        if show_wirings:
            # Show wiring at the current rotor position
            current_letter = rotor_wirings[i][rotors[i].position]
            rotor_labels[i].config(text=current_letter)  # Show letter at position
        else:
            # Show the current position (i.e., letter at the current rotor position)
            rotor_labels[i].config(text=rotor_positions[i])  # Show position

# Function to update the display label dynamically
def update_display_label():
    if show_wirings:
        rotor_title_display.config(text="Displaying: Wiring")
    else:
        rotor_title_display.config(text="Displaying: Position")

# Encrypt function
def encrypt_letter(event=None):
    letter = entry.get().upper()
    entry.delete(0, tk.END)
    if len(letter) == 1 and letter.isalpha():
        encrypted = machine.encrypt(letter)
        output_display.config(text=encrypted)
        rotor_positions = machine.get_rotor_positions()
        update_rotor_display(rotor_positions)
    else:
        output_display.config(text="Invalid")

# Toggle function to switch between position and wiring
def toggle_rotor_display():
    global show_wirings
    show_wirings = not show_wirings
    rotor_positions = machine.get_rotor_positions()  # Get updated rotor positions
    update_rotor_display(rotor_positions)
    update_display_label()  # Update the display label text

# --- GUI Setup ---
root = tk.Tk()
root.title("Enigma Machine Simulator")

# Input field
input_label = tk.Label(root, text="Enter a letter:", font=("Courier", 14))
input_label.grid(row=0, column=0, padx=10, pady=10)

entry = tk.Entry(root, width=2, font=("Courier", 24), justify='center')
entry.grid(row=0, column=1, padx=5)
entry.focus()

# Encrypt button
encrypt_button = tk.Button(root, text="Encrypt", font=("Courier", 12), command=encrypt_letter)
encrypt_button.grid(row=0, column=2, padx=10)

entry.bind("<Return>", encrypt_letter)

# Output display
output_label = tk.Label(root, text="Encrypted Output:", font=("Courier", 14))
output_label.grid(row=1, column=0, padx=10)

output_display = tk.Label(root, text="", font=("Courier", 24), fg="green", width=2)
output_display.grid(row=1, column=1, padx=5)

# Rotor display title
rotor_title = tk.Label(root, text="Rotor Display:", font=("Courier", 14))
rotor_title.grid(row=2, column=0, pady=10)

# Rotor displaying
rotor_title_display = tk.Label(root, text="Displaying:", font=("Courier", 10))
rotor_title_display.grid(row=5, column=2, pady=20)

# Rotor position labels
rotor_labels = []
for i in range(3):
    lbl = tk.Label(root, text="A", font=("Courier", 32), width=2,
                   relief="ridge", bd=4, bg="lightgrey")
    lbl.grid(row=2, column=i+1, padx=5)
    rotor_labels.append(lbl)

# Plugboard display (static, non-editable)
plugboard_title = tk.Label(root, text="Plugboard Connections:", font=("Courier", 14, "bold"))
plugboard_title.grid(row=3, column=0, columnspan=3, pady=(20, 5))

plugboard_display = tk.Label(root, text=", ".join([f"{a} ⇄ {b}" for a, b in plugboard_pairs]), font=("Courier", 12), fg="blue")
plugboard_display.grid(row=4, column=0, columnspan=3)

# Reset button to reset rotors
reset_button = tk.Button(root, text="Reset Rotors", command=reset_rotors)
reset_button.grid(row=0, column=3, pady=10)

# Toggle button to switch between rotor position and wiring
toggle_button = tk.Button(root, text="Toggle Rotor Display", font=("Courier", 12), command=toggle_rotor_display)
toggle_button.grid(row=5, column=0, columnspan=2, pady=10)

# Initialize display label immediately
update_display_label()

# Start GUI
root.mainloop()
