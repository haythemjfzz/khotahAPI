from flask import Flask, request, jsonify
from flask_cors import CORS
import iPlan_Sotfwar_S


app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests

@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.json  # Receive JSON data
    print("Received Data:", data)  # Debugging output

    # Check the value of currentDepartment and send data accordingly
    if data.get("currentDepartment") == "1":
        response = iPlan_Sotfwar_S.process_data(data)
    elif data.get("currentDepartment") == "2":
        response = iPlan_Sotfwar_M.process_data(data)
    elif data.get("currentDepartment") == "3":
        response = iPlan_Sotfwar_MTGM.process_data(data)
    elif data.get("currentDepartment") == "4":
        response = iPlan_Sotfwar_MTGE.process_data(data)
    elif data.get("currentDepartment") == "5":
        response = iPlan_Sotfwar_MTGC.process_data(data)
    elif data.get("currentDepartment") == "6":
        response = iPlan_Sotfwar_MTGP.process_data(data)
    elif data.get("currentDepartment") == "7":
        response = iPlan_Sotfwar_G.process_data(data)
    elif data.get("currentDepartment") == "8":
        response = iPlan_Sotfwar_L.process_data(data)
    elif data.get("currentDepartment") == "9":
        response = iPlan_Sotfwar_LES.process_data(data)
    elif data.get("currentDepartment") == "10":
        response = iPlan_Sotfwar_LEG.process_data(data)

    
    
    else:
        response = {"error": "Invalid currentDepartment value"}

    


    return jsonify(response), 200
@app.route("/")
def home():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
