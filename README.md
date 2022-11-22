# EVE3D
Color-coding protein structure in PyMOL according to evolutionary conservation based on the Evolutionary model of Variant Effects (EVE) https://evemodel.org/.

## Credits
All credits belong to the **Marks lab** and **OATML group**  for developing the EVE model. Please find the original publication FYI and for reference here: https://www.nature.com/articles/s41586-021-04043-8

## Requirements

- python=3.7
- pandas=1.4.1
- pathlib=1.0.1
- sys
- os

## Usage

1. Download EVE prediction score from https://evemodel.org/ as .csv file for your gene of interest or as a bulk and unzip into EVE_csv folder.
2. Run EVE3D.py and enter: gene as named on EVE website, cut-offs for benign and deleterious as given by EVE multiplied by 100, object name of your protein in PyMOL.
3. Tool stores .pml file with the generated commands for PyMOL in the repo /Output folder.
4. Excecute .pml from PyMOL console by navigating into output folder (cd path) and run .pml file (@GENE.pml).

## Example result



https://user-images.githubusercontent.com/118387712/203362376-bceeb567-1b23-4059-87bb-560733113f75.MOV

