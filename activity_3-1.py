class Car:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

    def start(self):
        print('Vroom!')

    def talk(self, driver):
        print(f'Hello, {driver}, I am {self.name}.')

# my_car = Car('Kitt', 180)
# my_other_car = Car('Speedy', 55)

# my_car.talk('Michael')


class Race:
    def __init__(self, name, driver_limit):
        self.name = name
        self.driver_limit = driver_limit
        self.drivers = []

    def add_driver(self, driver):
        if len(self.drivers) < self.driver_limit:
            self.drivers.append(driver)

    def get_average_ranking(self):
        rank_sum = 0
        for driver in self.drivers:
            rank_sum += driver.get_ranking()
        return rank_sum / len(self.drivers)


seattle_500 = Race('Seattle 500', 4)
# print(seattle_500.name, seattle_500.driver_limit, seattle_500.drivers)


class Driver:
    number_of_drivers = 0

    def __init__(self, name, age, ranking):
        self.name = name
        self.age = age
        self.ranking = ranking
        Driver.number_of_drivers += 1

    def get_ranking(self):
        return self.ranking


dale = Driver('Dale Earnhardt', 29, 100)
lewis = Driver('Lewis Hamilton', 36, 83)
eliud = Driver('Eliud Kipchoge', 36, 95)
sebastian = Driver('Sebastian Vettel', 34, 76)
ayrton = Driver('Ayrton Senna', 34, 99)

seattle_500.add_driver(dale)
seattle_500.add_driver(lewis)
seattle_500.add_driver(sebastian)
seattle_500.add_driver(ayrton)
print(seattle_500.get_average_ranking())

print(Driver.number_of_drivers)
