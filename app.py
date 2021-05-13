from flask import Flask
import redis
import time
import pandas as pd
from settings import columnas_f, list_categoricas
from joblib import dump, load
from flask_restful import Api, Resource, reqparse
import json
import numpy as np

#Inicializando Flask application

app = Flask(__name__)
API_app = Api(app)

model = load('logistic_regressor.joblib')
scaler = load('scaler.joblib')
columnas = ['genero', 'monto', 'hora', 'establecimiento', 'ciudad',
       'tipo_tc', 'linea_tc', 'interes_tc', 'status_txn', 'is_prime', 'dcto',
       'cashback', 'device_score', 'os', 'dia', 'fecha']

X_solve = pd.DataFrame(np.zeros((1, len(columnas_f))), columns = columnas_f)

@app.route("/")
def homepage():
	return "Bienvenido a la API de detección de fraude"

class Predict(Resource):

    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument('genero')
        parser.add_argument('monto')
        parser.add_argument('hora')
        parser.add_argument('establecimiento')
        parser.add_argument('ciudad')
        parser.add_argument('tipo_tc')
        parser.add_argument('linea_tc')
        parser.add_argument('interes_tc')
        parser.add_argument('status_txn')
        parser.add_argument('is_prime')
        parser.add_argument('dcto')
        parser.add_argument('cashback')
        parser.add_argument('device_score')
        parser.add_argument('os')
        parser.add_argument('dia')
        args = parser.parse_args()

        #X_solve = pd.DataFrame(args.values(), columns = columnas)

        X = args


        for key, value in X.items():
            if key in list_categoricas:
                key_m = key + '_' + value
                X_solve.loc[0, key_m] = 1
            else:
                X_solve.loc[0, key] = value


        df_solve = scaler.transform(X_solve.values)

        predicciones = model.predict(df_solve)
        print(predicciones)
        out = {'Prediction': str(predicciones[0])}

        return out, 200

API_app.add_resource(Predict, '/predict')

if __name__ == '__main__':
    app.run(debug=False )




