# main.py

import writerXls
import saveXls
from table import data

def main():
    # Écrire un fichier .ods
    writerXls.create_ods('data.ods', data)

    # Lire le fichier .ods
    read_data = saveXls.read_ods('data.ods')

    # Afficher les données
    for row in read_data:
        print('\t'.join(map(str, row)))

if __name__ == "__main__":
    main()