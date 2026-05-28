import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, text


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)


create_table_query = """
CREATE TABLE IF NOT EXISTS ising_mc_results (
    id SERIAL PRIMARY KEY,

    lattice_size INTEGER NOT NULL,
    temperature DOUBLE PRECISION NOT NULL,
    coupling_j DOUBLE PRECISION NOT NULL,

    equilibration_steps INTEGER NOT NULL,
    measurement_steps INTEGER NOT NULL,

    energy_mean DOUBLE PRECISION,
    energy_std DOUBLE PRECISION,

    magnetization_mean DOUBLE PRECISION,
    abs_magnetization_mean DOUBLE PRECISION,
    magnetization_std DOUBLE PRECISION,

    heat_capacity DOUBLE PRECISION,
    susceptibility DOUBLE PRECISION,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""


with engine.connect() as connection:
    connection.execute(text(create_table_query))
    connection.commit()

print("Table ising_mc_results created successfully.")