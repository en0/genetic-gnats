import math
from typing import Optional

from .component_abc import SimComponentABC


class RelativeXAxisSensorNeuron(SimComponentABC):
    """Sensor for distance from X Center"""

    def signal(self, value: Optional[float] = 0) -> None:
        bx = self.parent.boundary.centerx
        x, _ = self.parent.location
        super().signal((x - bx) / 100)

    def update(self):
        pass


class RelativeYAxisSensorNeuron(SimComponentABC):
    """Sensor for distance from Y Center"""

    def signal(self, value: Optional[float] = 0) -> None:
        by = self.parent.boundary.centery
        _, y = self.parent.location
        super().signal((y - by) / 100)

    def update(self):
        pass


class XAxisSensorNeuron(SimComponentABC):

    def signal(self, value: Optional[float] = 0) -> None:
        x, _ = self.parent.location
        super().signal(x / 100)

    def update(self):
        pass


class NXAxisSensorNeuron(SimComponentABC):

    def signal(self, value: Optional[float] = 0) -> None:
        x, _ = self.parent.location
        super().signal(-(x / 100))

    def update(self):
        pass


class YAxisSensorNeuron(SimComponentABC):

    def signal(self, value: Optional[float] = 0) -> None:
        _, y = self.parent.location
        super().signal(y / 100)

    def update(self):
        pass


class NYAxisSensorNeuron(SimComponentABC):

    def signal(self, value: Optional[float] = 0) -> None:
        _, y = self.parent.location
        super().signal(-(y / 100))

    def update(self):
        pass


class PopulationSensorNeuron(SimComponentABC):

    def signal(self, value: Optional[float] = 0) -> None:
        rect = self.parent.rect.inflate(10, 10)
        count = len(self.parent.collection.collides_with(rect))
        super().signal(count)

    def update(self):
        pass


class RelativeDistanceFromCenterSensorNeuron(SimComponentABC):

    def signal(self, value: Optional[float] = 0) -> None:
        x, y = self.parent.boundary.center
        cx, cy = self.parent.location
        dx, dy = abs(cx - x), abs(cy - y)
        dist = math.sqrt(dx**2 + dy**2)
        super().signal(dist / 100)

    def update(self):
        pass
