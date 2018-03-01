class Ride:
    def __init__(self, parameters):
        parametersList = parameters.split(' ')
        self.startX = parametersList[0]
        self.startY = parametersList[1]

        self.finishX = parametersList[2]
        self.finishY = parametersList[3]

        self.earliestStart = parametersList[4]
        self.earliestFinish = parametersList[5]

    def assignCar(self,car):
        self.assignedCar = car

    def assigned(self):
        if self.assignedCar:
            return self.assignedCar
        else:
            return False