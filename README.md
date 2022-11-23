# EVE3D
Color-coding protein structure in PyMOL according to evolutionary conservation based on the Evolutionary model of Variant Effects (EVE) https://evemodel.org/.

# Overview
The EVE3D python script computes a mean EVE score per amino acid residue ranging from 0 (benign) to 1 (pathogenic) and translates these into PyMOL commands for color-coding each residue on a spectrum from blue (benign) to red (pathogenic). The tool regards the benign/pathogenic cut-offs provided by the EVE model. It is designed to allow color-coding of multiple protein objects in quaternary structures. Please note that EVE is not yet readily available for all human genes. 

## Credits
Credits belong to the **Marks lab** and **OATML group**  for developing the fantastic EVE model. Please find the original publication FYI and for reference here: https://www.nature.com/articles/s41586-021-04043-8

## Requirements

- python=3.7
- pandas=1.4.1
- pathlib=1.0.1
- sys
- os
- PyMOL

## Usage

1. Fetch structure (e.g., from RCSB or alphafold2). Make protein of interest a seperate object and assign object name. 
2. Download EVE prediction score from https://evemodel.org/ as .csv file for your gene of interest or as a bulk. Unzip into EVE_csv folder.
2. Run EVE3D.py. Enter: a) gene as named on EVE website, b) cut-offs for benign and c) pathogenic provided by EVE **multiplied by 100**, d) object name of your protein in PyMOL.
3. Tool stores .pml file with the generated PyMOL commands in the repo /Output folder.
4. Excecute .pml from PyMOL console by navigating into the output folder (cd path) and run .pml file (@GENE.pml).

## Example result



https://user-images.githubusercontent.com/118387712/203595773-03815438-c809-446e-8c22-3cf293bb8c41.mp4

