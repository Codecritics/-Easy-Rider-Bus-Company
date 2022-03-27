from collections import defaultdict
from json import loads

standard_input = input()


def find_error(json_list: list[dict]) -> dict[int]:
    json_error = defaultdict(int)

    for element in json_list:
        bus_id, stop_id, stop_name, next_stop, stop_type, a_time = element["bus_id"], element["stop_id"], element[
            "stop_name"], element["next_stop"], element["stop_type"], element["a_time"]
        if type(bus_id) != int:
            json_error["bus_id"] += 1
        if type(stop_id) != int:
            json_error["stop_id"] += 1
        if type(stop_name) != str or (type(stop_name) == str and len(stop_name) == 0):
            json_error["stop_name"] += 1
        if type(element["next_stop"]) != int:
            json_error["next_stop"] += 1
        if type(stop_type) != str or (type(stop_type) == str and len(stop_type) > 1):
            json_error["stop_type"] += 1
        if type(a_time) != str or (type(a_time) == str and len(a_time) == 0):
            json_error["a_time"] += 1

    return json_error


def main():
    data = loads(standard_input, parse_float=float)
    errors = find_error(data)
    nb_errors = sum(errors.values())
    print(f"Type and required field validation: {nb_errors} errors")
    print(f"""\
bus_id: {errors['bus_id']}
stop_id: {errors['stop_id']}
stop_name: {errors['stop_name']}
next_stop: {errors['next_stop']}
stop_type: {errors['stop_type']}
a_time: {errors['a_time']}
    """)


if __name__ == '__main__':
    main()
