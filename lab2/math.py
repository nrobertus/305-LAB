import antigravity


makeList = ["Chevy Silverado", "Chevy Corvette", "Chevy Spark"]
mpgList = [15.0, 20.0, 30.0]

def calcOperatingCost(milesPerYear, costOfGas, mpg):
    gallonsPerYear = milesPerYear / mpg
    return costOfGas * gallonsPerYear

for x in range(0, len(makeList)):
    print(makeList[x] + ": $" + str(calcOperatingCost(10000.0, 1.79, mpgList[x])))

for x in range(len(makeList)):
    print makeList[x]
