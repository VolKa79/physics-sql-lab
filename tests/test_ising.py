from src.models.ising import IsingModel


def test_magnetization_range():
    model = IsingModel(size=10)

    magnetization = model.magnetization()

    assert -100 <= magnetization <= 100


def test_energy_is_number():
    model = IsingModel(size=10)

    energy = model.energy()

    assert isinstance(energy, float)