import json


def get_value(data_dict: dict, wanted_id: int) -> any:
    for key, value in data_dict.items():
        if key == "id" and value == wanted_id:
            return data_dict["value"]
        if type(value) is dict:
            result = get_value(value, wanted_id)
            if result is not None:
                return result
        if type(value) is list:
            for i in value:
                if type(i) is dict:
                    result = get_value(i, wanted_id)
                    if result is not None:
                        return result


if __name__ == "__main__":

    with open("data.json", encoding="UTF-8") as file:
        data = json.load(file)
        print(get_value(data, 1024))

