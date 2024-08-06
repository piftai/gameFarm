import time

class Creep:
    def __init__(self, health, size, reward, damage, X, Y):
        self.health = health
        self.size = size
        self.reward = reward
        self.damage = damage
        self.X = X
        self.Y = Y

    def move(self):
        #  добавить рандом
        if time.time() % 2 == 0:
            self.X = self.X + 1 # тут рандом
        else:
            self.Y = self.Y + 2 # тут тоже

