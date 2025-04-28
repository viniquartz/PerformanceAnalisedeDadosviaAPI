import json

# function used to get data in json and save in memory
def get_data():
    db_load = ""
    # dictionary list
    with open("usuarios_1000.json") as json_file:
        db_load = json.load(json_file)
    return db_load
