import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

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