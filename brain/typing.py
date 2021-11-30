from abc import ABC, abstractmethod
from typing import Optional, List, Iterable

from .model import Gene


class IActivator(ABC):
    @abstractmethod
    def __call__(self, value: float) -> float: ...


class IPerceptron(ABC):
    @abstractmethod
    def activate(self) -> None: ...
    @abstractmethod
    def signal(self, value: Optional[float] = 0) -> None: ...
    @abstractmethod
    def attach_to(self, perceptron: "IPerceptron", weight: float): ...


class INeuralNetwork(ABC):
    @abstractmethod
    def update(self): ...


class IGenomeParser(ABC):
    @abstractmethod
    def as_gene(self, gene: List[any]) -> Gene: ...
    @abstractmethod
    def get_intermediate_neuron_count(self, genome: List[int]) -> int: ...
    @abstractmethod
    def parse_genome(self, genome: List[int]) -> Iterable[Gene]: ...
