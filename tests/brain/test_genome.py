from unittest import TestCase
from brain.genome import GenomeParser, NeuronTypeEnum


class GenomeParserTest(TestCase):

    def test_as_gene_intermediate_neuron_count(self):
        gp = GenomeParser()
        i = gp.get_intermediate_neuron_count([3])
        self.assertEqual(i, 3)

    def test_as_gene_source_neuron_type_is_source(self):
        gp = GenomeParser()
        gene = gp.as_gene([0, 0, 0, 0, 0])
        self.assertEqual(gene.source_neuron_type, NeuronTypeEnum.INPUT_NEURON)

    def test_as_gene_source_neuron_type_is_source_forced(self):
        gp = GenomeParser()
        gene = gp.as_gene([10, 0, 0, 0, 0])
        self.assertEqual(gene.source_neuron_type, NeuronTypeEnum.INPUT_NEURON)

    def test_as_gene_source_neuron_type_is_intermediate(self):
        gp = GenomeParser()
        gene = gp.as_gene([1, 0, 0, 0, 0])
        self.assertEqual(gene.source_neuron_type, NeuronTypeEnum.INTERMEDIATE_NEURON)

    def test_as_gene_source_neuron_type_is_intermediate_forced(self):
        gp = GenomeParser()
        gene = gp.as_gene([21, 0, 0, 0, 0])
        self.assertEqual(gene.source_neuron_type, NeuronTypeEnum.INTERMEDIATE_NEURON)

    def test_as_gene_source_neuron_id(self):
        gp = GenomeParser()
        gene = gp.as_gene([0, 3, 0, 0, 0])
        self.assertEqual(gene.source_neuron_id, 3)

    def test_as_gene_target_neuron_type_is_source(self):
        gp = GenomeParser()
        gene = gp.as_gene([0, 0, 0, 0, 0])
        self.assertEqual(gene.target_neuron_type, NeuronTypeEnum.INPUT_NEURON)

    def test_as_gene_target_neuron_type_is_source_forced(self):
        gp = GenomeParser()
        gene = gp.as_gene([0, 0, 10, 0, 0])
        self.assertEqual(gene.target_neuron_type, NeuronTypeEnum.INPUT_NEURON)

    def test_as_gene_target_neuron_type_is_intermediate(self):
        gp = GenomeParser()
        gene = gp.as_gene([0, 0, 1, 0, 0])
        self.assertEqual(gene.target_neuron_type, NeuronTypeEnum.INTERMEDIATE_NEURON)

    def test_as_gene_target_neuron_type_is_intermediate_forced(self):
        gp = GenomeParser()
        gene = gp.as_gene([0, 0, 21, 0, 0])
        self.assertEqual(gene.target_neuron_type, NeuronTypeEnum.INTERMEDIATE_NEURON)

    def test_as_gene_target_neuron_id(self):
        gp = GenomeParser()
        gene = gp.as_gene([0, 0, 0, 3, 0])
        self.assertEqual(gene.target_neuron_id, 3)

    def test_as_gene_connection_weight(self):
        gp = GenomeParser()
        gene = gp.as_gene([0, 0, 0, 0, 0.1])
        self.assertEqual(gene.connection_weight, 0.1)

    def test_parse_genome_returns_nodes(self):
        gp = GenomeParser()
        genes = gp.parse_genome([
            10,
            2, 3, 4, 5, 0.6,
            5, 4, 3, 2, 0.1,
        ])
        self.assertEqual(len(list(genes)), 2)

    def test_parse_genome_gene_one(self):
        gp = GenomeParser()
        gene1, gene2 = gp.parse_genome([
            10,
            2, 3, 4, 5, 0.6,
            5, 4, 3, 2, 0.1,
        ])
        self.assertEqual((
            NeuronTypeEnum.INPUT_NEURON, 3, NeuronTypeEnum.INPUT_NEURON, 5, 0.6
        ), gene1)

    def test_parse_genome_gene_two(self):
        gp = GenomeParser()
        gene1, gene2 = gp.parse_genome([
            10,
            2, 3, 4, 5, 6,
            5, 4, 3, 2, 1,
        ])
        self.assertEqual((
            NeuronTypeEnum.INTERMEDIATE_NEURON, 4, NeuronTypeEnum.INTERMEDIATE_NEURON, 2, 1.0
        ), gene2)
