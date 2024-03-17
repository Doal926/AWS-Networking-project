from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])  # Specify POST method for body data
def get_param():
    if request.method == "POST":
        # Get the request data as JSON
        data = request.get_json()

        # Check if request has data and if the parameter exists
        if data is None or "param_name" not in data:
            return jsonify({"error": "Missing parameter in request body"}), 400

        # Get the parameter value from the JSON data
        param_value = data["param_name"]

        # Process or return the parameter value
        return jsonify({"param": param_value})
    else:
        return "subnet 1.1"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1234, debug=True)
