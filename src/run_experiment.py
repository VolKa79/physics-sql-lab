from sqlalchemy import create_engine, text

from models.ising import IsingModel


DATABASE_URL = "postgresql+psycopg2://postgres:1488@localhost:5432/physics_lab"

engine = create_engine(DATABASE_URL)


def save_experiment(
    model_name,
    lattice_size,
    temperature,
    coupling_j,
    steps,
    magnetization,
    energy,
):
    query = """
    INSERT INTO experiments (
        model_name,
        lattice_size,
        temperature,
        coupling_j,
        steps,
        magnetization,
        energy
    )
    VALUES (
        :model_name,
        :lattice_size,
        :temperature,
        :coupling_j,
        :steps,
        :magnetization,
        :energy
    );
    """

    with engine.connect() as connection:
        connection.execute(
            text(query),
            {
                "model_name": model_name,
                "lattice_size": lattice_size,
                "temperature": temperature,
                "coupling_j": coupling_j,
                "steps": steps,
                "magnetization": magnetization,
                "energy": energy,
            },
        )
        connection.commit()


if __name__ == "__main__":
    lattice_size = 10
    temperature = 2.0
    coupling_j = 1.0
    steps = 0

    model = IsingModel(size=lattice_size)

    magnetization = float(model.magnetization())
    energy = float(model.energy())

    save_experiment(
        model_name="ising_2d",
        lattice_size=lattice_size,
        temperature=temperature,
        coupling_j=coupling_j,
        steps=steps,
        magnetization=magnetization,
        energy=energy,
    )

    print("Experiment saved.")
    print(f"Magnetization: {magnetization}")
    print(f"Energy: {energy}")