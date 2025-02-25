import json

def load_test_data():
    with open('config.json') as f:
        return json.load(f)
