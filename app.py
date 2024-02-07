from flask import Flask, request
import pickle
import re

app = Flask(__name__)

# Making an introduction endpoint
@app.route("/", methods = ['GET'])
def welcome():
    template = """
        Welcome to the API Version of my Model: How to navigate? (use Postman) --- try "/guide", or "/predict"
    """
    return template

# Making an guidance endpoint
@app.route("/guide", methods = ["GET"])
def guide():
    return {
        'Age': "Driver Age (above 21 years)",
        'Education_Level': "Numeric (value upto 12th), & word (above 12th)",
        'Income': "Enter montly income of driver", 
        'Joining Designation': "1 to 5", 
        'Grade': "1 to 5",
        'Quarterly Rating': "1 to 4", 
        'Firstreport_leadtime' : "-100 to 300", 
        'service_days': '1 to 700'
    }

#Loading the model:
with open('model.pkl','rb') as handle:
    model = pickle.load(handle)

# Making an Prediction endpoint
@app.route("/predict", methods = ['POST','GET'])
def predict():
    inputs = request.get_json()

    age = int(inputs['Age'])

    ed_text = inputs['Education_Level']
    ed = re.findall('\d+', ed_text)
    if len(ed) == 0:
        education = 2
    else: 
        education = int(ed[-1])

    income = int(inputs['Income'])

    designation = int(inputs['Joining Designation'])

    grade = int(inputs['Grade'])

    qrate = int(inputs['Quarterly Rating'])

    lead = int(inputs['Firstreport_leadtime'])

    service = int(inputs['service_days'])

    x_q = [[age, education, income, designation, grade, qrate, lead, service]]

    pred = model.predict(x_q)

    if pred == 1:
        return "CHURN"
    else:
        return "NOT-CHURN"





