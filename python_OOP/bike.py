class Bike:

    def __init__(self, price, max_speed, miles=0):
        self.price = price
        self.max_speed = max_speed
        self. miles = miles

    def display_info(self):
        print(f'price:\t\t{self.price}\nmax_speed:\t{self.max_speed}\nmiles:\t\t{self.miles}')
        return self

    def ride(self):
        print('riding'); self.miles += 10
        return self

    def reverse(self):
        print('reversing'); self.miles -= 5
        return self


my_bike = Bike(price=100, max_speed='25mph', miles=50)
his_bike = Bike(price=500, max_speed='40mph', miles=200)
that_other_bike = Bike(price=1000, max_speed='45mph', miles=2000)

my_bike.display_info().ride().reverse().reverse().display_info()
