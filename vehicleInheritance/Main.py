from Class import *
if __name__ == '__main__':
    v1 = Vehicle("corolla", 100_000.00, 20_000)

    # show the vehicle data
    print("Vehicle 1 data:")
    v1.show_data()

    # updating price
    v1.update_price(-50_000)

    c1 = Car("womenfolks", 5_122_777, 63_737, 3)

    # Show car data
    print("\nCar 1 data:")
    c1.show_data()

    # using set methods
    c1.model_set("menfolks")
    c1.price_set(592_595)
    c1.mileage_set(25_252)
    c1.qnt_doors_set(2)
    print("\nloading new data...\n")

    # show modified car data
    print("Car 1  modified data:")
    c1.show_data()

    c2 = Car("wags", 523_227, 63_737)

    # Show car data
    print("\nCar 2 data:")
    c2.show_data()

    # using set methods
    c2.model_set("faded")
    c2.price_set(63_638)
    c2.mileage_set(25_252)
    print("\nloading new data...\n")

    # show modified car data
    print("Car 2  modified data:")
    c2.show_data()

    c3 = Car("ski", 36_737)

    # Show car data
    print("\nCar 3 data:")
    c3.show_data()

    # using set methods
    c3.model_set("yuu")
    c3.price_set(372_383)
    print("\nloading new data...\n")

    # show modified car data
    print("Car 3  modified data:")
    c3.show_data()

    m1 = Motorcycle("deque", 62_772, 10_000, 600)

    # Show motorcycle data
    print("\nMotorcycle 1 data:")
    m1.show_data()

    # using set methods
    m1.model_set("eyrie")
    m1.price_set(743_793)
    m1.mileage_set(500_252)
    m1.cylinder_capacity_set(1200)
    print("\nloading new data...\n")

    # show modified car data
    print("Motorcycle 1  modified data:")
    m1.show_data()

    m2 = Motorcycle("vicinity", 10_000_000, 26_933)

    # Show car data
    print("\nMotorcycle 2 data:")
    m2.show_data()

    # using set methods
    m2.model_set("faded")
    m2.price_set(63_638)
    m2.mileage_set(25_252)
    print("\nloading new data...\n")

    # show modified car data
    print("Motorcycle 2  modified data:")
    m2.show_data()

    # testing methods
    print(f"\n {vars(v1)}")
    print(f"\n{c1.__dict__}")
    print(f"\n{m1.__dict__}")
    c2.car_condition()
