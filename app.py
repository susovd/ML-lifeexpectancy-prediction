import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods = ['POST'])
def predict():
    '''
    for rendering results on html GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = prediction[0]
    return render_template('index.html', prediction_text = "The estimated life expectancy is {}".format(output))


@app.route("/visualisations")
def visualisations():
    return render_template("visualisations.html")

@app.route("/about")
def about():
    return render_template("about.html")



if __name__ == '__main__':
    app.debug = True
    app.run()
