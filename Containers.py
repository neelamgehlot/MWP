from collections import OrderedDict
#from aenum import Enum, enum

#Verb = enum(POSITIVE = 'Positive', NEGATIVE = 'Negative', TRANSFER = 'Transfer', OBSERVATION = 'Observation')


class Container:
# decide on default value of quantity

    def __init__(self, name, entity, attribute, quantity):
        self.name = name
        self.entity = entity
        self.attribute = attribute
        self.quantity = quantity
 #       self.verb = Verb.OBSERVATION

    def copyContainer(self, container):
        container.name = self.name
        container.entity = self.entity
        container.attribute = self.attribute
        container.quantity = self.quantity
  #      container.verb = self.verb

    def printContainer(self):
        print ("Name : " + str(self.name) + "\nEntity : " + str(self.entity) + "\nAttr : " + str(self.attribute) + "\nQuantity : " + str(self.quantity) + "\n")


