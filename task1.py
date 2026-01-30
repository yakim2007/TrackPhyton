import json
def task() -> float:
    with open('input.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        composition = 0
        for item in data:
            composition += item['score'] * item['weight']
        return round(composition, 3)


print(task())
