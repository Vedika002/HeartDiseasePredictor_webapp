import numpy as np
from flask import Flask,redirect,url_for, request, render_template
import pickle

app= Flask(__name__)

model= pickle.load(open('model.pkl','rb'))

@app.route('/')
def getstarted():
    return render_template("getstart.html")

@app.route('/home')
def home():
    return render_template('ind.html')

@app.route('/predict',methods=['POST'])
def predict():

    int_features = [float(x) for x in request.form.values()]
    features = np.array(int_features)
    reshaped=features.reshape(1,-1)
    prediction = model.predict(reshaped)
    if prediction == 0: 
        predicts=0
    else:
        predicts=1    
    # return render_template('result.html', prediction=predicts)
    return redirect(url_for('load', prediction=predicts))
    # return redirect(url_for('result', prediction=predicts))
@app.route('/load/<int:prediction>')
def load(prediction):
    return render_template('result.html',prediction=prediction)
@app.route('/display_result/<int:prediction>')
def display_result(prediction):
    return render_template('display_result.html', prediction=prediction)

if __name__ == "__main__":
    app.run()