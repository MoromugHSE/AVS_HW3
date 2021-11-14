from transport import Transport
from random import randint, random


class Truck(Transport):
    __slots__ = ['_max_mass']

    # Truck constructor.
    def __init__(self, volume, fuel_100km, max_mass):
        super().__init__(volume, fuel_100km)
        if max_mass < 1 or max_mass > 1000:
            raise AttributeError("Wrong truck data")
        self._max_mass = max_mass

    # Reads a Truck from file.
    @staticmethod
    def read_from_file(file):
        try:
            volume, fuel_100km, max_mass = file.readline().split()
            volume = int(volume)
            fuel_100km = float(fuel_100km)
            max_mass = int(max_mass)
            return Truck(volume, fuel_100km, max_mass)
        except:
            return None

    # Generates a Truck.
    @staticmethod
    def generate():
        volume = randint(1, 200)
        fuel_100km = random() * 19 + 1
        max_mass = randint(1, 1000)
        return Truck(volume, fuel_100km, max_mass)

    # Writes the Truck to file.
    def write_to_file(self, file):
        super().write_to_file(file)
        file.write(f'This is a truck. The truck can take up to {self._max_mass} kg.')
