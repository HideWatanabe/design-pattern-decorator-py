class coffee:
    def drink(self):
        print("Drinking a coffee")

class sugar_decorador:
    def __init__(self, decoratee):
        self._decoratee = decoratee
        print("OK!")

    def drink(self):
        print("Putting some sugar")
        self._decoratee.drink()


if __name__ == "__main__":
    wish = coffee()
    cup = sugar_decorador(wish)
    cup.drink()