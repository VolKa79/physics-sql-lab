from sqlalchemy import create_engine, text


DATABASE_URL = "postgresql+psycopg2://postgres:1488@localhost:5432/physics_lab"

engine = create_engine(DATABASE_URL)


select_query = """
SELECT *
FROM experiments;
"""


with engine.connect() as connection:

    result = connection.execute(text(select_query))

    for row in result:
        print(row)