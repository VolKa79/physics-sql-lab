from sqlalchemy import create_engine, text


DATABASE_URL = "postgresql+psycopg2://postgres:1488@localhost:5432/physics_lab"

engine = create_engine(DATABASE_URL)


alter_query_1 = """
ALTER TABLE experiments
ADD COLUMN IF NOT EXISTS magnetization DOUBLE PRECISION;
"""

alter_query_2 = """
ALTER TABLE experiments
ADD COLUMN IF NOT EXISTS energy DOUBLE PRECISION;
"""


with engine.connect() as connection:

    connection.execute(text(alter_query_1))
    connection.execute(text(alter_query_2))

    connection.commit()

print("Table updated successfully.")