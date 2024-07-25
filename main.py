from flask import Flask, render_template, request, jsonify
import pandas as pd
import pickle
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load datasets and trained model
data = pd.read_csv('Col.csv')
data1 = pd.read_csv('final_dataset.csv')

with open("home_prices_model.pkl", 'rb') as file:
    decision = pickle.load(file)

# Define features for prediction
X = data

# Define route for home page
@app.route('/')
def index():
    # Get unique values for dropdowns
    bedrooms = sorted(data1['beds'].unique())
    bathrooms = sorted(data1['baths'].unique())
    sizes = sorted(data1['size'].unique())
    zip_codes = sorted(data1['zip_code'].unique())

    # Render index.html template with dropdown options
    return render_template('index.html', bedrooms=bedrooms, bathrooms=bathrooms, sizes=sizes, zip_codes=zip_codes)

# Define route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Get form data and check for missing fields
    bedrooms_str = request.form.get('beds')
    bathrooms_str = request.form.get('baths')
    size_str = request.form.get('size')
    zipcode_str = request.form.get('zip_code')

    if not all([bedrooms_str, bathrooms_str, size_str, zipcode_str]):
        return jsonify({'error': 'Missing form fields'}), 400

    # Convert form data to float
    try:
        bedrooms = float(bedrooms_str)
        bathrooms = float(bathrooms_str)
        size = float(size_str)
        zipcode = float(zipcode_str)
    except ValueError:
        return jsonify({'error': 'Invalid form field values'}), 400

    # Find index of zipcode in X.columns
    loc_index = np.where(X.columns == str(zipcode))[0]
    print(zipcode, X.columns)
    if len(loc_index) > 0:
        loc_index = loc_index[0]
    else:
        # Handle case where zip_code is not found
        print("Zip code not found in data.")
        return jsonify({'error': 'Zip code not found'}), 400

    # Create input array for prediction
    x = np.zeros(len(X.columns))
    x[0] = size
    x[1] = bathrooms
    x[2] = bedrooms
    if loc_index >= 0:
        x[loc_index] = 1

    # Make prediction
    prediction = decision.predict([x])[0]

    # Return prediction as JSON
    return jsonify({'Price in USD': prediction})

# Run the app if this script is executed
if __name__ == "__main__":
    app.run(debug=True, port=5000)
