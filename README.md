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

- ## Monte Carlo temperature sweep

This project includes a Metropolis Monte Carlo implementation of the 2D Ising model.
The simulation can be run for multiple lattice sizes and temperatures. For each run, the measured physical observables are stored in a PostgreSQL database.

Stored observables include:

* mean energy per spin
* energy standard deviation
* mean magnetization per spin
* mean absolute magnetization per spin
* magnetization standard deviation
* heat capacity
* magnetic susceptibility

The main idea is to avoid recomputing expensive simulations. Results are saved permanently in SQL tables and can later be reused for analysis and plotting.

## Run temperature sweep

```bash
python src/run_temperature_sweep.py
```

## Load saved results

```bash
python src/analysis/load_ising_results.py
```

## Plot magnetization

```bash
python src/analysis/plot_magnetization.py
```

## Current database table

The main Monte Carlo results are stored in:

```text
ising_mc_results
```

This table contains simulation parameters, measured observables, and timestamps.

## Scientific goal

The project aims to reproduce basic finite-size behavior of the 2D Ising model near the critical temperature:

```text
Tc ≈ 2.269
```

Later extensions will include energy plots, heat capacity peaks, magnetic susceptibility, larger lattice sizes, cached runs, and more advanced statistical analysis.

