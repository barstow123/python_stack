class Product:

    def __init__(self, price, name, weight, brand, status='for sale'):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.status = status

    def sell(self):
        if (self.status == 'for sale'):
            status = 'sold'
        else:
            print('Error: item already sold')
        return self

    def add_tax(self, tax):
        return self.price * tax

    def return_item(self, reason_for_return):
        if (reason_for_return == 'defective'):
            self.status = reason_for_return
            self.price = 0
        if (reason_for_return == 'like new'):
            self.status = 'for sale'
        if (reason_for_return == 'opened'):
            self.status = 'used'
            self.price = self.price*0.8
        return self

    def display_info(self):
        print('price:\t\t%0.2f' % self.price)
        print(f'name:\t\t{self.name}\n'
              f'weight:\t\t{self.weight}\n'
              f'brand:\t\t{self.brand}\n'
              f'status:\t\t{self.status}\n\n')
        return self


toy = Product(9.99, 'Buzz Lightyear of Star Command', '1.5lb', 'Hasbro')

toy.display_info().sell().return_item('opened').display_info()
