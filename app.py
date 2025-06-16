from flask import Flask, request, jsonify
from flask_cors import CORS
import iPlan_Sotfwar_S


app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests


@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.json  # Receive JSON data
    print("Received Data:", data)  # Debugging output

    # Check the value of s_science_week and send data accordingly
    if data.get("s_science_week") == "1":
        response = iPlan_Sotfwar_S.process_data(data)
    
    else:
        response = {"error": "Invalid s_science_week value"}

    


    return jsonify(response), 200
@app.route("/")
def home():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
