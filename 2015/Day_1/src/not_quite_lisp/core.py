def main():
    from os import path
    input_code = get_input_code(path.abspath("assets/input.txt"))
    requested_floor, basement_pos = get_floor(input_code=input_code)
    print(f"First Quest: {requested_floor}\nSecond Quest: {basement_pos}")


def get_input_code(file: str):
    with open(file, "r") as f:
        characters = f.read()
    return characters


def get_floor(input_code: str = "(()()))))((((("):
    floor: int = 0
    numbers = {
        "count": 0,
        "pos": 0,
        "break": False,
    }
    input_as_list: list[str] = list(input_code)
    for c in input_as_list:
        numbers["count"] += 1
        floor += 1 if c == "(" else False
        floor -= 1 if c == ")" else False
        if floor == -1 and not numbers["break"]:
            numbers["pos"] = numbers["count"]
            numbers["break"] = True
    return floor, numbers["pos"]
