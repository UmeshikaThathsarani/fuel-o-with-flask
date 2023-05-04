from flask import Flask, request
from flask_cors import CORS
import numpy as np
import tensorflow as tf
from tensorflow import keras
import joblib

app = Flask(__name__)
CORS(app)

# Load the trained model
model = keras.models.load_model('fuel_consumption_prediction_model.h5')

# Load the label encoding, one-hot encoding and scaling transformers
label_encoder_year = joblib.load('label_encoder_year.pkl')
label_encoder_make = joblib.load('label_encoder_make.pkl')
label_encoder_class = joblib.load('label_encoder_class.pkl')
label_encoder_drive = joblib.load('label_encoder_drive.pkl')
label_encoder_transmission = joblib.load('label_encoder_transmission.pkl')
label_encoder_fuel_type = joblib.load('label_encoder_fuelType.pkl')
onehot_encoder_year = joblib.load('onehot_encoder_Year.pkl')
onehot_encoder_make = joblib.load('onehot_encoder_Make.pkl')
onehot_encoder_class = joblib.load('onehot_encoder_Class.pkl')
onehot_encoder_drive = joblib.load('onehot_encoder_Drive.pkl')
onehot_encoder_transmission = joblib.load('onehot_encoder_Transmission.pkl')
onehot_encoder_turbocharger = joblib.load('onehot_encoder_Turbocharger.pkl')
onehot_encoder_supercharger = joblib.load('onehot_encoder_Supercharger.pkl')
onehot_encoder_fuel_type = joblib.load('onehot_encoder_Fuel Type.pkl')
scaler_engine_cylinders = joblib.load('scaler_Engine Cylinders.pkl')


@app.route('/predict', methods=['POST'])
def predict():
    
    json_data = request.json
    
    year = json_data['year']
    make = json_data['make']
    _class = json_data['_class']
    drive = json_data['drive']
    transmission = json_data['transmission']
    engine_cylinders = json_data['engineCylinders']
    turbocharger = json_data['turbocharger']
    supercharger = json_data['supercharger']
    fuel_type = json_data['fuelType']

    # Convert the input parameters to a numpy array
    input_data = np.array([[year, make, _class, drive, transmission, engine_cylinders, turbocharger, supercharger, fuel_type]])
    
    input_data_year = input_data[:, 0]
    input_data_make = input_data[:, 1]
    input_data_class = input_data[:, 2]
    input_data_drive = input_data[:, 3]
    input_data_transmission = input_data[:, 4]
    input_data_engine_cylinders = np.array([int(input_data[:, 5])])
    input_data_turbocharger = np.array([int(input_data[:, 6])])
    input_data_supercharger = np.array([int(input_data[:, 7])])
    input_data_fuel_type = input_data[:, 8]

    # Perform label encoding
    input_data_year = label_encoder_year.transform(input_data_year)
    input_data_make = label_encoder_make.transform(input_data_make)
    input_data_class = label_encoder_class.transform(input_data_class)
    input_data_drive = label_encoder_drive.transform(input_data_drive)
    input_data_transmission = label_encoder_transmission.transform(input_data_transmission)
    input_data_fuel_type = label_encoder_fuel_type.transform(input_data_fuel_type)

    # Perform one-hot encoding
    X_cat_year = onehot_encoder_year.transform([input_data_year])
    X_cat_make = onehot_encoder_make.transform([input_data_make])
    X_cat_class = onehot_encoder_class.transform([input_data_class])
    X_cat_drive = onehot_encoder_drive.transform([input_data_drive])
    X_cat_transmission = onehot_encoder_transmission.transform([input_data_transmission])
    X_cat_turbocharger = onehot_encoder_turbocharger.transform([input_data_turbocharger])
    X_cat_supercharger = onehot_encoder_supercharger.transform([input_data_supercharger])
    X_cat_fuel_type = onehot_encoder_fuel_type.transform([input_data_fuel_type])

    # Perform scaling
    input_data_engine_cylinders = scaler_engine_cylinders.transform([input_data_engine_cylinders])

    # Create a new numpy array
    encoded_input_data = np.concatenate((X_cat_year, X_cat_make, X_cat_class, X_cat_drive, X_cat_transmission, X_cat_turbocharger, X_cat_supercharger, X_cat_fuel_type, input_data_engine_cylinders), axis=1)

    # Predict the fuel consumption using the trained model
    predictions = model.predict(encoded_input_data)
    city_fuel_consumption, highway_fuel_consumption = predictions[0]

    response = "City Fuel Consumption:  "+str(city_fuel_consumption)+"  l/100km\nHighway Fuel Consumption:  "+str(highway_fuel_consumption)+"  l/100km"
    
    # Return the response object
    return response

if __name__=="__main__":
    app.run(debug=True)