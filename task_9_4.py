class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        if self.speed > 0:
            print("машина поехала")

    def stop(self):
        if self.speed == 0:
            print("машина остановилась")

    def turn(self, direction): #left right back straight
        if direction == "left":
            print("Машина повернула налево")
        elif direction == "right":
            print("Машина повернула вправо")
        elif direction == "back":
            print("Машина повернула назад")
        elif direction == "straight":
            print("Машина не изменила направления")

    def show_speed(self):
        return self.speed

class TownCar(Car):
    limit = 60

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police == False)

    def show_speed(self):
        if self.speed > self.limit:
            print("Превышение скорости")
        else:
            return self.speed

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police == False)

class WorkCar(Car):
    limit = 40

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > self.limit:
            print("Превышение скорости")
        else:
            return self.speed

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, True)
