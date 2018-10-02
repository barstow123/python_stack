class products:

    def __init__(self, price, name, weight, brand, status='for sale'):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.status = status

    def sell(self):
        if (self.status == 'for sale'):
            status = 'sold'
        else :
            print('Error: item already sold')

    def add_tax(self, tax):
        return self.price*tax

    def return_item(self, reason_for_return):
        