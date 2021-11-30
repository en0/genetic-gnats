from pygame import Rect
from random import choice
from simulation.sim import Sim
from simulation.selection_pressure import (
    TopThirdSelectionPressure,
    BottomThirdSelectionPressure,
    LeftThirdSelectionPressure,
    RightThirdSelectionPressure,
    SmallRightThirdSelectionPressure,
    CentralCircleSelectionPressure,
    OffCenterCircleSelectionPressure,
    ThinLineSelectionPressure,
)


def main():
    screen_size = 800, 600
    selectors = [
        #TopThirdSelectionPressure(Rect((0, 0), screen_size)),
        #BottomThirdSelectionPressure(Rect((0, 0), screen_size)),
        #LeftThirdSelectionPressure(Rect((0, 0), screen_size)),
        #RightThirdSelectionPressure(Rect((0, 0), screen_size)),
        #SmallRightThirdSelectionPressure(Rect((0, 0), screen_size)),
        #CentralCircleSelectionPressure(Rect((0, 0), screen_size)),
        #OffCenterCircleSelectionPressure(Rect((0, 0), screen_size)),
        ThinLineSelectionPressure(Rect((0, 0), screen_size)),
    ]
    sim = Sim(
        screen_size=screen_size,
        selector=choice(selectors),
        seed=100,
        neuron_connections=10,
        intermediate_neurons=5,
        mutation_factor=50,
        cycles_per_generation=1000,
        population_size=120,
    )
    sim.run()


if __name__ == "__main__":
    main()
