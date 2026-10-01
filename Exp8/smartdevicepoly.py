class SmartDevice:
    def turn_on(self):
        print("Smart device is turned ON")

    def turn_off(self):
        print("Smart device is turned OFF")


class Light(SmartDevice):
    def turn_on(self):
        print("Light is turned ON")

    def turn_off(self):
        print("Light is turned OFF")


class Fan(SmartDevice):
    def turn_on(self):
        print("Fan is turned ON")

    def turn_off(self):
        print("Fan is turned OFF")


class AC(SmartDevice):
    def turn_on(self):
        print("AC is turned ON")

    def turn_off(self):
        print("AC is turned OFF")


class TV(SmartDevice):
    def turn_on(self):
        print("TV is turned ON")

    def turn_off(self):
        print("TV is turned OFF")



light = Light()
fan = Fan()
ac = AC()
tv = TV()


devices = [light, fan, ac, tv]

for device in devices:
    device.turn_on()
    device.turn_off()