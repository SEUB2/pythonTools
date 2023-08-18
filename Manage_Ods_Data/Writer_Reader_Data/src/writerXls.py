# writerXls.py

import ezodf
import os

def create_ods(filename, data):
    path = os.path.join("..", "ods", filename)
    spreadsheet = ezodf.newdoc(doctype='ods', filename=path)
    sheet = ezodf.Table(name='Feuille1')
    spreadsheet.sheets += sheet

    for i, row in enumerate(data):
        for j, value in enumerate(row):
            sheet[i, j].set_value(value)

    spreadsheet.save()