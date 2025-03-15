import random
import time

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

        matrix[self.tiger.x][self.tiger.y] = 'T'

        for rabbit in self.rabbits:
            if not rabbit.is_catched:
                matrix[rabbit.x][rabbit.y] = 'З'

        for row in matrix:
            print(' '.join(row))

class Rabbit:
    def __init__(self, x, y):
        self.x = x # Координата x
        self.y = y # Координата y
        self.is_catched = False

    def to_catch(self): # Меняет атрибут класса is_catched на True или False
        self.is_catched = True

class Tiger:
    def __init__(self, rabbits):
        self.x = 0
        self.y = 0
        self.state = 'hunting'
        self.lucky_jump = 0.5
        self.rabbits = rabbits

    def randomly_move(self):

        self.x += random.choice([-1, 1])

        if self.x < 0:
            self.x = 0
        elif self.x > 4:
            self.x = 0

        self.y += random.choice([-1, 1])

        if self.y < 0:
            self.y = 0
        elif self.y > 4:
            self.y = 0

    def check_nearby_rabbit(self, rabbit):   # Проверка, что кролик рядом
        return abs(self.x - rabbit.x) <= 1 and abs(self.y - rabbit.y) <= 1

    def update_state(self):
        if self.state == 'hunting':
            print('Тигр охотится')
            self.randomly_move()

            if any(self.check_nearby_rabbit(rabbit) for rabbit in self.rabbits):
                self.state = 'attack'
                print('Тигр атакует')

        elif self.state == 'attack':
            current_lucky = random.random()
            if current_lucky < self.lucky_jump:
                print('Заяц не пойман')
                self.state = 'return_home'
            else:
                for rabbit in self.rabbits:
                    if self.check_nearby_rabbit(rabbit):
                        rabbit.to_catch()
                        print(f'Заяц на клетке({rabbit.x}, {rabbit.y}) пойман!')
                        self.state = 'return_home'

        elif self.state == 'return_home':
            self.x, self.y = 0, 0

class Game:
    def __init__(self):

        self.rabbit1 = Rabbit(random.randint(1, 4), random.randint(1, 4))
        self.rabbit2 = Rabbit(random.randint(1, 4), random.randint(1, 4))

        self.rabbits = [self.rabbit1, self.rabbit2]

        self.Shiaron = Tiger(self.rabbits)

        self.field = Field(self.Shiaron, self.rabbits)

        while self.Shiaron.state != 'return_home':
            self.field.display()
            self.Shiaron.update_state()
            time.sleep(1)

            if self.Shiaron.state == 'return_home':
                break

hunt = Game()