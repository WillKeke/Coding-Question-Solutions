def smallestDifference(array1, array2):
    array1.sort()
    array2.sort()
    index1 = 0
    index2 = 0
    smallest = float("inf")
    current = float("inf")
    smallestPair = []
    while index1 < len(array1) and index2 < len(array2):
        firstNum = array1[index1]
        secondNum = array2[index2]
        if firstNum < secondNum:
            current = secondNum - firstNum
            index1 += 1
        elif secondNum < firstNum:
            current = firstNum - secondNum
            index2 += 1
        else:
            return [firstNum, secondNum]
        if smallest > current:
            smallest = current
            smallestPair = [firstNum, secondNum]
    return smallestPair
