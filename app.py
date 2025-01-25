from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load('iris_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from request
    data = request.get_json(force=True)

    # Convert data into dataframe
    data_df = pd.DataFrame([data])

    # Make prediction
    prediction = model.predict(data_df)

    # Convert prediction to a meaningful label
    species = ['setosa', 'versicolor', 'virginica']
    predicted_species = species[prediction[0]]

    # Return prediction
    return jsonify({'prediction': predicted_species})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)