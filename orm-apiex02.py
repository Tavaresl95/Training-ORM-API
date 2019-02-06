class Flight:
    def __init__(self, origin, destination, duration):
        self.origin = origin
        self.destination = destination
        self.duration = duration

    def print_info(self):
        print("Flight origin: {}".format(self.origin))
        print("Flight destination: {}".format(self.destination))
        print("Flight duration: {}".format(self.duration))

def main():
    f1 = Flight(origin="Brasilia", destination="Natal", duration=435)
    f1.print_info()

    f2 = Flight(origin="Tokyo", destination="Canada", duration=570)
    f2.print_info()

if __name__ == "__main__":
    main()