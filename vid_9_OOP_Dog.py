
#BRR
#MSAW


class Dog:

    def __init__(self, name="", weight=0, height=0):
        self.name=name
        self.weight=weight
        self.height=height

    def run(self):
        print("{} the dog runs".format(self.name))

    def eat(self):
        print("{} the dog eats".format(self.name))

    def bark(self):
        print("{} the dog barks".format(self.name))


def main():
    dog_one=Dog("Spot", 66, 26)
    dog_one.bark()

    dog_2=Dog("Simba", 62, 25)
    dog_2.eat()

    dog_3=Dog("Bowser",55, 12)
    dog_3.run()

main()
