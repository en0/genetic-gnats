from typing import NamedTuple

from .enum import NeuronTypeEnum


class Gene(NamedTuple):
    source_neuron_type: NeuronTypeEnum
    source_neuron_id: int
    target_neuron_type: NeuronTypeEnum
    target_neuron_id: int
    connection_weight: float
