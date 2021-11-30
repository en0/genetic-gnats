import math
from .typing import IActivator


class LogisticActivator(IActivator):
    def __call__(self, value: float) -> float:
        return (1.0 / (1 + math.e ** -value)) - 0.5


class PassActivator(IActivator):
    def __call__(self, value: float) -> float:
        return value
