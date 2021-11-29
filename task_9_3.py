
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.wage = wage
        self.bonus = bonus
        self._income = {"wage": self.wage, "bonus": bonus}
        self.name = name
        self.surname = surname
        self.position = position


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'name: {self.name} surname: {self.surname}'

    def get_total_income(self):
        return int(self.wage + self.bonus)