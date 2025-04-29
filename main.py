from plugboard import Plugboard
from rotor import Rotor
from reflector import Reflector
from enigma_machine import EnigmaMachine

def run_enigma_simulation(enigma_machine):
    print("Welcome to your Enigma Machine!")
    while True:
        letter = input("Type a letter (A-Z) or EXIT to quit: ").upper()
        if letter == "EXIT":
            break
        if not letter.isalpha() or len(letter) != 1:
            print("Invalid input. Enter a single letter A-Z.")
            continue
        output = enigma_machine.encrypt(letter)
        print(f"Encrypted letter: {output}")
        print(f"Rotor positions: {enigma_machine.get_rotor_positions()}\n")

# Setup machine
rotor_I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", notch='Q', position='A')
rotor_II = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", notch='E', position='A')
rotor_III = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", notch='V', position='A')

reflector_B = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
plugboard = Plugboard([('A', 'B'), ('C', 'D')])

enigma = EnigmaMachine([rotor_III, rotor_II, rotor_I], reflector_B, plugboard)

run_enigma_simulation(enigma)
