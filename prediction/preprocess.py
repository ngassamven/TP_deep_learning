# Décomposition saisonnière de la série temporelle
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt
import statsmodels.tsa.stattools as stattools
import warnings
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_absolute_percentage_error
import numpy as np

# Votre fonction de prétraitement
def preprocessing(dataset):
    data = pd.read_csv(dataset, index_col=None)
    # Convertir la colonne de dates en type datetime
    #data['date'] = pd.to_datetime(data['date'])
    # Supprimer la partie "+00:00" du format de date
    #data['date'] = data['date'].dt.strftime('%Y-%m-%d %H:%M')
    #data['date'] = pd.to_datetime(data['date'])
    # Définir la colonne 'date' comme index
    #data.set_index('date', inplace=True)

    # Calculer la moyenne des valeurs à chaque intervalle de 3 heures
    #data1 = data.resample('3H').mean()
    # Split data into train (80%) and test (20%) sets
    ind_split = int(len(data) * 0.8)

    ts_train = data[:ind_split]
    ts_test = data[ind_split:]
    return data, ts_train, ts_test 

# Votre fonction de prétraitement ML
def preprocessingML(data):
    for i in range(1, 8):
        data[f"lag_{i}"] = data[value_column].shift(i)
    data.dropna(inplace=True)
    from sklearn.model_selection import train_test_split
    X = data.drop(value_column, axis=1)
    y = data[value_column]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, shuffle=False)
    
    return X_train, X_test, y_train, y_test

# Utilisez vos fonctions pour prétraiter vos données
data1, ts_train, ts_test = preprocessing('donnees_meteo_transformees.csv')
X_train, X_test, y_train, y_test = preprocessingML(data)

# Continuez avec le reste de votre code...
