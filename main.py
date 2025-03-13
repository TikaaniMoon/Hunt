class Field:
    def __init__(self, tiger, rabbits):
        self.size = 5
        self.tiger = tiger
        self.rabbits = rabbits

    def display(self):
        matrix = []
        for _ in range(self.size):
            row = []
            for _ in range(self.size):
                row.append('*')
            matrix.append(row)

        for row in matrix:
            print(' '.join(row))

grid = Field('tiger', 'rabbits')
grid.display()

class Rabbit:
    def __init__(self, x, y):
        self.x = x # Координата x
        self.y = y # Координата y
        self.is_catched = False

    def to_catch(self): # Меняет атрибут класса is_catched на True или False
        self.is_catched = True

