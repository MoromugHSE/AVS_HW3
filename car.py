from transport import Transport
from random import random, randint


class Car(Transport):
    __slots__ = ['_max_speed']

    # Car constructor.
    def __init__(self, volume, fuel_100km, max_speed):
        super().__init__(volume, fuel_100km)
        self._max_speed = max_speed

    # Reads a Car from file.
    @staticmethod
    def read_from_file(file):
        try:
            volume, fuel_100km, max_speed = file.readline().split()
            volume = int(volume)
            fuel_100km = float(fuel_100km)
            max_speed = int(max_speed)
            return Car(volume, fuel_100km, max_speed)
        except:
            return None

    # Generates a Car.
    @staticmethod
    def generate():
        volume = randint(1, 200)
        fuel_100km = random() * 19 + 1
        max_speed = randint(1, 100)
        return Car(volume, fuel_100km, max_speed)

    # Writes the Car to file.
    def write_to_file(self, file):
        super().write_to_file(file)
        file.write(f'This is a car. The car can speed up to {self._max_speed} km/h.')
