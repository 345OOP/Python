def find_max(myList):
    maximum = myList[0]
    for number in myList:
        if number > maximum:
            maximum = number
    return maximum
