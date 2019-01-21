#parent class

class Human:

    def __init__(self):
        print("Human is destructive")

    def whoisThis(self):
        print("Human")

    def build(self):
        print("Build faster")

#child class

class Engineer(Human):

    def __init__(self, name):
        self.name = name
        super().__init__()
        print("{} Engineer is always ready".format(name))

    def whoisThis(self):
        super().whoisThis()
        print("{} is an Engineer".format(self.name))

    def work(self):
        print("{} Work faster".format(self.name))

    def build(self):
        print("{} Build faster".format(self.name))

anush = Engineer("Anush")
anush.whoisThis()
anush.build()
anush.work()
anush.build()