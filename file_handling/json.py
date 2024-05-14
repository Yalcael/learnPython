import json


data: dict = {"name": "Vincent", "age": 23, "Job": None}

with open("new_data.json", "w") as file:
    json.dump(data, file)
    # json_format: str = json.dumps(data)
    # print(json_format)
