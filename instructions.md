
# Goal

Write a simple python app processing csv and excel files.

# Overview

The app should be able to:
- read csv and excel files
- validate the data against a Pydantic model.
- merge multiple excel files into one
- merge multiple csv files into one

# Details

This a dummy app, but think about a realistic scenario.

1. Define a Pydantic model using various type of fields (str, int, float, bool, list, dates.)
2. Do not hesitate to create a preprocessing function to transform the data into the good format before validating it.
3. Create a function that will validate a csv file against the Pydantic model.
4. The app should use a UI with a tool like tkinter to ask the user to upload its file.
5. The app should ask the user for the output file path and filename.
6. Before exporting the results, the app should nicely format the excel file using a tool like openpyxl.

# Notes

* The app should span across multiple files.
* We are using pydantic 2.11.3 so beware of the breaking changes. Do not use the old V1 syntax.
