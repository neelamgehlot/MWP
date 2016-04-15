from collections import OrderedDict

class Container:

    countainer_Count = 0
    def __init__(self, name, entity, attribute, quantity, verb):
        self.name = name
        self.entity = entity
        self.attribute = attribute
        self.quantity = quantity
        self.verb = verb
        Container.countainer_Count += 1

    def createContainerFromSentence(self,sentence):
        for key,value in sentence.iteritems():
            print str(key)+" "+str(value)


def main():
    global j
    lines = []
    with open("POSOut.txt") as tagged_file:
        lines = tagged_file.readlines()

    sentences = []

    for i in range(0, len(lines)):
        lines[i] = lines[i].rstrip("\n")

    for i in range(0, len(lines)-1):
        if lines[i]=='<s>':
            sentence = OrderedDict()
            for j in range(i+1, len(lines)):
                if lines[j]=='</s>':
                    i = j
                    break
                else:
                    tag, word = lines[j].split(" ")
                    # print (tag + word)
                    sentence[tag] = word
                    # sentence[]
            sentences.append(sentence)

        else:
            continue

    for sentence in sentences:
        for key, value in sentence.iteritems():
            print key,
            print value
        print("")

    arr_first_container = []
    arr_second_container = []

    for i in range(0,len(sentences)):



# for every question, there will be n sentences
# Hence creating array of dictionaries




if __name__=="__main__":
    main()