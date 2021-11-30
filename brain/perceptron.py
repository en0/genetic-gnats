from typing import List, Tuple, Optional

from .typing import IPerceptron, IActivator


class Perceptron(IPerceptron):

    _input: List[float]
    _attached: List[Tuple[IPerceptron, float]]
    _activator: IActivator
    _output: float

    @property
    def output(self) -> float:
        return self._output

    def activate(self) -> None:
        self._output = self._activator(sum(self._input))
        self._input = []
        for n, w in self._attached:
            n.signal(self._output * w)

    def signal(self, value: Optional[float] = 0) -> None:
        self._input.append(value)

    def attach_to(self, perceptron: IPerceptron, weight: float):
        self._attached.append((perceptron, weight))

    def __init__(self, activator: IActivator):
        self._input: List[float] = []
        self._attached: List[Tuple[IPerceptron, float]] = []
        self._activator = activator
