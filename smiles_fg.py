# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo>=0.23.16",
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


if __name__ == "__main__":
    app.run()
