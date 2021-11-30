from typing import Optional, List
from unittest import TestCase, skip
from brain import BrainBuilderABC, Perceptron, PassActivator
from brain.genome import GenomeParser
from brain.typing import IPerceptron, INeuralNetwork


class InputMock(Perceptron):
    def signal(self, value: Optional[float] = 0) -> None:
        super().signal(1)


class OutputMock(Perceptron):
    result: float = 0

    def activate(self):
        self.result += sum(self._input)
        self._input = []


class BuilderMock(BrainBuilderABC):

    activator = PassActivator()

    def build_input_neurons(self) -> List[IPerceptron]:
        return self.input_neurons

    def build_output_neurons(self) -> List[IPerceptron]:
        return self.output_neurons

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.input_neurons = [InputMock(PassActivator()) for _ in range(3)]
        self.output_neurons = [OutputMock(PassActivator()) for _ in range(3)]


class BrainBuilderTest(TestCase):

    def test_creates_builder(self):
        parser = GenomeParser()
        builder = BuilderMock(parser)
        brain = builder.build([
            0,
            0, 1, 0, 3, 0.1
        ])
        self.assertIsInstance(brain, INeuralNetwork)

    def test_creates_simple_network(self):
        parser = GenomeParser()
        builder = BuilderMock(parser)
        brain = builder.build([
            0,
            0, 1, 0, 1, 1.0
        ])
        brain.update()
        self.assertEqual(builder.output_neurons[1].result, 1.0)

    def test_creates_les_simple_network(self):
        parser = GenomeParser()
        builder = BuilderMock(parser)
        brain = builder.build([
            1,
            0, 0, 1, 0, 2.0,
            1, 0, 0, 1, 1.0,
        ])
        brain.update()
        self.assertEqual(builder.output_neurons[1].result, 2.0)

    def test_creates_unsimple_network(self):
        parser = GenomeParser()
        builder = BuilderMock(parser)
        brain = builder.build([
            1,
            0, 0, 1, 0, 2.0,
            1, 0, 1, 0, 2.0,
            1, 0, 0, 1, 1.0,
        ])
        brain.update()
        brain.update()
        self.assertEqual(8.0, builder.output_neurons[1].result)

