from flask import Flask, render_template, request
import pickle

def model(cat , amt,city,pop,job):
 with open('pipe.pkl', 'rb') as file:
    fraud_model = pickle.load(file)
    val = fraud_model.predict([[cat , amt  ,city , pop , job]])
    return val

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

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction_result = None
    with open('pipe.pkl', 'rb') as file:
     fraud_model = pickle.load(file)

    if request.method == 'POST':
        # Handle form submission here
        category = request.form.get('category')
        amt = request.form.get('amt')
        state = request.form.get('state')
        city_pop = request.form.get('city_pop')
        job = request.form.get('job')

        prediction = model(category , float(amt) , state , int(city_pop) , job)

        # Update the prediction result
        prediction_result = 'Fraud' if prediction[0] == 1 else 'Not Fraud'

    return render_template('index.html', categories=categories, states=states, jobs=jobs, prediction_result=prediction_result)

if __name__ == '__main__':
    app.run(debug=True)

