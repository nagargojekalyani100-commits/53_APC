class Camera:
    def take_photo(self):
        print("Taking a photograph.")


class Phone:
    def make_call(self, number):
        print("Calling", number)


class Smartphone(Camera, Phone):
    def display(self):
        print("Smartphone supports both camera and phone operations.")


# Create object
s1 = Smartphone()

s1.display()
s1.take_photo()
s1.make_call("9876543210")