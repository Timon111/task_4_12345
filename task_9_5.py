class Stationery:
    def __init__(self, title):
        self.title = title

    def drow(self):
        print("Запуск отрисовки")

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def drow(self):
        print("Запуск отрисовки: тонкая прямая синяя линия")

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def drow(self):
        print("Запуск отрисовки: тонкая прямая черная линия")

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def drow(self):
        print("Запуск отрисовки: толстая прямая черная линия")