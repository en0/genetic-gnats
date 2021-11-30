import random
from pygame import Surface, Rect, draw, Vector2
from typing import List, Tuple
from brain.enum import NeuronTypeEnum

from .interface import ISimObject, IComponent, ISimObjectCollection
from .brain_factory import BrainFactory
from .components import *


class SimObject(ISimObject):

    color: Tuple[int, int, int]

    @property
    def rect(self) -> Rect:
        rect = Rect((0, 0), self.size)
        rect.center = self.location
        return rect

    def think(self):
        self.vector = 0, 0
        self.brain.update()

    def update(self):

        for neuron in self.neurons:
            neuron.update()

        vec = Vector2(self.vector)
        if vec:
            x, y = Vector2(self.location) + (vec.normalize() * 2)

            # Non-self collide code
            #if self.boundary.collidepoint(x, y):
                #self.location = x, y

            # Self collide code
            n_rect = self.rect.copy()
            n_rect.center = x, y
            if self.boundary.collidepoint(x, y):
                if len(self.collection.collides_with(n_rect)) == 1:
                    self.location = x, y

    def draw(self, gfx: Surface):
        draw.circle(gfx, self.color, self.location, 5)

        vec = Vector2(self.vector)
        v = Vector2(self.location) + (vec.normalize() if vec else vec) * 10
        draw.line(gfx, (0, 255, 0), self.location, v)

    def __init__(self, boundary: Rect, location: Tuple[float, float], genome: List[int], color: Tuple[int, int, int] = None):
        self.color = color or (0, 0, 255)
        self.genome = genome.copy()
        self.size = 10, 10
        self.vector = 0, 0
        self.location = location
        self.boundary = boundary
        input_neurons = [
            XAxisSensorNeuron(self),
            YAxisSensorNeuron(self),
            NXAxisSensorNeuron(self),
            NYAxisSensorNeuron(self),
            RelativeXAxisSensorNeuron(self),
            RelativeYAxisSensorNeuron(self),
            RelativeDistanceFromCenterSensorNeuron(self),
            PopulationSensorNeuron(self),
        ]
        output_neurons = [
            XAxisMotorNeuron(self),
            YAxisMotorNeuron(self),
            RandomMotorNeuron(self),
        ]
        self.brain = BrainFactory(self, input_neurons, output_neurons).build(genome)
        self.neurons: List[IComponent] = input_neurons + output_neurons
