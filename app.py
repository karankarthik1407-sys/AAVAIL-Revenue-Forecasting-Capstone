from flask import Flask, request, jsonify
from src.predict import predict_one

app = Flask(__name__)


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.post("/predict")
def predict():
    payload = request.get_json(force=True)
    country = payload.get("country")
    date = payload.get("date")

    if not country or not date:
        return jsonify(error="country and date required"), 400

    return jsonify(predict_one(country, date))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
