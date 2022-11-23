# EVE3D
Color-coding protein structure in PyMOL according to evolutionary conservation based on the Evolutionary model of Variant Effects (EVE) https://evemodel.org/.

## Credits
Credits belong to the **Marks lab** and **OATML group**  for developing the fantastic EVE model. Please find the original publication FYI and for reference here: https://www.nature.com/articles/s41586-021-04043-8

## Requirements

- python=3.7
- pandas=1.4.1
- pathlib=1.0.1
- sys
- os

## Usage

1. Download EVE prediction score from https://evemodel.org/ as .csv file for your gene of interest or as a bulk. Unzip into EVE_csv folder.
2. Run EVE3D.py. Enter: a) gene as named on EVE website, b) cut-offs for benign and c) deleterious provided by EVE multiplied by 100, d) object name of your protein in PyMOL.
3. Tool stores .pml file with the generated PyMOL commands in the repo /Output folder.
4. Excecute .pml from PyMOL console by navigating into the output folder (cd path) and run .pml file (@GENE.pml).

## Example result
