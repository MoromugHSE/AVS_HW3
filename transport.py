from random import randint


class Transport:
    __slots__ = ['_key', '_volume', '_fuel_100km']

    # Transport constructor.
    def __init__(self, volume, fuel_100km):
        if (volume < 1 or volume > 200) or (fuel_100km < 1 or fuel_100km > 20):
            raise AttributeError('Wrong transport data')
        self._volume = volume
        self._fuel_100km = fuel_100km

    # Reads a Transport from file.
    @staticmethod
    def read_from_file(file):
        key = file.readline()
        try:
            key = int(key)
        except ValueError:
            key = 0
        if key == 1:
            from truck import Truck
            return Truck.read_from_file(file)
        elif key == 2:
            from bus import Bus
            return Bus.read_from_file(file)
        elif key == 3:
            from car import Car
            return Car.read_from_file(file)
        else:
            return None

    # Returns max distance a transport can ride.
    def get_max_distance(self):
        return self._volume / self._fuel_100km * 100

    # Generates a Transport.
    @staticmethod
    def generate():
        key = randint(1, 3)
        if key == 1:
            from truck import Truck
            return Truck.generate()
        elif key == 2:
            from bus import Bus
            return Bus.generate()
        elif key == 3:
            from car import Car
            return Car.generate()

    # Writes the Transport to file.
    def write_to_file(self, file):
        file.write(f"This transport has a volume of {self._volume} and needs "
                   f"{self._fuel_100km} fuel for 100 km. ")
