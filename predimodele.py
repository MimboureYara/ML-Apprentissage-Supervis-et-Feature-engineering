# Importation des librairies
import numpy as np
import pandas as pd
import random as rd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
pd.options.mode.chained_assignment = None  # default='warn'
from ipykernel import kernelapp as app
import os
from sklearn import linear_model
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.svm import SVC
#importation de la librairie de calcul

def mod_prediction(modele):
    data = pd.read_csv("/content/ccdefault.csv")
    
    # Variable à modéliser
    y = data["DEFAULT"]

    # variables explicatives
    x = data.drop("DEFAULT", axis = 1)
    x = x.drop("ID", axis = 1)

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test  = train_test_split(x, 
                                                        y, 
                                                        test_size=0.25, 
                                                        random_state=42)
    svc = SVC(random_state=42)
    svc.fit(x_train, y_train)


    from sklearn.linear_model import LogisticRegression
    logit = LogisticRegression()
    titan_logit=logit.fit(x, y)
    # Erreur sur l'écahntillon test
    1-titan_logit.score(x_test, y_test)

    #importation de l'outil 
    from statsmodels.tools import add_constant 
    import statsmodels as sm
    #données X avec la constante 
    XTrainBis = sm.tools.add_constant(x_train) 
    
    #vérifier la structure 
    print(XTrainBis.info()) 

    #visualisation des premières lignes de la structure 
    #premières lignes 
    print(XTrainBis.head()) 


    #importation de la classe de calcul 
    from statsmodels.api import Logit 
    
    #régression logistique - on passe la cible et les explicatives 
    lr = Logit(endog=y_train,exog=XTrainBis) 
    
    #lancer les calculs 
    #algorithme de Newton-Raphson utilisé par défaut 
    #https://www.statsmodels.org/stable/generated/statsmodels.discrete.discrete_model.Logit.fit.html 
    res = lr.fit() 

    # Coefficients
    #résumé des résultats 
    print(res.summary()) 

    return mod_prediction(x_test)

mod_prediction(modele)

