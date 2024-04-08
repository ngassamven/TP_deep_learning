import sqlite3
import csv

# Connexion à la base de données
conn = sqlite3.connect('donnees_meteo.db')
cursor = conn.cursor()

# Création des tables si elles n'existent pas déjà
#cursor.execute('''CREATE TABLE IF NOT EXISTS donnees_originales (
                    #date TEXT,
                    #temperature_2m REAL
                #)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS donnees_transformees (
                    date TEXT,
                    temperature_2m REAL
                )''')

# Fonction pour insérer les données du CSV dans la base de données
def enregistrer_donnees(table_name, date, temperature_2m):
    cursor.execute(f'''INSERT INTO {table_name} (date, temperature_2m) VALUES (?, ?)''', (date, temperature_2m))
    conn.commit()

# Lecture des fichiers CSV et insertion des données dans la base de données
#with open('C:/TP/Data/donnees_meteo_originales.csv', 'r') as csv_file:
    #csv_reader = csv.DictReader(csv_file)
    #for row in csv_reader:
        #date = row['date']
        #temperature_2m = float(row['temperature_2m'])
        #enregistrer_donnees('donnees_originales', date, temperature_2m)

with open('C:/TP/Data/donnees_meteo_transformees.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        date = row['date']
        temperature_2m = float(row['temperature_2m'])
        enregistrer_donnees('donnees_transformees', date, temperature_2m)

print("Données enregistrées avec succès dans la base de données.")

# Fermeture de la connexion à la base de données
conn.close()
