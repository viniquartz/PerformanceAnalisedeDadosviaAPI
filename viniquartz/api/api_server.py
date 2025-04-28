import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, jsonify # type: ignore
import modules.load_data
import modules.data_analysis

import time
from datetime import datetime

app = Flask(__name__)

# Data load
data = modules.load_data.get_data()
data_analysis = modules.data_analysis.DataAnalysis(data)

@app.route('/users', methods=['GET'])
def get_user():
    return jsonify(data)

@app.route('/users/<property_name>', methods=['GET'])
def get_users_property(property_name):
    properties = data_analysis.get_property_for_all_data(property_name)
    return jsonify(properties)

@app.route('/user/<user_id>', methods=['GET'])
def get_user_id(user_id):
    user = data_analysis.get_user_by_id(user_id)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404
    
@app.route("/superusers", methods=["GET"])
def get_superusers():
    start_time = time.time()
    superusers = data_analysis.get_superuser_list()
    superusers_names = [user.get("nome") for user in superusers]
    end_time = time.time()
    execution_time_ms = int((end_time - start_time) * 1000)

    response = {
        "timestamp": datetime.now().isoformat() + "Z",
        "execution_time_ms": execution_time_ms,
        "data": superusers_names
    }
    return jsonify(response)

@app.route("/top-countries", methods=["GET"])
def get_top_countries():
    start_time = time.time()
    top_countries = data_analysis.get_top_countries()
    end_time = time.time()
    execution_time_ms = int((end_time - start_time) * 1000)

    response = {
        "timestamp": datetime.now().isoformat() + "Z",
        "execution_time_ms": execution_time_ms,
        "data": top_countries
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
