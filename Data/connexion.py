import pandas as pd
import sqlite3
from io import StringIO

def Connexion():
    # Connexion à la base de données
    con = sqlite3.connect('C:/TP/Data/donnees_meteo.db')
    
    # Lecture des données de la table 'donnees_originales'
    #data_originales = pd.read_sql('SELECT * FROM donnees_originales', con)
    
    # Lecture des données de la table 'donnees_transformees'
    data_transformees = pd.read_sql('SELECT * FROM donnees_transformees', con)
    
    # Fermeture de la connexion à la base de données
    con.close()
    
    # Convertir les DataFrames en chaînes CSV
    #csv_buffer_originales = StringIO()
    #data_originales.to_csv(csv_buffer_originales, index=False)
    
    csv_buffer_transformees = StringIO()
    data_transformees.to_csv(csv_buffer_transformees, index=False)
    
    # Réinitialiser la position du curseur dans les tampons
    #csv_buffer_originales.seek(0)
    csv_buffer_transformees.seek(0)
    
    return  csv_buffer_transformees
