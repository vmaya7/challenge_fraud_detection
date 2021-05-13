import requests
url = 'http://127.0.0.1:5000/predict'

test = {'genero': 'F',
 'monto': 608.3456335342977,
 'hora': 20,
 'establecimiento': 'Super',
 'ciudad': 'Merida',
 'tipo_tc': 'Física',
 'linea_tc': 71000,
 'interes_tc': 51,
 'status_txn': 'Aceptada',
 'is_prime': 0,
 'dcto': 60.834563353429786,
 'cashback': 5.4751107018086795,
 'device_score': 3,
 'os': 'ANDROID',
 'dia': 1}

response = requests.post(url, data = test)
print(response)
print(response.json())
response.json()