class car:
    def __init__(self, make, model):
        self.__make = make
        self.__year_model = model
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__year_model

    def get_speed(self):
        return self.__speed


def main():
    cars = car("Lamborghini", "2015 Egoista")

    for i in range(0,5):
        cars.accelerate()
        print("Your speed is", cars.get_speed(),"mph.")

    for i in range(0, 5):
        cars.brake()
        print("Your speed is", cars.get_speed(), "mph.")

main()