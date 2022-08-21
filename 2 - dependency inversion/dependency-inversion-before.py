class Bombilla:
    def turn_on(self):
        print("Bombilla: turned on...")

    def turn_off(self):
        print("Bombilla: turned off...")


class Interruptor:

    def __init__(self, l: Bombilla):
        self.Bombilla = l
        self.on = False

    def press(self):
        if self.on:
            self.Bombilla.turn_off()
            self.on = False
        else:
            self.Bombilla.turn_on()
            self.on = True


l = Bombilla()
switch = Interruptor(l)
switch.press()
switch.press()
