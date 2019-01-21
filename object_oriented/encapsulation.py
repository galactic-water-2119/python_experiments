class Industry:

    def __init__(self):
        self.__name = "Information Technology"
        self.__maxrevenue = 1000

    def revenue(self):
        print("Industry name: {} revenue: {}".format(self.__name, self.__maxrevenue))

    def setMaxRevenue(self, revenue):
        self.__maxrevenue = revenue


IT = Industry()
IT.revenue()

# change the revenue

IT.__maxrevenue = 2000
IT.revenue()

# using setter function

IT.setMaxRevenue(3000)
IT.revenue()


