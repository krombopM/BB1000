year = list(yearBirths.year)
births = list(yearBirths.births)
listOfIndices = []
years = list(range(1880, 2010))
for item in years:
    listOfIndices.append(year.count(item))
listOfIndices.insert(0,0)
actualListOfIndices = []
for item in range(len(listOfIndices)):
    actualListOfIndices.append(item + sum(listOfIndices[0:item]))
del actualListOfIndices[1]
print(actualListOfIndices)
sumOfBirthsPerYear = []
for item in actualListOfIndices[1:-1]:
    amount = sum
