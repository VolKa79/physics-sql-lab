import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)


insert_query = """
INSERT INTO experiments (
    model_name,
    lattice_size,
    temperature,
    coupling_j,
    steps
)
VALUES (
    :model_name,
    :lattice_size,
    :temperature,
    :coupling_j,
    :steps
);
"""


with engine.connect() as connection:
    connection.execute(
        text(insert_query),
        {
            "model_name": "ising_2d",
            "lattice_size": 10,
            "temperature": 2.0,
            "coupling_j": 1.0,
            "steps": 0,
        },
    )
    connection.commit()

print("Experiment inserted successfully.")