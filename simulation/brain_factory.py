from typing import List
from brain import BrainBuilderABC
from brain.typing import IPerceptron
from brain.genome import GenomeParser

from .interface import ISimObject


class BrainFactory(BrainBuilderABC):
    def build_input_neurons(self) -> List[IPerceptron]:
        return self.input_neurons

    def build_output_neurons(self) -> List[IPerceptron]:
        return self.output_neurons

    def __init__(
        self,
        sim_object: ISimObject,
        input_neurons: List[IPerceptron],
        output_neurons: List[IPerceptron]
    ):
        super().__init__(GenomeParser())
        self.input_neurons = input_neurons
        self.output_neurons = output_neurons
        self.obj = sim_object
