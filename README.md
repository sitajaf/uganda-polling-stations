# uganda-voter-register
A simple python utility tool to covert the uganda voter register for 2016 general elections from excel to json


The current version on the electoral commission website (as of 15/12/2015) is already converted. It is `uganda-voter-register.json`

To convert another:
- clone the repo

- cd into it

- create a virtualenv:
  e.g `virtualenv ve --no-site-packages`
  
- install the requirements e.g with pip:
  `pip install -r requirements.txt`
- Copy your excel version (must be on same sheet, doesnt matter even if it has multiple titles in between so long as the headings are the same as in the current reg) to project dir

- In convert.py, change the `uganda-voter-register.xlsx` to your file name

- run `python converty.py`
