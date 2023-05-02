from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np

app = Flask(__name__)
CORS(app)


@app.route('/predict', methods=['POST'])
def predict():
    response_body = "Hello from Lambda" + str(1999)
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
    
    # response = {
    #     "isBase64Encoded": False,
    #     "statusCode": 200,
    #     "body": response_body,
    #     "headers": {
    #         "content-type": "application/json"
    #     }
    # }
    
    # Return the response object
    return year

if __name__=="__main__":
    app.run(debug=True)