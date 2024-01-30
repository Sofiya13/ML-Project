from flask import Flask, render_template, request

app = Flask(__name__)

# Sample data for dropdowns
categories = ['grocery_pos', 'entertainment', 'shopping_pos', 'misc_pos',
              'shopping_net', 'gas_transport', 'misc_net', 'grocery_net',
              'food_dining', 'health_fitness', 'kids_pets', 'home',
              'personal_care', 'travel']

states = ['WA', 'ID', 'CA', 'NM', 'WY', 'HI', 'NE', 'OR', 'UT', 'AZ', 'CO',
          'MO', 'AK']

jobs = ['Contractor', 'Designer', 'exhibition/display', 'Electronics engineer',
        'Geoscientist', 'Health physicist', 'Insurance broker', 'Land/geomatics surveyor',
        'Petroleum engineer', 'Research officer, political party',
        'Special educational needs teacher', 'Surveyor, land/geomatics',
        'Surveyor, minerals', 'Systems analyst', 'Tax inspector',
        'Water engineer', 'other']

def preprocess_input(category, amt, state, city_pop, job):
    # Add your preprocessing logic here
    # This is a simple example, adjust it based on your needs
    processed_input = [category, float(amt), state, int(city_pop), job]
    return processed_input

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction_result = None

    if request.method == 'POST':
        # Handle form submission here
        category = request.form.get('category')
        amt = request.form.get('amt')
        state = request.form.get('state')
        city_pop = request.form.get('city_pop')
        job = request.form.get('job')

        # Use preprocess_input to prepare the input for the model
        processed_input = preprocess_input(category, amt, state, city_pop, job)

        # Assuming you have a model loaded elsewhere in your code
        # Replace this line with the actual prediction logic
        #prediction = fraud_model.predict(processed_input)

        # Placeholder for demonstration purposes
        prediction = [0]

        # Update the prediction result
        prediction_result = 'Fraud' if prediction[0] == 1 else 'Not Fraud'

    return render_template('index.html', categories=categories, states=states, jobs=jobs, prediction_result=prediction_result)

if __name__ == '__main__':
    app.run(debug=True)

