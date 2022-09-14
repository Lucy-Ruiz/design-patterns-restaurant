from franchise import Franchise

class Simulation:
    def __init__(self):
        pass

    def run_simulation(self):
        obj_1 = Franchise(78)
        obj_1.place_order()
        obj_1.place_order()
        obj_1.place_order()
        obj_2 = Franchise(23)
        obj_2.place_order()
        obj_2.place_order()
        obj_3 = Franchise(4)
        obj_3.place_order()
