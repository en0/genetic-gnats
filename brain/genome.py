import itertools as it
from typing import Iterable, List

from .enum import NeuronTypeEnum
from .model import Gene
from .typing import IGenomeParser


def _grouper(iterable, n, fill_value=None):
    args = [iter(iterable)] * n
    return it.zip_longest(*args, fillvalue=fill_value)


class GenomeParser(IGenomeParser):

    def as_gene(self, gene: List[any]) -> Gene:
        (
            source_neuron_type,
            source_neuron_id,
            target_neuron_type,
            target_neuron_id,
            connection_weight,
        ) = gene
        return Gene(
            source_neuron_type=NeuronTypeEnum(source_neuron_type % 2),
            source_neuron_id=source_neuron_id,
            target_neuron_type=NeuronTypeEnum(target_neuron_type % 2),
            target_neuron_id=target_neuron_id,
            connection_weight=float(connection_weight),
        )

    def get_intermediate_neuron_count(self, genome: List[int]) -> int:
        return int(genome[0])

    def parse_genome(self, genome: List[int]) -> Iterable[Gene]:
        for gene in _grouper(genome[1:], 5):
            yield self.as_gene(gene)
