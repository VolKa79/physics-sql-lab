import numpy as np


class IsingModel:
    def __init__(self, size=10, temperature=2.0, coupling_j=1.0, seed=None):

        # Linear lattice size: total number of spins = size x size
        self.size = size

        # Temperature T in units where k_B = 1
        self.temperature = temperature

        # Ferromagnetic coupling constant J
        self.coupling_j = coupling_j

        # Random number generator for reproducibility
        self.rng = np.random.default_rng(seed)

        # Random initial spin configuration (+1 or -1)
        self.spins = self.rng.choice([-1, 1], size=(size, size))

    def magnetization(self):

        # Total magnetization:
        # M = Σ s_i
        return np.sum(self.spins)

    def energy(self):

        # Total Ising Hamiltonian:
        #
        # H = -J Σ s_i s_j
        #
        # with nearest-neighbor interactions
        # and periodic boundary conditions.

        energy = 0.0

        for i in range(self.size):
            for j in range(self.size):

                spin = self.spins[i, j]

                # 4 nearest neighbors on square lattice
                neighbors = (
                    self.spins[(i + 1) % self.size, j]
                    + self.spins[(i - 1) % self.size, j]
                    + self.spins[i, (j + 1) % self.size]
                    + self.spins[i, (j - 1) % self.size]
                )

                energy += -self.coupling_j * spin * neighbors

        # Each bond counted twice
        return energy / 2.0

    def metropolis_step(self):

        # Choose random spin
        i = self.rng.integers(0, self.size)
        j = self.rng.integers(0, self.size)

        spin = self.spins[i, j]

        neighbors = (
            self.spins[(i + 1) % self.size, j]
            + self.spins[(i - 1) % self.size, j]
            + self.spins[i, (j + 1) % self.size]
            + self.spins[i, (j - 1) % self.size]
        )

        # Energy difference for proposed spin flip:
        #
        # ΔE = E_new - E_old
        #
        # For Ising nearest-neighbor interaction:
        #
        # ΔE = 2 J s_i Σ_neighbors s_j
        delta_e = 2.0 * self.coupling_j * spin * neighbors

        # Metropolis acceptance rule
        #
        # Always accept if energy decreases.
        if delta_e <= 0:
            self.spins[i, j] *= -1

        else:

            # Otherwise accept thermally
            #
            # P = exp(-ΔE / T)
            probability = np.exp(-delta_e / self.temperature)

            if self.rng.random() < probability:
                self.spins[i, j] *= -1

    def run(self, equilibration_steps=1000, measurement_steps=3000):

        # Thermalization / equilibration stage:
        #
        # System relaxes toward equilibrium distribution.
        for _ in range(equilibration_steps):
            self.metropolis_step()

        energies = []
        magnetizations = []

        # Measurement stage
        for _ in range(measurement_steps):

            self.metropolis_step()

            energies.append(self.energy())
            magnetizations.append(self.magnetization())

        energies = np.array(energies, dtype=float)
        magnetizations = np.array(magnetizations, dtype=float)

        n_spins = self.size * self.size

        # Intensive observables (per spin)
        energy_mean = np.mean(energies) / n_spins
        energy_std = np.std(energies) / n_spins

        magnetization_mean = np.mean(magnetizations) / n_spins

        # |M| is important because finite systems
        # fluctuate between positive and negative phases
        abs_magnetization_mean = np.mean(np.abs(magnetizations)) / n_spins

        magnetization_std = np.std(magnetizations) / n_spins

        # Heat capacity:
        #
        # C_v = ( <E²> - <E>² ) / (N T²)
        heat_capacity = np.var(energies) / (
            n_spins * self.temperature**2
        )

        # Magnetic susceptibility:
        #
        # χ = ( <M²> - <|M|>² ) / (N T)
        susceptibility = np.var(np.abs(magnetizations)) / (
            n_spins * self.temperature
        )

        return {
            "energy_mean": float(energy_mean),
            "energy_std": float(energy_std),
            "magnetization_mean": float(magnetization_mean),
            "abs_magnetization_mean": float(abs_magnetization_mean),
            "magnetization_std": float(magnetization_std),
            "heat_capacity": float(heat_capacity),
            "susceptibility": float(susceptibility),
        }


if __name__ == "__main__":

    model = IsingModel(
        size=10,
        temperature=2.0,
        coupling_j=1.0,
        seed=42,
    )

    results = model.run(
        equilibration_steps=1000,
        measurement_steps=3000,
    )

    print(results)