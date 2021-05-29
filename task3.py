class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        return f'Размер клетки: {self.quantity + other.quantity}'

    def __sub__(self, other):
        sub_minus = self.quantity - other.quantity
        return f'Уменьшение, теперь: {sub_minus} клеток' if sub_minus > 0 else 'Клетки отсутствуют'

    def __mul__(self, other):
        sub_multiplication = self.quantity * other.quantity
        return f'Клетки умножились до: {sub_multiplication} клеток'

    def __truediv__(self, other):
        sub_division = self.quantity // other.quantity
        return f'Клетки поделились на: {sub_division} полноценные клетки'

    def make_order(self, row):
        result = ''
        for i in range(int(self.quantity / row)):
            result += '*' * row + '\n'
        result += '*' * (self.quantity % row) + '\n'
        return result


cell = Cell(24)
cell_2 = Cell(5)
print(cell + cell_2)
print(cell - cell_2)
print(cell / cell_2)
print(cell * cell_2)
print(cell.make_order(10))
