from transport import Transport


class Container:
    __slots__ = ['_size', '_cont']

    # Container constructor.
    def __init__(self):
        self._size = 0
        self._cont = []

    # Pushes element to the end of container.
    def push_back(self, tr):
        self._size += 1
        self._cont.append(tr)

    # Generates a container.
    @staticmethod
    def generate(size):
        cont = Container()
        for i in range(size):
            cont.push_back(Transport.generate())
        return cont

    # Reads a Constructor from file.
    @staticmethod
    def read_from_file(size, file):
        cont = Container()
        for i in range(size):
            tr = Transport.read_from_file(file)
            if tr is None:
                return None
            else:
                cont.push_back(tr)
        return cont

    # Either reads a Constructor from file or generates it.
    @staticmethod
    def create(file):
        try:
            size = file.readline()
            size = int(size)
            assert size >= 0
            if size <= 20:
                return Container.read_from_file(size, file)
            else:
                return Container.generate(size)
        except:
            return None

    # Finds average distance Transport in Container can ride.
    def get_average_distance(self):
        distance_sum = 0
        for tr in self._cont:
            distance_sum += tr.get_max_distance()
        if self._size == 0:
            return 0
        else:
            return distance_sum / self._size

    # Removes from container all elements with max distance less than average.
    def remove_lesser_than_average(self):
        av_dist = self.get_average_distance()
        bad_transport = []
        for tr in self._cont:
            if tr.get_max_distance() < av_dist:
                bad_transport.append(tr)
        for tr in bad_transport:
            self._cont.remove(tr)
            self._size -= 1

    # Writes the Container to file.
    def write_to_file(self, file):
        file.write(f'There are {self._size} elements in container:\n')
        for tr in self._cont:
            tr.write_to_file(file)
            file.write('\n')
        file.write('\n')
