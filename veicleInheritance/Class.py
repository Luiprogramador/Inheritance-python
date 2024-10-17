class Vehicle(object):
    def __init__(self, model, price, mileage=0):
        self.mileage = mileage
        self.price = price
        self.model = model

    def mileage_get(self):
        return self.mileage

    def mileage_set(self, new_mileage):
        self.mileage = new_mileage

    def price_get(self):
        return self.price

    def price_set(self, new_price):
        self.mileage = new_price

    def model_get(self):
        return self.model

    def model_set(self, new_model):
        self.model = new_model

    def show_data(self):
        data = self.__str__()
        for key, value in data.items():
            print(f'{key.title()}: {value}')

    def __str__(self):
        return {'model': self.model, 'price': self.price, 'mileage': self.mileage}

    def update_price(self, price_increase):
        if price_increase < 0:
            print("put a value greater than 0.")
        else:
            self.price = self.price + price_increase
            print(f"The value increasing is {self.price}")

    def car_condition(self):
        condition = 0
        if self.mileage == 0:
            self.mileage = condition
            print("The car is 0 kilometers.")
        elif 0 < self.mileage < 20_000:
            self.mileage = condition
            print("The car is pre-owned.")
        elif self.mileage > 20_000:
            self.mileage = condition
            print("The car is used")
        else:
            print("it's not possible to use a value less than 0")


class Car(Vehicle):
    def __init__(self, model, price, mileage=0, qnt_doors=4):
        super().__init__(model, price, mileage)
        self.qnt_doors = qnt_doors

    def qnt_doors_get(self):
        return self.qnt_doors

    def qnt_doors_set(self, new_qnt_doors):
        self.qnt_doors = new_qnt_doors

    def show_data(self):
        data = self.return_data()
        for key, value in data.items():
            print(f'{key.title()}: {value}')

    def return_data(self):
        return {'model': self.model, 'price': self.price, 'mileage': self.mileage, 'doors': self.qnt_doors}


class Motorcycle(Vehicle):
    def __init__(self, model, price, mileage=0, cylinder_capacity=0):
        super().__init__(model, price, mileage)
        self.cylinder_capacity = cylinder_capacity

    def cylinder_capacity_get(self):
        return self.cylinder_capacity

    def cylinder_capacity_set(self, new_cylinder):
        self.cylinder_capacity = new_cylinder

    def show_data(self):
        data = self.__str__()
        for key, value in data.items():
            print(f'{key.title()}: {value}')

    def __str__(self):
        return {'model': self.model, 'price': self.price, 'mileage': self.mileage,
                'cylinder_capacity': self.cylinder_capacity}
