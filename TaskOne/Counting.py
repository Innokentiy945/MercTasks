class Division:
    def checkDivision(number, divider):
        if number % divider == 0:
            return True
        else:
            return False


class Initial:
    def __int__(self, count, dividerOne, divederTwo):
        self.count = count
        self.dividerOne = dividerOne
        self.dividerTwo = divederTwo


class Counting(Initial, Division):
    init = Initial()
    div = Division
    init.count = 100
    init.dividerOne = 5
    init.dividerTwo = 3
    for init.count in range(init.count, 0, -1):

        if div.checkDivision(init.count, init.dividerOne*init.dividerTwo):
            print("Agile", "Software", "Testing")
        elif div.checkDivision(init.count, init.dividerOne):
            print("Agile")
        elif div.checkDivision(init.count, init.dividerTwo):
            print("Software")
        else:
            print(init.count)
