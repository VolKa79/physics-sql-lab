from sqlalchemy import create_engine, text


DATABASE_URL = "postgresql+psycopg2://postgres:1488@localhost:5432/physics_lab"

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