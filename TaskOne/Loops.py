class Initial:
    def __int__(self, number):
        self.number = number


class Counting(Initial):
    init = Initial()
    init.number = 100
    for init.number in range(init.number, 0, -1):

        if init.number % 15 == 0:
            print("Agile", "Software", "Testing")
        elif init.number % 5 == 0:
            print("Agile")
        elif init.number % 3 == 0:
            print("Software")
        else:
            print(init.number)


