class Question:
    def __init__(self):
        # print ("Constrctor created\n")
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

    def printContainer1(self):
        for i in range(0, len(self.container1)):
            print ("Name : " + str(self.container1[i].name) + "\nEntity : " + str(self.container1[i].entity) + "\nAttr : " + str(self.container1[i].attribute) + "\nQuantity : " + str(self.container1[i].quantity) + "\n")

    def printContainer2(self):
        for i in range(0, len(self.container2)):
            print ("Name : " + str(self.container2[i].name) + "\nEntity : " + str(self.container2[i].entity) + "\nAttr : " + str(self.container2[i].attribute) + "\nQuantity : " + str(self.container2[i].quantity) + "\n")