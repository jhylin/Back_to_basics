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


@app.cell
def _():
    import marimo as mo

    return


@app.cell
def _():
    # sample code only
    from rdkit import Chem

    return (Chem,)


@app.cell
def _(Chem):
    mol = Chem.MolFromSmiles('COC(=O)CNC(=O)CCCO')
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
    from py2opsin import py2opsin

    return (py2opsin,)


@app.cell
def _(py2opsin):
    smiles_string = py2opsin(
        chemical_name = "ethane",
        output_format = "SMILES",
    )

    smiles_string
    return


if __name__ == "__main__":
    app.run()
