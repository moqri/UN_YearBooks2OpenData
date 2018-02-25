# UN YearBooks to OpenData

## Preparation
1. Download a UN Yearbook PDF from https://unstats.un.org/unsd/publications/statistical-yearbook/past-issues/ and place it in 1_yearbooks folder 
2. find pages containing tables and update the list in 2_table_page_numbers folder

## Software Requirement
1. PyPDF2 (https://pypi.python.org/pypi/PyPDF2) - need to be installed (pip install PyPDF2)
2. Tabula (http://tabula.technology/) - included (needs Java to be installed)

## Run 
``` 
./run.sh
```
Will produce PDF "cuts" in 3_table_pdfs folder and initial csv files in 4_table_csvs folder

## Cleaning
Data need to be manually cleaned. Cleaned data could be stored in 5_tables_cleaned folder
