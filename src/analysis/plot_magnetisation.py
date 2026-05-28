import os

import matplotlib.pyplot as plt
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
    AVG(abs_magnetization_mean) AS abs_magnetization_mean
FROM ising_mc_results
GROUP BY lattice_size, temperature
ORDER BY lattice_size, temperature;
"""


df = pd.read_sql(query, engine)


plt.figure(figsize=(8, 6))

for lattice_size in sorted(df["lattice_size"].unique()):

    subset = df[df["lattice_size"] == lattice_size]
    df = df.sort_values(["lattice_size", "temperature"])
    plt.plot(
        subset["temperature"],
        subset["abs_magnetization_mean"],
        marker="o",
        label=f"L={lattice_size}",
    )


plt.xlabel("Temperature T")
plt.ylabel("<|M|>")
plt.title("2D Ising Model: Magnetization vs Temperature")

plt.grid(True)
plt.legend()

plt.tight_layout()

plt.show()