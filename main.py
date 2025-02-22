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

