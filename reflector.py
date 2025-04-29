class Reflector:
    def __init__(self, wiring: str):
        self.wiring = wiring

    def reflect(self, c: str) -> str:
        index = ord(c.upper()) - ord('A')
        return self.wiring[index]
