import os

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)


query = """
SELECT
    lattice_size,
    temperature,
    energy_mean,
    abs_magnetization_mean,
    heat_capacity,
    susceptibility
FROM ising_mc_results
ORDER BY lattice_size, temperature;
"""


df = pd.read_sql(query, engine)

print(df)