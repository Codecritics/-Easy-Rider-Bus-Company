import re
from json import loads


class Bus:
    errors = {
        "bus_id": 0,
        "stop_id": 0,
        "stop_name": 0,
        "next_stop": 0,
        "stop_type": 0,
        "a_time": 0
    }

    def __init__(self, bus_id, stop_id, stop_name, next_stop, stop_type, a_time):
        self.bus_id, self.stop_id, self.stop_name, self.next_stop, self.stop_type, self.a_time \
            = None, None, None, None, None, None
        self.set_bus_id(bus_id)
        self.set_stop_id(stop_id)
        self.set_stop_name(stop_name)
        self.set_next_stop(next_stop)
        self.set_stop_type(stop_type)
        self.set_a_time(a_time)

    def set_bus_id(self, bus_id):
        try:
            assert isinstance(bus_id, int)
        except AssertionError:
            self.errors['bus_id'] += 1
        else:
            self.bus_id = bus_id

    def set_stop_id(self, stop_id):
        try:
            assert isinstance(stop_id, int)
        except AssertionError:
            self.errors['stop_id'] += 1
        else:
            self.stop_id = stop_id

    def set_stop_name(self, stop_name):
        template = r'[A-Z][a-z]+\s+(Road|Avenue|Boulevard|Street)$'

        try:

            assert isinstance(stop_name, str) and bool(re.search(template, stop_name))
        except AssertionError as m:
            self.errors['stop_name'] += 1
        else:
            self.stop_name = stop_name

    def set_next_stop(self, next_stop):
        try:
            assert isinstance(next_stop, int)
        except AssertionError:
            self.errors['next_stop'] += 1
        else:
            self.next_stop = next_stop

    def set_stop_type(self, stop_type):
        template = '[SOF]?$'
        try:
            assert isinstance(stop_type, str) and bool(re.match(template, stop_type))
        except AssertionError:
            self.errors['stop_type'] += 1
        else:
            self.stop_type = stop_type

    def set_a_time(self, a_time):
        template = r'([0-1][0-9]|[2[0-4]):[0-5]?[0-9]$'
        try:
            assert isinstance(a_time, str) and bool(re.match(template, a_time))
        except AssertionError:
            self.errors['a_time'] += 1
        else:
            self.a_time = a_time

    def __str__(self):
        nb_errors = sum(self.errors.values())
        string = f"Type and required field validation: {nb_errors} errors\n"
        string += f"stop_name: {self.errors['stop_name']}\n"
        string += f"stop_type: {self.errors['stop_type']}\n"
        string += f"a_time: {self.errors['a_time']}\n"

        return string


standard_input = input()


def main():
    data = loads(standard_input, parse_float=float)
    buses = []
    for element in data:
        bus_id, stop_id, stop_name, next_stop, stop_type, a_time = element["bus_id"], element["stop_id"], element[
            "stop_name"], element["next_stop"], element["stop_type"], element["a_time"]
        buses.append(Bus(bus_id, stop_id, stop_name, next_stop, stop_type, a_time))

    print(buses[0])


if __name__ == '__main__':
    main()
