import json


def save_data(topic, content):

    data = {
        "topic": topic,
        "content": content
    }

    with open("dataset.json", "a") as f:
        json.dump(data, f)
        f.write("\n")