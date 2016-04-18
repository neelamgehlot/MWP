# coding=utf-8
from __future__ import division
from collections import OrderedDict
from makeVerbDict import makeVerbDictionary
from Containers import Container
from Question import Question

verbTags = ['VM','PSP','NST','VAUX']

trainingDictionary = makeVerbDictionary("POSOutWithVC.txt")

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
    for i in range(0,len(sentences)-1):
        if sentence_number == 0:
            containerFirstSentence(sentences[i], question)
        else:
            containerOtherSentence(sentences[i], question,sentence_number)

            # After creating copy containers, call modify on same sentence by passing the same copied container

            modifyContainer(sentences[i],question,sentence_number)
        sentence_number += 1
    name = ""
    quantity = ""
    entity = ""
    attribute = ""
    for key, value in sentences[len(sentences)-1].iteritems():
        if value == "NNP":
            name = key




    print "Container1"
    question.printContainer1()
    print "Container2"
    question.printContainer2()
    arr_first_container = []
    arr_second_container = []

def modifyContainer(sentence, question, sentence_number):

    # print sentence
    # indexOfVerb = -1

    # indexOfQuantity = -1

    index = 0
    indexOfPronoun = -1
    valueEncountered = []
    integerWordDict = OrderedDict()
    listOfIndicesOfProperNouns = []
    namesOfProperNouns = []
    verbsFound = []
    val = 0

    for key, value in sentence.iteritems():
        integerWordDict[index] = key

        if value == 'PRP':
            indexOfPronoun = index

        if value == 'NNP' :
            listOfIndicesOfProperNouns.append(index)
            namesOfProperNouns.append(key)

        if value in verbTags:
            # print key
            verbsFound.append(key)


        if value == 'QC':
            # indexOfQuantity = index
            val = convertToEnglish(key)
            valueEncountered.append(val)
        index += 1


    actionToBePerformed = categoriseVerb(verbsFound)

    # Depending on action to be performed, there will be two operations
    actionInOneContainer, actionInSecondContainer = twoActions(actionToBePerformed)


    if len(listOfIndicesOfProperNouns)==2:
        # name name
        firstName = namesOfProperNouns[0]
        secondName = namesOfProperNouns[1]

        if firstName == question.container1[sentence_number].name:
            q1 = modifyQuantityOfCurrentContainer(question.container1[sentence_number].quantity, actionInOneContainer, val)

            question.container1[sentence_number].quantity = q1
        else:
            q2 = modifyQuantityOfCurrentContainer(question.container2[sentence_number].quantity, actionInSecondContainer,val)

            question.container2[sentence_number].quantity = q2

        if firstName == question.container2[sentence_number].name:
            q2 = modifyQuantityOfCurrentContainer(question.container2[sentence_number].quantity, actionInOneContainer,val)

            question.container2[sentence_number].quantity = q2
        else:
            q1 = modifyQuantityOfCurrentContainer(question.container1[sentence_number].quantity, actionInSecondContainer, val)

            question.container1[sentence_number].quantity = q1

    elif len(listOfIndicesOfProperNouns)==1 and indexOfPronoun!= -1:
        # name pronoun
        q1 = modifyQuantityOfCurrentContainer(question.container1[sentence_number].quantity, actionInOneContainer, val)

        question.container1[sentence_number].quantity = q1

        q2 = modifyQuantityOfCurrentContainer(question.container2[sentence_number].quantity, actionInSecondContainer,val)

        question.container2[sentence_number].quantity = q2

    elif indexOfPronoun!=-1:
        #  only pronoun
        q1 = modifyQuantityOfCurrentContainer(question.container1[sentence_number].quantity, actionInOneContainer, val)

        question.container1[sentence_number].quantity = q1

    elif indexOfPronoun == -1:
        # only noun
        nameFound = namesOfProperNouns[0]
        if nameFound == question.container1[sentence_number].name:
            q1 = modifyQuantityOfCurrentContainer(question.container1[sentence_number].quantity, actionInOneContainer, val)

            question.container1[sentence_number].quantity = q1
        else:
            q2 = modifyQuantityOfCurrentContainer(question.container2[sentence_number].quantity, actionInOneContainer, val)

            question.container2[sentence_number].quantity = q2

def modifyQuantityOfCurrentContainer(quantity_of_container, action, value_to_add_delete):
    # add or delete value
    if action.strip(" ") == "POSITIVE":
        return str(quantity_of_container) + " + " + str(value_to_add_delete)
    elif action.strip(" ") == "NEGATIVE":
        return str(quantity_of_container) + " - " + str(value_to_add_delete)
    else:
        return str(quantity_of_container)

def twoActions(actionToBePerformed):
    # Depending upon either observation, construct, destroy, transfer, return pos,neg, None
    if actionToBePerformed == 0 :
        return "NONE", "NONE"
    elif actionToBePerformed == 1:
        return "POSITIVE", "POSITIVE"
    elif actionToBePerformed == 2:
        return "NEGATIVE", "NEGATIVE"
    elif actionToBePerformed == 3:
        return "POSITIVE", "NEGATIVE"
    else:
        return "NEGATIVE", "POSITIVE"

def categoriseVerb(verbsFound):
    # for i in range(0, len(verbsFound)):
    #     print verbsFound[i],
    # for key, value in trainingDictionary.iteritems():
    #     print key,
    #     print value
    # print trainingDictionary
    newValuesOfProbabilty = [1.0 for i in range(0,5)]
    for j in range(0,5):
        for i in range(0,len(verbsFound)):
            if verbsFound[i] in trainingDictionary:
                individualProbabilty = trainingDictionary[verbsFound[i]][j]/trainingDictionary[verbsFound[i]][5]
                newValuesOfProbabilty[j] = newValuesOfProbabilty[j]*individualProbabilty

    max_value = max(newValuesOfProbabilty)

    # print newValuesOfProbabilty
    max_indices = [index for index, value in enumerate(newValuesOfProbabilty) if value==max_value]
    return max_indices[0]

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

        # container.printContainer()
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

        # container.printContainer()
        if indexOfSecondNNP!=-1:
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

            # container.printContainer()

def containerOtherSentence(sentence, question, sentence_number):
    # find pronoun, noun, verb

    copyConstructorOf1 = Container()

    copyConstructorOf1.copyContainer(question.container1[sentence_number-1])
    # print "first ka copy"
    # copyConstructorOf1.printContainer()

    question.addContainer(copyConstructorOf1)
    # print len(question.names)
    # print "Hah"
    name = ""
    quantity = ""
    entity = ""
    attribute = ""

    quantityFlag = False
    entityFlag = False
    if len(question.names)==1:
        booleanMakeNewContainer = False
        for key, value in sentence.iteritems():
            if value == "NNP" and key not in question.names:
                newName = key
                booleanMakeNewContainer = True
                question.names.add(newName)

            if quantityFlag and not entityFlag and value == "NN":
                entity = key
                entityFlag = True

            if quantityFlag and not entityFlag and value == "JJ":
                attribute = key

        if booleanMakeNewContainer==True:
            container = Container(newName, entity, attribute, "J")

            question.addContainer(container)

            # container.printContainer()

    else:
        # Copy second container also that is make container2[1]
        copyConstructorOf2 = Container()

        copyConstructorOf2.copyContainer(question.container2[sentence_number-1])
        # print "second copy"
        # copyConstructorOf2.printContainer()

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
