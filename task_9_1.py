from itertools import cycle
from time import sleep

class TrafficLight:
    def __init__(self, color):
        self._color = color

    def state(self):
        return self._color

    def running(self):
        try:
            cyclic = cycle(["red", "yellow", "green"])
            while self._color != next(cyclic):
                next(cyclic)
            while True:
                self._color = next(cyclic)
                if self._color == "red":
                    sleep(7)
                elif self._color == "yellow":
                    sleep(2)
                if self._color == "green":
                    sleep(7)
        except KeyboardInterrupt:
            print("KeyboardInterrupt")

    def next_color(self, next_color):
        if 0 < next_color:
            cyclic = ("red", "yellow","green")
            self._color = cyclic[int(next_color) % 2]
            self.state()
        else:
            print("InvalidValueError")
