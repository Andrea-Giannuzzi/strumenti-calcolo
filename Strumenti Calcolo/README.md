# Calculation Tools

`Strumenti Calcolo` is a collection of small Python scripts dedicated to
symbolic computation and to supporting physics and mathematics exercises.

The project begins with a script for symbolic derivatives, but it is designed
to grow: new files may be added in the future for other symbolic computation
tools, such as differential equations, symbolic linear algebra, series,
transforms, Lagrangian systems, or formula manipulation.

## Available Tools

| File | Purpose |
| --- | --- |
| `symbolic_derivatives.py` | Guided examples of symbolic derivatives, partial derivatives, composite functions, and terms in the Euler-Lagrange equation. |

## Requirements

The project mainly uses **SymPy**, the Python library best suited to symbolic
computation.

Recommended installation:

```bash
python3 -m pip install sympy
```

If you are working in a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install sympy
```

## Running the Scripts

From the `Strumenti Calcolo` directory:

```bash
python3 symbolic_derivatives.py
```

From the parent repository directory:

```bash
python3 "Strumenti Calcolo/symbolic_derivatives.py"
```

## Documentation for Individual Tools

For details about the current script:

- [`README_symbolic_derivatives.md`](README_symbolic_derivatives.md)

When new scripts are added, each may have brief dedicated documentation covering
its purpose, dependencies, execution command, and main examples.

## Planned Organization

The goal is to keep every tool simple, readable, and easy to modify:

- one Python file for each main topic;
- educational comments for mathematically important steps;
- ready-to-use examples with no mandatory interactive input;
- an updated main README listing the available tools;
- an optional dedicated README for the most important scripts.
