import numpy as np
from flask import Flask, request, jsonify, render_template, url_for
import pickle

app = Flask(__name__)
model = None


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def predict():
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    # prediction = model.predict(final_features)
    prediction = [0.24]
    print(prediction[0])

    # output = round(prediction[0], 2)
    return render_template('home.html', prediction_text="AQI for East Lansingn {}".format(prediction[0]))


@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)


if __name__ == '__main__':
    app.run(debug=True)
