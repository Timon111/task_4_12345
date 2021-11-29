
class Road:
    asf_mass = 25 #кг
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width

    def formule(self, height):
        return f"{self._width} м*{self._lenght} м*{Road.asf_mass} кг*{height} см = {self._width * self._lenght * Road.asf_mass * height} т"