# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo>=0.23.16",
#     "py2opsin==1.2.0",
#     "rdkit==2025.9.3",
# ]
# ///

import marimo

__generated_with = "0.23.16"
app = marimo.App(width="full")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Starting a Marimo notebook**

    To create or edit a marimo notebook, use the command: *marimo edit notebook_filename.py* in the terminal ([reference link](https://docs.marimo.io/getting_started/quickstart/) to show other related commands). It will then ask if you'd like to run this notebook in a sandboxed venv containing this notebooks's dependencies. By answering yes, this'll immediately take you to the notebook opened in your default web browser. This requires marimo to be installed earlier, and this Marimo [reference link](https://docs.marimo.io/getting_started/installation/) shows how to do it. Marimo notebooks work well with uv, a Python package installer and manager.

    The only other thing to note here is that Marimo notebooks currently only work with Python programming language and not other languages (unless there are new plans announced from the Marimo team).

    Marimo notebook apparently exists as a Python script so if it is opened in an editor (e.g. VS Code), it'll look different from how it appears in a browser as the code inside the notebook will look like it's for an app.
    """)
    return


@app.cell
def _():
    # apparently need this line below so markdown cells can be used
    import marimo as mo

    return (mo,)


@app.cell
def _():
    # sample code only
    from rdkit import Chem

    return (Chem,)


@app.cell
def _(Chem):
    #mol = Chem.MolFromSmiles('COC(=O)CNC(=O)CCCO')
    mol = Chem.MolFromSmiles("C1=CC=CC=C1")
    mol
    return (mol,)


@app.cell
def _(Chem, mol):
    f_group = Chem.MolFromSmarts('C=O')
    matches = mol.GetSubstructMatches(f_group)
    len(matches)
    return


@app.cell
def _():
    # https://github.com/dan2097/opsin
    # https://github.com/JacksonBurns/py2opsin
    from py2opsin import py2opsin

    return (py2opsin,)


@app.cell
def _(py2opsin):
    smiles_string = py2opsin(
        chemical_name = ["ethane", "cyclopentane", "benzene", "pyridine"], 
        output_format = "SMILES",
    )

    smiles_string
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    There are different types of SMILES available...
    """)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
