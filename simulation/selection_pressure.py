from typing import Tuple

from pygame import Surface, Rect, draw, Vector2

from .interface import ISelectionPressure, ISimObjectCollection


class RegionSelectionPressure(ISelectionPressure):

    region: Rect
    image: Surface

    def select(self, population: ISimObjectCollection):
        return population.collides_with(self.region)

    def draw(self, gfx: Surface):
        gfx.blit(self.image, self.region)

    def init_image(self):
        self.image = Surface(self.region.size)
        self.image.fill((0, 100, 0))
        self.image.set_alpha(50)


class TopThirdSelectionPressure(RegionSelectionPressure):

    def __init__(self, boundary: Rect):
        self.region = boundary.copy()
        self.region.height = self.region.height // 3
        self.init_image()


class BottomThirdSelectionPressure(RegionSelectionPressure):

    def __init__(self, boundary: Rect):
        self.region = boundary.copy()
        self.region.height = self.region.height // 3
        self.region.bottom = boundary.bottom
        self.init_image()


class LeftThirdSelectionPressure(RegionSelectionPressure):

    def __init__(self, boundary: Rect):
        self.region = boundary.copy()
        self.region.width = self.region.width // 3
        self.init_image()


class RightThirdSelectionPressure(RegionSelectionPressure):

    def __init__(self, boundary: Rect):
        self.region = boundary.copy()
        self.region.width = self.region.width // 3
        self.region.right = boundary.right
        self.init_image()


class SmallRightThirdSelectionPressure(RegionSelectionPressure):

    def __init__(self, boundary: Rect):
        self.region = boundary.copy()
        self.region.width = self.region.width // 3
        self.region.height = self.region.height // 3
        self.region.right = boundary.right
        self.region.midleft = boundary.midleft
        self.init_image()


class ThinLineSelectionPressure(RegionSelectionPressure):

    def __init__(self, boundary: Rect):
        self.region = boundary.copy()
        self.region.width = 100
        self.region.left += 120
        self.init_image()


class CircleSelectionPressure(ISelectionPressure):

    image: Surface
    region: Rect
    diameter: int = 200
    offset: Tuple[float, float] = 0, 0

    def select(self, population: ISimObjectCollection):
        result = []
        for a in population.collides_with(self.region):
            if Vector2(a.rect.center).distance_to(self.region.center) < self.diameter // 2:
                result.append(a)
        return result

    def draw(self, gfx: Surface):
        gfx.blit(self.image, self.region)

    def init_image(self):
        self.image = Surface(self.region.size)
        draw.circle(self.image, (0, 100, 0), self.image.get_rect().center, self.diameter // 2)
        self.image.set_alpha(50)

    def __init__(self, boundary: Rect):
        self.region = Rect(0, 0, self.diameter, self.diameter)
        self.region.center = boundary.center + Vector2(self.offset)
        self.init_image()


class CentralCircleSelectionPressure(CircleSelectionPressure):
    offset: Tuple[float, float] = 0, 0


class OffCenterCircleSelectionPressure(CircleSelectionPressure):
    offset = 120, 120
