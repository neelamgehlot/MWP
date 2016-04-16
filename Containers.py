from collections import OrderedDict
#from aenum import Enum, enum

#Verb = enum(POSITIVE = 'Positive', NEGATIVE = 'Negative', TRANSFER = 'Transfer', OBSERVATION = 'Observation')


class Container:
# decide on default value of quantity

    def __init__(self, name=None, entity=None, attribute=None, quantity=None):
        if name == None:
            self.name = ""
            self.entity = ""
            self.attribute = ""
            self.quantity = ""
        else:
            self.name = name
            self.entity = entity
            self.attribute = attribute
            self.quantity = quantity
    # self.verb = Verb.OBSERVATION

    def copyContainer(self, container):
        self.name = container.name
        self.entity = container.entity
        self.attribute = container.attribute
        self.quantity = container.quantity


    # container.verb = self.verb

    def printContainer(self):
        print ("Name : " + str(self.name) + "\nEntity : " + str(self.entity) + "\nAttr : " + str(self.attribute) + "\nQuantity:" + str(self.quantity) + "\n")


