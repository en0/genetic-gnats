import random

from pygame import Rect
from typing import List, Union, Tuple

from brain.enum import NeuronTypeEnum
from .sim_object import SimObject
from .interface import ISimObject


class SimulatorObjectFactory:

    def random_location(self) -> Tuple[int, int]:
        x = random.randint(self._boundary.left, self._boundary.right)
        y = random.randint(self._boundary.top, self._boundary.bottom)
        return x, y

    def reproduce(self, a: ISimObject, b: ISimObject):
        x = random.randint(1, len(a.genome) - 2)
        ng, color = self.mutate(a.genome[:x] + b.genome[x:])
        return SimObject(self._boundary, self.random_location(), ng, color)

    def mutate(self, genome: List[int]):
        if random.randint(0, self._mutation_factor) != 0:
            return genome, None
        index = random.randint(0, len(genome) - 1)
        if isinstance(genome[index], float):
            genome[index] = random.uniform(genome[index]-2, genome[index]+2)
        elif isinstance(genome[index], int):
            genome[index] = random.randint(genome[index]-2, genome[index]+2)
        elif isinstance(genome[index], NeuronTypeEnum):
            genome[index] = random.choice([
                NeuronTypeEnum.INPUT_NEURON,
                NeuronTypeEnum.INTERMEDIATE_NEURON,
            ])
        return genome, (255, 0, 0)

    def random_genome(self) -> List[Union[int, float]]:
        genome = [self._intermediate_neurons]
        for i in range(self._connections):
            genome.extend([
                random.choice([0, 1]),
                random.randint(0, 1000),
                random.choice([0, 1]),
                random.randint(0, 1000),
                random.uniform(-2.0, 2.0)
            ])
        return genome

    def new(self):
        return SimObject(self._boundary, self.random_location(), self.random_genome())

    def __init__(self, boundary: Rect, **kwargs):

        kwargs.setdefault("seed", 100)
        kwargs.setdefault("neuron_connections", 50)
        kwargs.setdefault("intermediate_neurons", 50)
        kwargs.setdefault("mutation_factor", 10)

        random.seed(kwargs["seed"])
        self._connections = kwargs["neuron_connections"]
        self._intermediate_neurons = kwargs["intermediate_neurons"]
        self._mutation_factor = kwargs["mutation_factor"]
        self._boundary = boundary
