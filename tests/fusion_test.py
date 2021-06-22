import unittest
from calculator.PersonaFusionCalculator import PersonaFusionCalculator


class FusionTests(unittest.TestCase):
    calculator = PersonaFusionCalculator()

    def test_simple_fuse_two_personas(self):
        result = self.calculator.get_fusion_result(['Silky', 'Arsene'])
        self.assertEqual(result, 'Succubus')

        result = self.calculator.get_fusion_result(['Silky', 'Pixie'])
        self.assertEqual(result, 'Clotho')


if __name__ == '__main__':
    unittest.main()
