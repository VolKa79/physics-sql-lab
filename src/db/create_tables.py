import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)


create_experiments_table = """
CREATE TABLE IF NOT EXISTS experiments (
    id SERIAL PRIMARY KEY,
    model_name VARCHAR(100) NOT NULL,
    lattice_size INTEGER NOT NULL,
    temperature DOUBLE PRECISION,
    coupling_j DOUBLE PRECISION,
    steps INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""


with engine.connect() as connection:
    connection.execute(text(create_experiments_table))
    connection.commit()

print("Table experiments created successfully.")