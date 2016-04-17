class Question:
    def __init__(self):
        print ("Constrctor created\n")
        self.container1 = []
        self.container2 = []
        self.names = set()


    def addContainer(self, container):
        if len(self.container1) == 0:
            self.container1.append(container)

        elif len(self.container2) == 0 and container.name != self.container1[0].name:
            self.container2.append(container)

        elif container.name == self.container1[0].name:
            self.container1.append(container)

        else:
            self.container2.append(container)
