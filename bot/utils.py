import json

from langchain.schema import messages_from_dict


def save_as_json(file_name, file_data):
    output_file_path = "../data/" + file_name + ".json"
    with open(output_file_path, "w") as json_file:
        json.dump(file_data, json_file, indent=4)

    return


def load_json(path):
    try:
        with open(path, 'r') as json_file:
            # data = json.loads(json_file.read())
            data = json.load(json_file)

        return messages_from_dict(data)
    except:
        return messages_from_dict([])
