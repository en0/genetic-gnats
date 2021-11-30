from typing import List
from abc import ABC, abstractmethod

from .enum import NeuronTypeEnum
from .neural_net import NeuralNetwork
from .activator import LogisticActivator
from .perceptron import Perceptron
from .typing import INeuralNetwork, IGenomeParser, IPerceptron


def _select_from(identity: int, members: List[IPerceptron]) -> IPerceptron:
    index = identity % len(members)
    return members[index]


class BrainBuilderABC(ABC):

    activator = LogisticActivator()

    @abstractmethod
    def build_input_neurons(self) -> List[IPerceptron]:
        ...

    def build_intermediate_neurons(self, count: int) -> List[IPerceptron]:
        return [
            Perceptron(self.activator)
            for _ in range(count)
        ]

    @abstractmethod
    def build_output_neurons(self) -> List[IPerceptron]:
        ...

    def build(self, genome: List[int]) -> INeuralNetwork:

        intermediate_neuron_count = self._parser.get_intermediate_neuron_count(genome)
        input_neurons = self.build_input_neurons()
        intermediate_neurons = self.build_intermediate_neurons(intermediate_neuron_count)
        output_neurons = self.build_output_neurons()

        nn = NeuralNetwork(
            input_neurons=input_neurons,
            intermediate_neurons=intermediate_neurons,
            output_neurons=output_neurons,
        )

        for gene in self._parser.parse_genome(genome):
            source_neuron = (
                _select_from(gene.source_neuron_id, input_neurons)
                if gene.source_neuron_type == NeuronTypeEnum.INPUT_NEURON or intermediate_neuron_count == 0
                else _select_from(gene.source_neuron_id, intermediate_neurons)
            )
            target_neuron = (
                _select_from(gene.target_neuron_id, output_neurons)
                if gene.target_neuron_type == NeuronTypeEnum.OUTPUT_NEURON or intermediate_neuron_count == 0
                else _select_from(gene.target_neuron_id, intermediate_neurons)
            )
            source_neuron.attach_to(target_neuron, gene.connection_weight)

        return nn

    def __init__(self, genome_parser: IGenomeParser):
        self._parser = genome_parser
