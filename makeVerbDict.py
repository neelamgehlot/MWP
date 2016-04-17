def makeVerbDictionary(fileName):
    verbDict = dict()

    lines = []
    with open(fileName) as tagged_file:
        lines = tagged_file.readlines()

    for i in range(0, len(lines)):
        # print lines[i]
        if lines[i].rstrip("\n").strip(" ") == "<vc>":
            for j in range(i + 1, len(lines)):
                if lines[j]=='\n':
                    continue
                if lines[j].rstrip("\n").strip(" ") == "</vc>":
                    i = j
                    break
                else:
                    line = lines[j].rstrip("\n").strip(" ")
                    temp = line.split(" ")
                    verb = temp[0].strip(" ")
                    category = temp[1].strip(" ")
                    # print verb,
                    # print category
                    if verb in verbDict:
                        verbDict[verb][int(category)] += 1

                    else:
                        verbDict[verb] = list(0 for i in range(0, 5))
                        verbDict[verb][int(category)] += 1



        else:
            continue

    return verbDict



