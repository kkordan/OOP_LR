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

class HeavyTank(Tank):
    def __init__(self, name):
        super().__init__(name, armor=25, damage=60, health=300)
        self.shield_active = False

    def activate_shield(self):
        if self.is_alive:
            self.shield_active = True
            self.armor *= 2
            print(f"{self.name} активировал щит! Броня удвоена!")

    def deactivate_shield(self):
        if self.shield_active:
            self.shield_active = False
            self.armor //= 2
            print(f"{self.name} деактивировал щит!")

class LightTank(Tank):
    def __init__(self, name):
        super().__init__(name, armor=10, damage=40, health=150)
        self.dodges_left = 3

    def dodge(self, damage):
        if self.dodges_left > 0 and self.is_alive:
            self.dodges_left -= 1
            print(f"{self.name} уклонился от атаки! Осталось уклонений: {self.dodges_left}")
            return True
        return False

    def take_damage(self, damage):
        if not self.dodge(damage):
            super().take_damage(damage)
