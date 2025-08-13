from flask import Flask, request, jsonify
from flask_cors import CORS
import iPlan_Sotfwar_S
import iPlan_Sotfwar_G
import iPlan_Sotfwar_MTGP


app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests

@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.json  # Receive JSON data
    print("Received Data:", data)  # Debugging output

    # Check the value of s_science_week and send data accordingly
    if data.get("department") == "S":
        response = iPlan_Sotfwar_S.process_data(data)
    elif data.get("department") == "GESTION":
        response = iPlan_Sotfwar_G.process_data(data)
    elif data.get("department") == "P":
        response = iPlan_Sotfwar_MTGP.process_data(data)
    
    else:
        response = {"error": "Invalid s_science_week value"}

    


    return jsonify(response), 200
@app.route("/")
def home():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/ping')
def ping():
    return "pong", 200


