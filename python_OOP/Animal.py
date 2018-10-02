class Animal:

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def display_health(self):
        print(f'health:\t\t{self.health}')


class Dog(Animal):

    def __init__(self, name):
        super().__init__(name, None)
        self.health = 150

    def pet(self):
        self.health += 5
        return self


class Dragon(Animal):

    def __init__(self, name):
        super().__init__(name, None)
        self.health = 170

    def fly(self):
        self.health -= 10

    def display_health(self):
        super().display_health()
        print('I am a Dragon!')


anon = Animal('anon', 100)
anon.walk().walk().walk().run().run().display_health()

jessi = Dog('Jessi')
jessi.walk().walk().walk().run().run().pet().display_health()

poof = Dragon('Poof')
poof.display_health()
