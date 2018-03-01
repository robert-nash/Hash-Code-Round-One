class Ride:
    assignedCar = False

    def __init__(self, parameters):
        parametersList = parameters.split(' ')
        self.startX = int(parametersList[0])
        self.startY = int(parametersList[1])

        self.finishX = int(parametersList[2])
        self.finishY = int(parametersList[3])

        self.earliestStart = int(parametersList[4])
        self.earliestFinish = int(parametersList[5])

    def assignCar(self, car):
        self.assignedCar = car

    def assigned(self):
        if self.assignedCar:
            return self.assignedCar
        else:
            return False
