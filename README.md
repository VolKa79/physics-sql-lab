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
