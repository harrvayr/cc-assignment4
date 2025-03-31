from flask import Flask, jsonify, request
import pickle

app = Flask(__name__)

sa_model = pickle.load(open("sentiment_analysis_model.sav", "rb"))

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
    app.run(host="0.0.0.0", port="8100", debug=False)
