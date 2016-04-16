from collections import OrderedDict
from Containers import Container
from Question import Question


def main():
    global j
    lines = []
    with open("POSOut.txt") as tagged_file:
        lines = tagged_file.readlines()

    sentences = []

    for i in range(0, len(lines)):
        lines[i] = lines[i].rstrip("\n")

    for i in range(0, len(lines)-1):
        if lines[i] == '<s>':
            sentence = OrderedDict()
            for j in range(i+1, len(lines)):
                if lines[j] == '</s>':
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

    question = Question()
    count = 0
    for sentence in sentences:
        if count == 0:
            containerFirstSentence(sentence, question)
        else:
            containerOtherSentence(sentence, question)

        count += 1

    arr_first_container = []
    arr_second_container = []
'''
    for i in range(0,len(sentences)):
        print "hello"
'''


def containerFirstSentence(sentence, question):
    names = set()
    for key, value in sentence.iteritems():
        if value == "NNP":
            names.add(key)
    print (names)
    if len(names) == 1:
        quantityFlag = False
        entityFlag = False
        name = ""
        quantity = ""
        entity = ""
        attribute = ""
        for key, value in sentence.iteritems():

            # print str(key)+" "+str(value)
            if value == "NNP":
                name = key

            if value == "QC" and isNumber(key):
                quantity = key
                quantityFlag = True

            if quantityFlag and not entityFlag and value == "NN":
                entity = key
                entityFlag = True

            if quantityFlag and not entityFlag and value == "JJ":
                attribute = key

        container = Container(name, entity, attribute, quantity)

        question.addContainer(container)

        container.printContainer()


def containerOtherSentence(sentence, question):
    '''
    Container construction for other sentences
    '''

def isNumber(num):
    return True

# for every question, there will be n sentences
# Hence creating array of dictionaries




if __name__=="__main__":
    main()