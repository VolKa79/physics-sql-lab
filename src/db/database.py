from sqlalchemy import create_engine


DATABASE_URL = "postgresql+psycopg2://postgres:1488@localhost:5432/physics_lab"


engine = create_engine(DATABASE_URL)

connection = engine.connect()

print("Successfully connected to PostgreSQL!")

connection.close()