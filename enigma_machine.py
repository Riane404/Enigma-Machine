from plugboard import Plugboard
from rotor import Rotor
from reflector import Reflector

class EnigmaMachine:
    def __init__(self, rotors, reflector, plugboard):
        self.rotors = rotors
        self.reflector = reflector
        self.plugboard = plugboard

    def step_rotors(self):
        rotate_next = self.rotors[0].rotate()
        if rotate_next:
            rotate_next = self.rotors[1].rotate()
            if rotate_next:
                self.rotors[2].rotate()

    def encrypt(self, c: str) -> str:
        if not c.isalpha() or len(c) != 1:
            return c
        c = c.upper()
        self.step_rotors()
        c = self.plugboard.swap(c)
        for rotor in self.rotors:
            c = rotor.encode_forward(c)
        c = self.reflector.reflect(c)
        for rotor in reversed(self.rotors):
            c = rotor.encode_backward(c)
        c = self.plugboard.swap(c)
        return c

    def get_rotor_positions(self):
        return ''.join(chr(rotor.position + ord('A')) for rotor in self.rotors)
