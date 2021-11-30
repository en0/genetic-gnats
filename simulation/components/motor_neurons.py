import random

from .component_abc import SimComponentABC


class XAxisMotorNeuron(SimComponentABC):

    def update(self):
        x, y = self.parent.vector
        self.parent.vector = (x + self.output), y


class YAxisMotorNeuron(SimComponentABC):

    def update(self):
        x, y = self.parent.vector
        self.parent.vector = x, (y + self.output)


class RandomMotorNeuron(SimComponentABC):

    def update(self):
        x, y = self.parent.vector
        x = random.choice([
            0,
            x + self.output,
            x - self.output,
        ])
        y = random.choice([
            0,
            y + self.output,
            y - self.output,
        ])
        self.parent.vector = x, y
