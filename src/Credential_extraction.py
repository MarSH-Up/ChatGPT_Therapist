import json
# Open the JSON file and load its contents


def ApiKey():
    data = []
    with open('api_data.json') as json_file:
        data = json.load(json_file)

    return data['API KEY']
