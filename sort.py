digitEvenList = []
digitOddList = []
capitalList = []
smallList = []


def convert(test):
    for value in test:
        if value.isdigit():
            if int(value) % 2 == 0:
                digitEvenList.append(value)
                print(digitEvenList)
            else:
                digitOddList.append(value)
                print(digitOddList)
        elif value.isupper():
            capitalList.append(value)
        elif value.islower():
            smallList.append(value)
    digitEvenList.sort()
    digitOddList.sort()
    capitalList.sort()
    smallList.sort()
    return smallList + capitalList + digitOddList+ digitEvenList



values = convert('kdxamAS12V611')

print(''.join(values))