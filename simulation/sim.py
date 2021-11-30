import pygame
import random
from typing import Tuple

from .interface import ISimObjectCollection, ISelectionPressure
from .sim_object_factory import SimulatorObjectFactory
from .sim_object_collection import SimulationObjectCollection


class Sim:

    screen_size: Tuple[int, int]
    is_running: bool = False
    screen: pygame.Surface
    frame_delay: int
    boundary: pygame.Rect
    sim_objects: ISimObjectCollection = None
    cycles_per_generation: int = 500
    population_size: int = 100

    def run(self):
        cycles = 0

        self.is_running = True
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("Evolution Simulator")

        clock = pygame.time.Clock()
        self.frame_delay = clock.tick()
        while self.is_running:
            self.is_running = not pygame.event.get(pygame.QUIT)
            self.screen.fill((0, 0, 0))

            if cycles == 0:
                self.populate()

            self.sim_objects.compile()

            for sim_object in self.sim_objects:
                sim_object.think()
            for sim_object in self.sim_objects:
                sim_object.update()
            for sim_object in self.sim_objects:
                sim_object.draw(self.screen)

            self.selector.draw(self.screen)
            pygame.draw.rect(self.screen, (255, 0, 0), self.boundary, width=1)
            pygame.display.flip()

            cycles = (cycles + 1) % self.cycles_per_generation
            self.frame_delay = clock.tick()

    def populate(self) -> None:
        if self.sim_objects is None:
            self.sim_objects = SimulationObjectCollection(self.screen.get_rect())
            for _ in range(self.population_size):
                n = self.obj_factory.new()
                while any([n.rect.colliderect(o.rect) for o in self.sim_objects if o != n]):
                    n.location = self.obj_factory.random_location()
                self.sim_objects.add_member(n)
            return

        self.sim_objects.compile()

        offspring = []
        parents = self.selector.select(self.sim_objects)

        print(f"{len(parents) / self.population_size * 100}% Survival Rate")

        while len(offspring) < self.population_size:
            n = self.obj_factory.reproduce(
                random.choice(parents),
                random.choice(parents),
            )
            while any([n.rect.colliderect(o.rect) for o in offspring if o != n]):
                n.location = self.obj_factory.random_location()
            offspring.append(n)

        self.sim_objects.clear()
        for member in offspring:
            self.sim_objects.add_member(member)

    def __init__(self, screen_size: Tuple[int, int], selector: ISelectionPressure, **kwargs):
        kwargs.setdefault("cycles_per_generation", 500)
        kwargs.setdefault("population_size", 100)
        self.selector = selector
        self.screen_size = screen_size
        self.boundary = pygame.Rect(
            pygame.Vector2(10),
            pygame.Vector2(self.screen_size) - pygame.Vector2(20)
        )
        self.obj_factory = SimulatorObjectFactory(self.boundary, **kwargs)
        self.cycles_per_generation = kwargs["cycles_per_generation"]
        self.population_size = kwargs["population_size"]
