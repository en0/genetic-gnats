import pygame
from typing import Iterable
from pygame import Surface
from abc import ABC, abstractmethod
from typing import Tuple, List


class IComponent(ABC):

    @abstractmethod
    def update(self):
        ...


class ISimObjectCollection(ABC):

    @abstractmethod
    def compile(self) -> None:
        ...

    @abstractmethod
    def add_member(self, member: "ISimObject") -> None:
        ...

    @abstractmethod
    def clear(self) -> None:
        ...

    @abstractmethod
    def collides_with(self, rect: pygame.Rect) -> List["ISimObject"]:
        ...

    @abstractmethod
    def __iter__(self):
        ...


class ISimObject(ABC):

    size: Tuple[float, float]
    vector: Tuple[float, float]
    boundary: pygame.Rect
    location: Tuple[float, float]
    collection: ISimObjectCollection

    @property
    @abstractmethod
    def rect(self) -> pygame.Rect:
        ...

    @abstractmethod
    def think(self):
        ...

    @abstractmethod
    def update(self):
        ...

    @abstractmethod
    def draw(self, gfx: Surface):
        ...


class ISelectionPressure(ABC):

    @abstractmethod
    def select(self, population: ISimObjectCollection):
        ...

    @abstractmethod
    def draw(self, gfx: Surface):
        ...