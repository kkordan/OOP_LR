class Tank:
    def __init__(self, name, armor, damage, health):
        self.name = name
        self.armor = armor
        self.damage = damage
        self.health = health
        self.is_alive = True

    def take_damage(self, damage):
        real_damage = damage - self.armor
        if real_damage > 0:
            self.health -= real_damage
            if self.health <= 0:
                self.health = 0
                self.is_alive = False
                print(f"{self.name} уничтожен!")
            else:
                print(f"{self.name} получил {real_damage} урона. Осталось {self.health} HP")
        else:
            print(f"Броня {self.name} полностью поглотила урон!")

    def shoot(self, target):
        if self.is_alive:
            print(f"{self.name} стреляет в {target.name}!")
            target.take_damage(self.damage)
        else:
            print(f"{self.name} уничтожен и не может стрелять!")
