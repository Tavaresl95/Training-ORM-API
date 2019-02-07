class Flight:

    counter = 1

    def __init__(self, origin, destination, duration):

        # Creating always a new id
        self.id = Flight.counter
        Flight.counter += 1

        # Look into passengers list
        self.passengers = []

        #information about the flight
        self.origin = origin
        self.destination = destination
        self.duration = duration

    def print_info(self):
        print("Flight origin: {}".format(self.origin))
        print("Flight destination: {}".format(self.destination))
        print("Flight duration: {}".format(self.duration))

        print()
        print("Passengers:")
        for passenger in self.passengers:
            print("{}".format(passenger.name))

    def delay(self, amount):
        self.duration += amount

    def add_passenger(self, p):
        self.passengers.append(p)
        p.flight_id = self.id


class Passenger:

    def __init__(self, name):
        self.name = name


def main():

    # Create flight 1
    f1 = Flight(origin="New York", destination="Paris", duration=540)

    # create passengers
    alice = Passenger(name="Alice")
    bob = Passenger(name="Bob")

    # Add passengers
    f1.add_passenger(alice)
    f1.add_passenger(bob)

    f1.print_info()


if __name__ == "__main__":
    main()
