import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
import pickle

load_dotenv()

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {f"origins": {os.environ.get("ADDRESS")}}})

sa_model = pickle.load(open("sentiment_analysis_model.sav", "rb"))

@app.route("/")
def hello():
    return "<h1>Hello world!</h1>"

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    prediction = sa_model.predict([data["text"]]) 

    analysis_result = {
        "text": data["text"],
        "sentiment": prediction[0]
    }

    return jsonify(analysis_result)


if __name__ == "__main__":
    debug_mode = False
    
    if os.environ.get("DEBUG").lower() == "true":
        debug_mode = True
    else:
        debug_mode = False

    app.run(host="0.0.0.0", port="8100", debug=debug_mode)
            
