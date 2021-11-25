#! /usr/bin/env python3
"""
Script to merge duplicates rows by the same values in a column.

- Group the data and apply set function.
- Expand the set into a dataframe.
- Rename the column or add prefix to the column names.
- Concatenate all the created dataframes and export.

Usage:
    python3 merge_dups_row.py -v -f data.xlsx -g "First Name" -o output.xlsx
"""


import argparse

import pandas as pd


# Create argument parser
parser = argparse.ArgumentParser(description="Merge duplicates rows by the same values in a column.")
required_argument = parser.add_argument_group("required named arguments")
parser.add_argument("-v", "--verbose", action="store_true", help="verbosity")
required_argument.add_argument("-f", "--file", help="excel filename", required=True)
parser.add_argument("-s", "--sheet", default=0, help="sheet name or number")
parser.add_argument("-n", "--nrows", default=None, type=int, help="number of rows")
required_argument.add_argument("-g", "--groupby", help="groupby column", required=True)
required_argument.add_argument("-o", "--output", help="output filename", required=True)

args = parser.parse_args()

# Store arguments in variables.
verbose = args.verbose
fileName = args.file

try:
    sheet = int(args.sheet)
except ValueError:
    sheet = args.sheet

nRows = args.nrows
groupbyCol = args.groupby
outFileName = args.output


# Read excel file, assuming data on the first sheet.
df = pd.read_excel(fileName, sheet_name=sheet, nrows=nRows)
if verbose:
    print("Original Data")
    print(df)
    print()


# Apply set function to all columns except the groupbyCol column.
# Set prevent duplicates values!! :)
df_merged = df.groupby(groupbyCol).agg(set).reset_index()
if verbose:
    print("Data merged into a set")
    print(df_merged)
    print()


# Get all column names.
cols = df_merged.columns.values

# Create an empty df_list.
df_list = []

# Loop through all column names.
for col in cols:
    # Expand the set in the column to different columns in a dataframe.
    df_tmp = pd.DataFrame(df_merged[col].tolist())

    if len(df_tmp.columns) > 1:
        # If new dataframe has multiple column, add prefix of the column name.
        df_tmp = df_tmp.add_prefix(f"{col}_")
    else:
        # If new dataframe has only one column, just rename the column.
        df_tmp.columns = [f"{col}"]

    # Append the dataframe to the list.
    df_list.append(df_tmp)

# Concatenate the dataframes in the list along the columns.
df_output = pd.concat(df_list, axis=1)
if verbose:
    print("Data merged into separate columns")
    print(df_output)
    print()


# Export to an excel file.
df_output.to_excel(outFileName, index=False)
