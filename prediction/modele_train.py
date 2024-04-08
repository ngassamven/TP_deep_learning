
import preprocess
import connectiondb


############################################ Modèle ARIMA #######################################################################

from statsmodels.tsa.arima.model import ARIMA

def Model_ARIMA(ts_train):
    order=(6,1,10)
    model = ARIMA(ts_train, order=order).fit()
    return model


########################################## Modele SARIMA #######################################################################

from statsmodels.tsa.arima.model import ARIMA

def Model_ARIMA(ts_train):
    order=(6,2,4)
    model = ARIMA(ts_train, order=order).fit()
    return model



######################################### Modele SARIMAX ###########################################################################




###################################### Modele de Regression Lineaire ################################################################
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

def Model_RegressionLineaire(X_train,y_train,X_test,y_test):
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print(f"Linear regression\n R^2={r2_score(y_test, y_pred):.2f}")
    return model



################################ persitance des models ##################################################

import os
import joblib

def sauvegarder_modele(modele, chemin_dossier, nom_fichier):
    
    # Créer le dossier s'il n'existe pas
    if not os.path.exists(chemin_dossier):
        os.makedirs(chemin_dossier)

    # Chemin complet du fichier de sauvegarde
    chemin_complet = os.path.join(chemin_dossier, nom_fichier)

    # Sauvegarde du modèle
    joblib.dump(modele, chemin_complet)

    return chemin_complet


############################### TRAIN ###############################################################


donne = connectiondb.Connexion()
data1, ts_train, ts_test = preprocess.preprocessing(donne)
X_train, X_test, y_train, y_test = preprocess.preprocessingML(data1)

directory = './Modeles'

Model_ARIMA=Model_ARIMA(ts_train)
sauvegarder_modele(Model_ARIMA, directory, 'model_arima')

Model_ARIMA=Model_SARIMA(ts_train)
sauvegarder_modele(Model_SARIMA, directory, 'model_sarima')

Model_RegressionLineaire=Model_RegressionLineaire(X_train,y_train,X_test,y_test)
sauvegarder_modele(Model_RegressionLineaire, directory, 'model_regression')
