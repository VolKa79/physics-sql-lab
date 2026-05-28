import os
import time

from dotenv import load_dotenv
from sqlalchemy import create_engine, text

from models.ising_mc import IsingModel


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)


def save_result(
    lattice_size,
    temperature,
    coupling_j,
    equilibration_steps,
    measurement_steps,
    results,
):

    

    insert_query = """
    INSERT INTO ising_mc_results (

        lattice_size,
        temperature,
        coupling_j,

        equilibration_steps,
        measurement_steps,

        energy_mean,
        energy_std,

        magnetization_mean,
        abs_magnetization_mean,
        magnetization_std,

        heat_capacity,
        susceptibility

    )
    VALUES (

        :lattice_size,
        :temperature,
        :coupling_j,

        :equilibration_steps,
        :measurement_steps,

        :energy_mean,
        :energy_std,

        :magnetization_mean,
        :abs_magnetization_mean,
        :magnetization_std,

        :heat_capacity,
        :susceptibility
    );
    """

    with engine.connect() as connection:

        connection.execute(
            text(insert_query),
            {
                "lattice_size": lattice_size,
                "temperature": temperature,
                "coupling_j": coupling_j,

                "equilibration_steps": equilibration_steps,
                "measurement_steps": measurement_steps,

                "energy_mean": results["energy_mean"],
                "energy_std": results["energy_std"],

                "magnetization_mean": results["magnetization_mean"],
                "abs_magnetization_mean": results["abs_magnetization_mean"],
                "magnetization_std": results["magnetization_std"],

                "heat_capacity": results["heat_capacity"],
                "susceptibility": results["susceptibility"],
            },
        )

        connection.commit()


if __name__ == "__main__":
    start_time = time.perf_counter() 
    lattice_sizes = [10, 20]

    temperatures = [
        1.5,
        1.8,
        2.0,
        2.2,
        2.269,
        2.4,
        2.6,
        3.0,
    ]

    equilibration_steps = 1000
    measurement_steps = 3000

    for lattice_size in lattice_sizes:

        for temperature in temperatures:

            print(
                f"Running L={lattice_size}, T={temperature}"
            )

            model = IsingModel(
                size=lattice_size,
                temperature=temperature,
                coupling_j=1.0,
            )

            results = model.run(
                equilibration_steps=equilibration_steps,
                measurement_steps=measurement_steps,
            )

            print(results)

            save_result(
                lattice_size=lattice_size,
                temperature=temperature,
                coupling_j=1.0,
                equilibration_steps=equilibration_steps,
                measurement_steps=measurement_steps,
                results=results,
            )

            print("Saved to database.\n")

    print("Temperature sweep completed.")
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time

    print(f"Total runtime: {elapsed_time:.2f} seconds")
    print(f"Total runtime: {elapsed_time / 60:.2f} minutes")