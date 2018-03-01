import ride


def getRides(fileName):
    f = open(fileName, 'r')
    n = f.readline().split(' ')[3]
    rides = []
    for i in range(n):
        rides.append(ride.Ride(f.readline().rstrip()))
    return rides


def getParameters(fileName):
    f = open(fileName, 'r')
    parametersList = f.readline().split(' ')
    f.close()
    return {
        'rows': parametersList[0],
        'columns': parametersList[1],
        'vehicles': parametersList[2],
        'rides': parametersList[3],
        'bonus': parametersList[4],
        'steps': parametersList[5],
    }
