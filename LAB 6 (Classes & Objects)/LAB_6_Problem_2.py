class Vehicle:
    def __init__(self, name, seating_capacity):
        self.name = name
        self.seating_capacity = seating_capacity

    def fare(self):
        return self.seating_capacity * 100


class Bus(Vehicle):
    def fare(self):
        fare = super().fare()
        return fare + fare * 0.10


bus = Bus("AIUB Bus", 40)
print(bus.fare())
