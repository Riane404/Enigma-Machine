class Rotor:
    def __init__(self, wiring: str, notch: str, position='A'):
        self.wiring = wiring
        self.notch = ord(notch.upper()) - ord('A')
        self.position = ord(position.upper()) - ord('A')

    def encode_forward(self, c: str) -> str:
        index = (ord(c.upper()) - ord('A') + self.position) % 26
        encoded_c = self.wiring[index]
        return chr((ord(encoded_c) - ord('A') - self.position + 26) % 26 + ord('A'))

    def encode_backward(self, c: str) -> str:
        index = (ord(c.upper()) - ord('A') + self.position) % 26
        letter = chr((index + ord('A')) % 256)
        pos_in_wiring = self.wiring.index(letter)
        return chr((pos_in_wiring - self.position + 26) % 26 + ord('A'))

    def rotate(self) -> bool:
        self.position = (self.position + 1) % 26
        return self.position == self.notch
    
    def get_current_wiring(self):
        return self.wiring[self.position:] + self.wiring[:self.position]

