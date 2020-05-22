dict = {"Rick": 85, "Amit": 42, "George": 53, "Tanya": 60, "Linda": 35}


def returnSum(myDict):
    sum = 0
    for i in myDict:
        sum = sum + myDict[i]

    return sum
print("Sum :", returnSum(dict))