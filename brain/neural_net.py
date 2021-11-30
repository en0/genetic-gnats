from typing import List

from .typing import INeuralNetwork, IPerceptron


class NeuralNetwork(INeuralNetwork):

    def update(self):
        for neuron in self._inputs:
            neuron.signal()
            neuron.activate()
        for neuron in self._intermediate:
            neuron.activate()
        for neuron in self._output:
            neuron.activate()

    def __init__(
        self,
        input_neurons: List[IPerceptron],
        intermediate_neurons: List[IPerceptron],
        output_neurons: List[IPerceptron],
    ):
        self._inputs = input_neurons
        self._intermediate = intermediate_neurons
        self._output = output_neurons
