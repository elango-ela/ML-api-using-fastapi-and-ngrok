import json
import requests


url = 'https://48e5-35-201-253-251.ngrok-free.app/diabetes_prediction'


input_data_for_model = {
    
    'Pregnancies' : 6,
    'Glucose' : 100,
    'BloodPressure' : 72,
    'SkinThickness' : 45,
    'Insulin' : 0,
    'BMI' : 33.6,
    'DiabetesPedigreeFunction' : 0.627,
    'Age' : 0
    }

input_json = json.dumps(input_data_for_model)

response = requests.post(url, data=input_json)

print(response.text)
