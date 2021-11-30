from unittest import TestCase
from unittest.mock import MagicMock

from brain.perceptron import Perceptron
from brain.typing import IActivator, IPerceptron


class PerceptronTest(TestCase):

    def setUp(self) -> None:
        self.ActivatorMock = MagicMock(spec=IActivator)

    def test_initialization_perceptron(self):
        activator_mock = self.ActivatorMock()
        p = Perceptron(activator_mock)
        self.assertTrue(True)

    def test_perceptron_calls_activator(self):
        activator_mock = self.ActivatorMock()
        p = Perceptron(activator_mock)
        p.signal(1)
        p.activate()
        activator_mock.assert_called()

    def test_signals_attached(self):
        activator_mock = self.ActivatorMock()
        output_mock = MagicMock(spec=IPerceptron)()
        activator_mock.return_value = 1
        p = Perceptron(activator_mock)
        p.attach_to(output_mock, 1)
        p.signal(1)
        p.activate()
        output_mock.signal.assert_called_with(1)

    def test_summation(self):
        activator_mock = self.ActivatorMock()
        output_mock = MagicMock(spec=IPerceptron)()
        activator_mock.side_effect = lambda x: x
        p = Perceptron(activator_mock)
        p.attach_to(output_mock, 1)
        p.signal(5)
        p.signal(6)
        p.signal(7)
        p.activate()
        output_mock.signal.assert_called_with(5 + 6 + 7)

    def test_summation_with_weight(self):
        activator_mock = self.ActivatorMock()
        output_mock = MagicMock(spec=IPerceptron)()
        activator_mock.side_effect = lambda x: x
        p = Perceptron(activator_mock)
        p.attach_to(output_mock, 2)
        p.signal(5)
        p.signal(6)
        p.signal(7)
        p.activate()
        output_mock.signal.assert_called_with((5 + 6 + 7) * 2)

    def test_summation_of_activator(self):
        activator_mock = self.ActivatorMock()
        output_mock = MagicMock(spec=IPerceptron)()
        activator_mock.side_effect = lambda x: 1
        p = Perceptron(activator_mock)
        p.attach_to(output_mock, 2)
        p.signal(5)
        p.signal(6)
        p.signal(7)
        p.activate()
        output_mock.signal.assert_called_with(2)

    def test_multiple_attachments(self):
        activator_mock = self.ActivatorMock()
        output_mock1 = MagicMock(spec=IPerceptron)()
        output_mock2 = MagicMock(spec=IPerceptron)()
        activator_mock.side_effect = lambda x: x
        p = Perceptron(activator_mock)
        p.attach_to(output_mock1, 2)
        p.attach_to(output_mock2, 4)
        p.signal(5)
        p.signal(6)
        p.signal(7)
        p.activate()
        output_mock1.signal.assert_called_with((5+6+7) * 2)
        output_mock2.signal.assert_called_with((5+6+7) * 4)
