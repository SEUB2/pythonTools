# saveXls.py

import ezodf
import os

def read_ods(filename):
    path = os.path.join("..", "ods", filename)
    doc = ezodf.opendoc(path)
    sheet = doc.sheets[0]

    data = []
    for row in sheet.rows():
        current_row = [cell.value for cell in row]
        data.append(current_row)

    return data