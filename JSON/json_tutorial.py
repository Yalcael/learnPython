# JSON or JavaScript object notation is a way of describing data.
import json


def main():
    data = {
        "username": "Vincent",
        "active": True,
        "subscribers": 10,
        "order_total": 30.99,
        "order_ids": ["ABC123", "QQQ422", "LOL300"],
    }

    print(data)

    # Printing object as json string
    s = json.dumps(data)
    print(s)

    # Getting Python object from json string
    data2 = json.loads(s)
    assert data2 == data

    # Writing data to file
    with open("data.json", "w") as f:
        json.dump(data, f)

    # Reading data from file
    with open("data.json") as f:
        data3 = json.load(f)
    assert data3 == data


if __name__ == "__main__":
    main()

# We use dump or dumps to take a Python object and convert it to JSON
# We use load or loads to take a JSON thing and convert it into a Python object.
# You can use requests to easily get information from a website,
# With the request library, you can call request.get, put in the URL and that will do a get request to that URL.
# This URL will respond with JSON.
# The request library has a built-in called DOT JSON, which will automatically do what loads would do.
# JSON is human READABLE, and it's the facto standard for Web API.
