from calculator.PersonaFusionCalculator import PersonaFusionCalculator

calculator = PersonaFusionCalculator()


def test_simple_fuse_two_personas():
    result = calculator.get_fusion_result(['Silky', 'Arsene'])
    assert result == 'Succubus'

    result = calculator.get_fusion_result(['Silky', 'Pixie'])
    assert result == 'Clotho'
