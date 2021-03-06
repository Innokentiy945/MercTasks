class Initial:
    def __int__(self, number):
        self.number = 100


class Counting(Initial):
    initial = Initial()
    for initial in range(100, 0, -1):

        if initial % 15 == 0:
            print("Agile", "Software", "Testing")
        elif initial % 5 == 0:
            print("Agile")
        elif initial % 3 == 0:
            print("Software")
        else:
            print(initial)


