from abc import abstractmethod
from brain import Perceptron, LogisticActivator

from ..interface import IComponent, ISimObjectCollection, ISimObject


class SimComponentABC(Perceptron, IComponent):

    @property
    def parent(self) -> ISimObject:
        return self._parent

    @abstractmethod
    def update(self):
        ...

    def __init__(self, sim_object: ISimObject):
        super().__init__(LogisticActivator())
        self._parent = sim_object
