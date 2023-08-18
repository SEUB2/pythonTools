import ezodf

def create_spreadsheet():
    # Créer un nouveau document spreadsheet
    spreadsheet = ezodf.newdoc(doctype='ods', filename='mon_tableau.ods')
    
    # Ajouter une nouvelle feuille de calcul
    sheet = ezodf.Table(name='Feuille1')
    spreadsheet.sheets += sheet
    
    # Ajouter des données à la feuille de calcul
    sheet['A1'].set_value('Bonjour')
    sheet['A2'].set_value('Monde')
    
    # Enregistrer le document
    spreadsheet.save()

def read_and_display():
    # Ouvrir le document
    doc = ezodf.opendoc('mon_tableau.ods')
    sheet = doc.sheets[0]
    
    # Afficher les données
    for row in sheet.rows():
        for cell in row:
            print(cell.value, end='\t')
        print()  # pour un retour à la ligne après chaque ligne du tableau

if __name__ == "__main__":
    create_spreadsheet()
    read_and_display()