# coding=utf-8
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

    for i in range(0, len(lines) - 1):
        if lines[i] == '<s>':
            sentence = OrderedDict()
            for j in range(i + 1, len(lines)):
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
    sentence_number= 0
    for sentence in sentences:
        if sentenc_number == 0:
            containerFirstSentence(sentence, question)
        else:
            containerOtherSentence(sentence, question,sentence_number)

            # After creating copy containers, call modify on same sentence by passing the same copied container

            modifyContainer(sentence,question,sentence_number)
        sentence_number += 1

    arr_first_container = []
    arr_second_container = []


'''
    for i in range(0,len(sentences)):
        print "hello"
'''

def modifyContainer(sentence, question, sentence_number):


    # indexOfVerb = -1

    # indexOfQuantity = -1

    index = 0
    indexOfPronoun = -1
    indexOfProperNoun = -1
    valueEncountered = []
    integerWordDict = OrderedDict()

    for key, value in sentence.iteritems():
        integerWordDict[index] = key

        if value == 'PRP':
            indexOfPronoun = index

        if value == 'NNP' and value in question.names:
            indexOfProperNoun = index

        if value == 'VM':
            # indexOfVerb = index

            actionToBePerformed = categoriseVerb(key)

            question.verbs.add(key)

        if value == 'QC':
            # indexOfQuantity = index
            val = convertToEnglish(key)
            valueEncountered.append(val)
        index += 1


    # Depending on action to be performed, there will be two operations
    actionInOneContainer, actionInSecondContainer = twoActions(actionToBePerformed)



    if indexOfPronoun < indexOfProperNoun and indexOfPronoun!=-1 and indexOfProperNoun!=-1:
        q1 = modifyQuantityOfCurrentContainer(question.container1[sentence_number].quantity, actionInOneContainer, val)

        question.container1[sentence_number].quantity = q1

        q2 = modifyQuantityOfCurrentContainer(question.container2[sentence_number].quantity, actionInSecondContaine,val)

        question.container2[sentence_number].quantity = q2

    if indexOfPronoun != -1 and indexOfProperNoun == -1:
        # In this sentence, only previous container is into existence, so change only in one container
        # Also the twoActions will return only one action
        # so make changes in only one quantity
        q1 = modifyQuantityOfCurrentContainer(question.container1[sentence_number].quantity, actionInOneContainer,val)

        question.container1[sentence_number].quantity = q1

    


def modifyQuantityOfCurrentContainer(quantity_of_container, action, value_to_add_delete):

    # add or delete value
    return "updatedQuantity"

def twoActions(actionToBePerformed):
    # Depending upon either observation, construct, destroy, transfer, return pos,neg, None
    return "positive", "negative"

def categoriseVerb(word):


def containerFirstSentence(sentence, question):
    names = set()
    for key, value in sentence.iteritems():
        if value == "NNP":
            names.add(key)
    question.names = names
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

                quantity = convertToEnglish(key)
                quantityFlag = True

            if quantityFlag and not entityFlag and value == "NN":
                entity = key
                entityFlag = True

            if quantityFlag and not entityFlag and value == "JJ":
                attribute = key

        container = Container(name, entity, attribute, quantity)

        question.addContainer(container)

        # add empty container in second container also

        question.addContainer(Container())

        container.printContainer()


    else:
        # There are more than two NNP

        integer_word_dict = OrderedDict()
        count = 0
        indexOfFirstNNP = -1
        indexOfSecondNNP = -1
        for key, value in sentence.iteritems():
            integer_word_dict[count] = key

            if value == 'NNP' and indexOfFirstNNP == -1:
                indexOfFirstNNP = count
            elif value == 'NNP' and indexOfFirstNNP != -1:
                indexOfSecondNNP = count

            count += 1


        quantityFlag = False
        entityFlag = False
        name = ""
        quantity = ""
        entity = ""
        attribute = ""
        for i in range(0, indexOfSecondNNP):
            if sentence[integer_word_dict[i]] == "NNP":
                name = integer_word_dict[i]

            if sentence[integer_word_dict[i]] == "QC" and isNumber(integer_word_dict[i]):

                quantity = convertToEnglish(integer_word_dict[i])
                quantityFlag = True

            if quantityFlag and not entityFlag and sentence[integer_word_dict[i]] == "NN":
                entity = integer_word_dict[i]
                entityFlag = True

            if quantityFlag and not entityFlag and sentence[integer_word_dict[i]] == "JJ":
                attribute = key

        container = Container(name, entity, attribute, quantity)

        question.addContainer(container)

        container.printContainer()

        for i in range(indexOfSecondNNP, len(sentence)):
            if sentence[integer_word_dict[i]] == "NNP":
                name = integer_word_dict[i]

            if sentence[integer_word_dict[i]] == "QC" and isNumber(integer_word_dict[i]):
                quantity = convertToEnglish(integer_word_dict[i])
                quantityFlag = True

            if quantityFlag and not entityFlag and sentence[integer_word_dict[i]] == "NN":
                entity = integer_word_dict[i]
                entityFlag = True

            if quantityFlag and not entityFlag and sentence[integer_word_dict[i]] == "JJ":
                attribute = integer_word_dict[i]

        container = Container(name, entity, attribute, quantity)

        question.addContainer(container)

        container.printContainer()


def containerOtherSentence(sentence, question, sentence_number):
    # find pronoun, noun, verb

    copyConstructorOf1 = Container()

    copyConstructorOf1.copyContainer(question.container1[sentence_number-1])
    print "first ka copy"
    copyConstructorOf1.printContainer()

    question.addContainer(copyConstructorOf1)
    print len(question.container1)
    name = ""
    quantity = ""
    entity = ""
    attribute = ""

    quantityFlag = False
    entityFlag = False
    if len(question.names)==1:

        for key, value in sentence.iteritems():
            if value == "NNP" and key not in question.names:
                name = key
                question.names.add(name)

            if quantityFlag and not entityFlag and value == "NN":
                entity = key
                entityFlag = True

            if quantityFlag and not entityFlag and value == "JJ":
                attribute = key

        container = Container(name, entity, attribute, "J")

        question.addContainer(container)

        container.printContainer()

    else:
        # Copy second container also that is make container2[1]
        copyConstructorOf2 = Container()

        copyConstructorOf2.copyContainer(question.container2[sentence_number-1])
        print "second copy"
        copyConstructorOf2.printContainer()

        question.addContainer(copyConstructorOf2)


def isNumber(num):
    return True


def convertToEnglish(num):
    ans = ""
    hindiToEnglish = OrderedDict()

    # for i in range(0,10):
    hindiToEnglish['०'] = 0;
    hindiToEnglish['१'] = 1;
    hindiToEnglish['२'] = 2;
    hindiToEnglish['३'] = 3;
    hindiToEnglish['४'] = 4;
    hindiToEnglish['५'] = 5;
    hindiToEnglish['६'] = 6;
    hindiToEnglish['७'] = 7;
    hindiToEnglish['८'] = 8;
    hindiToEnglish['९'] = 9;

    for i in range(0, len(num), 3):
        temp_digit = hindiToEnglish[num[i:i + 3]]
        ans += str(temp_digit)
    return ans


if __name__ == "__main__":
    main()
