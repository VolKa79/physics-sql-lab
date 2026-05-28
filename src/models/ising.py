import numpy as np


class IsingModel:
    def __init__(self, size=10):
        self.size = size
        self.spins = np.random.choice([-1, 1], size=(size, size))

    def magnetization(self):
        return np.sum(self.spins)

    def energy(self):
        energy = 0

        for i in range(self.size):
            for j in range(self.size):

                S = self.spins[i, j]

                neighbors = (
                    self.spins[(i + 1) % self.size, j]
                    + self.spins[i, (j + 1) % self.size]
                    + self.spins[(i - 1) % self.size, j]
                    + self.spins[i, (j - 1) % self.size]
                )

                energy += -S * neighbors

        return energy / 2


if __name__ == "__main__":

    model = IsingModel(size=10)

    print("Spins:")
    print(model.spins)

    print("\nMagnetization:")
    print(model.magnetization())

    print("\nEnergy:")
    print(model.energy())