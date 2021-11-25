# merge_dups_row

## Description
Script to merge duplicates rows by the same values in a column.

- Group the data and apply set function.
- Expand the set into a dataframe.
- Rename the column or add prefix to the column names.
- Concatenate all the created dataframes and export.

## Usage
```bash
python3 merge_dups_row.py -v -f data.xlsx -g "First Name" -o output.xlsx
```

## Dependencies
[Pandas](https://pandas.pydata.org/)
```bash
python3 -m pip install pandas
```

## Help Message
```bash
usage: merge_dups_row.py [-h] [-v] -f FILE [-s SHEET] [-n NROWS] -g GROUPBY -o OUTPUT

Merge duplicates rows by the same values in a column.

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         verbosity
  -s SHEET, --sheet SHEET
                        sheet name or number
  -n NROWS, --nrows NROWS
                        number of rows

required named arguments:
  -f FILE, --file FILE  excel filename
  -g GROUPBY, --groupby GROUPBY
                        groupby column
  -o OUTPUT, --output OUTPUT
                        output filename
```

### Note
Tested with Python 3.8.10 and Pandas 1.3.4
