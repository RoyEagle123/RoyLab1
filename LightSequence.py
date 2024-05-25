import random
import time  # Import the time module

class LightSequence:
    def __init__(self, num_leds, colors):
        self.num_leds = num_leds
        self.colors = colors
        self.sequence = []

    def reset(self):
        self.sequence = []

    def generate_initial_sequence(self):
        random.seed(time.time())  # Seed the random number generator
        initial_length = random.randint(1, 4)
        self.sequence = [(i, random.choice(self.colors)) for i in range(initial_length)]
        print(f"Initial sequence generated: {self.sequence}")

    def generateNext(self):
        if len(self.sequence) < self.num_leds:
            next_led = len(self.sequence)
            next_color = random.choice(self.colors)
            self.sequence.append((next_led, next_color))
            print(f"Next sequence: {self.sequence}")

    def checkInput(self, color):
        if self.sequence and self.sequence[-1][1] == color:
            self.sequence.pop()
            return True
        return False
