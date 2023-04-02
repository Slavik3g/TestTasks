import json
from datetime import datetime
import pytz


def update_data(obj: dict) -> None:
    for key in obj:
        if isinstance(obj[key], dict):
            update_data(obj[key])
        elif isinstance(obj[key], list):
            for item in obj[key]:
                if isinstance(item, dict):
                    update_data(item)
                else:
                    break
        elif key == "updated":
            obj[key] = datetime.now(pytz.timezone('Europe/Minsk')).isoformat()


if __name__ == "__main__":
    filename = 'nums.json'
    with open(filename) as f:
        res = json.load(f)
    update_data(res)
    print(res)
    with open(filename, 'w') as f:
        json.dump(res, f)
