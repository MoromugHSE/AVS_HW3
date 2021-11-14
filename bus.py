from transport import Transport
from random import random, randint


class Bus(Transport):
    __slots__ = ['_max_passengers']

    # Bus constructor.
    def __init__(self, volume, fuel_100km, max_passengers):
        super().__init__(volume, fuel_100km)
        if max_passengers < 1 or max_passengers > 40:
            raise AttributeError("Wrong bus data")
        self._max_passengers = max_passengers

    # Reads a Bus from file.
    @staticmethod
    def read_from_file(file):
        try:
            volume, fuel_100km, max_passengers = file.readline().split()
            volume = int(volume)
            fuel_100km = float(fuel_100km)
            max_passengers = int(max_passengers)
            return Bus(volume, fuel_100km, max_passengers)
        except:
            return None

    # Generates a Bus.
    @staticmethod
    def generate():
        volume = randint(1, 200)
        fuel_100km = random() * 19 + 1
        max_passengers = randint(1, 40)
        return Bus(volume, fuel_100km, max_passengers)

    # Writes the Bus to file.
    def write_to_file(self, file):
        super().write_to_file(file)
        file.write(f'This is a bus. The bus can take up to {self._max_passengers} passengers.')
