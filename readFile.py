import ride


def getRides(fileName):
    f = open(fileName, 'r')
    n = int(f.readline().split(' ')[3])
    rides = []
    for i in range(n):
        rides.append(ride.Ride(f.readline().rstrip()))
    return rides


def getParameters(fileName):
    f = open(fileName, 'r')
    parametersList = f.readline().split(' ')
    f.close()
    return {
        'rows': int(parametersList[0]),
        'columns': int(parametersList[1]),
        'vehicles': int(parametersList[2]),
        'rides': int(parametersList[3]),
        'bonus': int(parametersList[4]),
        'steps': int(parametersList[5]),
    }
