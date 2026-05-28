# Physics SQL Lab

A small scientific computing project for learning SQL, PostgreSQL, Python, testing, GitHub workflow, and CI/CD through computational physics examples.

The first implemented model is a basic 2D Ising model. Simulation results are stored in a PostgreSQL database and can be queried later for analysis.

## Project goals

- Learn SQL from scratch
- Connect Python with PostgreSQL
- Store computational physics experiments in a database
- Use Git and GitHub properly
- Add automated tests with pytest
- Run tests automatically with GitHub Actions CI
- Build toward a reproducible research-style workflow

## Current features

- Basic 2D Ising lattice
- Periodic boundary conditions
- Magnetization calculation
- Energy calculation
- PostgreSQL connection with SQLAlchemy
- Experiment logging into database
- Basic pytest tests
- GitHub Actions CI pipeline

## Project structure

```text
physics-sql-lab/
├── .github/workflows/ci.yml
├── notebooks/
├── src/
│   ├── analysis/
│   ├── db/
│   ├── models/
│   │   └── ising.py
│   └── run_experiment.py
├── tests/
│   └── test_ising.py
├── .gitignore
├── pytest.ini
├── README.md
└── requirements.txt

## Setup

Create and activate conda environment:

```bash
conda create -n physics_sql python=3.12
conda activate physics_sql
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql+psycopg2://postgres:YOUR_PASSWORD@localhost:5432/physics_lab
```

The `.env` file is ignored by Git and should not be committed.

## Run Ising model

```bash
python src/models/ising.py
```

## Run experiment and save to PostgreSQL

```bash
python src/run_experiment.py
```

## View saved experiments

```bash
python src/db/select_experiments.py
```

## Run tests

```bash
pytest
```

## Database table: experiments

Current columns:

- id
- model_name
- lattice_size
- temperature
- coupling_j
- steps
- created_at
- magnetization
- energy

## Roadmap

- Add temperature sweep for the Ising model
- Store many simulation runs automatically
- Add SQL queries for average energy and magnetization
- Add plots from database results
- Add more tests
- Add PostgreSQL service to GitHub Actions
- Add Docker Compose
- Add Streamlit dashboard
- Later: add Bose-Hubbard or Fermi-Hubbard toy models
