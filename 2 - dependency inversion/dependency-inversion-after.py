from abc import ABC, abstractmethod


class Suichable(ABC):
    @abstractmethod
    def prender(self):
        pass

    @abstractmethod
    def apagar(self):
        pass


class Bombilla(Suichable):
    def prender(self):
        print("Bombilla: turned on...")

    def apagar(self):
        print("Bombilla: turned off...")


class Ventilador(Suichable):
    def prender(self):
        print("Ventilador: turned on...")

    def apagar(self):
        print("Ventilador: turned off...")


class Switche:

    def __init__(self, c: Suichable):
        self.client = c
        self.on = False

    def press(self):
        if self.on:
            self.client.apagar()
            self.on = False
        else:
            self.client.prender()
            self.on = True


l = Bombilla()
f = Ventilador()
switch = Switche(f)
switch.press()
switch.press()
