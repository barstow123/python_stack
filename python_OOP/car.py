class Car:

    def __init__(self, price, speed, fuel, mileage=0):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = .15
        else :
            self.tax = .12

    def display_all(self):
        print(f'price:\t\t{self.price}\n'
              f'speed:\t\t{self.speed}\n'
              f'fuel:\t\t{self.fuel}\n'
              f'mileage:\t{self.mileage}\n'
              f'tax:\t\t{self.tax}')


car1 = Car(price=30000, speed='120mph', fuel='unleaded', mileage=30000)
car2 = Car(price=3000, speed='90mph', fuel='unleaded', mileage=120000)
car3 = Car(price=45000, speed='140mph', fuel='unleaded', mileage=15000)
car4 = Car(price=7000, speed='105mph', fuel='unleaded', mileage=60000)
car5 = Car(price=1000, speed='20mph', fuel='unleaded', mileage=300000)
car6 = Car(price=30000, speed='120mph', fuel='unleaded', mileage=30000)

car1.display_all()