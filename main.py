from flask import (
    Flask,
    request,
    jsonify
)
# import sklearn
from flask_cors import CORS
import pickle


app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return 'home'

# @app.route('/model', methods=['GET'])
# def load_model():
with open("dt.pkl","rb") as file:
    model=pickle.load(file)

@app.route('/model', methods=['POST'])
def predict():
    data = request.json['data']
    print(data)
    predictions = model.predict([data])[0]
    return jsonify(predictions.tolist())

if __name__=="__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)