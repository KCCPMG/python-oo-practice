"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        """Initialize the SerialGenerator instance with start and number properties, both set to the start argument"""
        self.start = start
        self.number = start

    def __repr__(self):
        return f"<SerialGenerator start={self.start} next={self.number}>"
    
    def generate(self):
        """Return instance's number property, increment number property"""
        self.number += 1
        return self.number - 1

    def reset(self):
        """Reset number property to start property"""
        self.number = self.start