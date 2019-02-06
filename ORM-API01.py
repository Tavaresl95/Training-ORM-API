class Flight:
    def __init__(self, origin, destination, duration):
        self.origin = origin
        self.destination = destination
        self.duration = duration

def main():
        #criando um voo
        f = Flight(origin="Salvador", destination="Natal", duration=540)

        #mudar valores
        f.duration += 15

        #mostrar resultados
        print(f.origin)
        print(f.destination)
        print(f.duration)
if __name__ == "__main__":
        main()