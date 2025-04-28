class Plugboard:
    def __init__(self, connections=None):
        self.wiring = {}
        if connections:
            for a, b in connections:
                self.wiring[a.upper()] = b.upper()
                self.wiring[b.upper()] = a.upper()

    def swap(self, c: str) -> str:
        return self.wiring.get(c.upper(), c.upper())
