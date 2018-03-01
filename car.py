class Car:

    carActive = False
    journeyStarted = False
    
    currentLocationX = 0
    currentLocationY = 0

    startX = 0
    startY = 0

    destinationX = 0
    destinationY = 0

    currentRider = False
    rideHistory = []

    def __init__(self,id):
        self.id = id

    def startCar (self, startX, startY, destinationX, destinationY, riderID):

        self.startX = startX
        self.startY = startY
        self.destinationX = destinationX
        self.destinationY = destinationY
        self.carActive = True

        self.currentRider = riderID

    def moveCar (self):

        if (self.journeyStarted == False):
            finalX = self.startX
            finalY = self.startY
        else:
            finalX = self.destinationX
            finalY = self.destinationY 

        if ((self.currentLocationX != finalX) or (self.currentLocationY != finalY)):
            if (finalX > self.currentLocationX):
                self.currentLocationX += 1
            elif (finalX < self.currentLocationX):
                self.currentLocationX -= 1
            elif (finalY > self.currentLocationY):
                self.currentLocationY += 1
            elif (finalY < self.currentLocationY):
                self.currentLocationY -= 1

            if ((self.currentLocationX == finalX) and (self.currentLocationY == finalY)):
                if ((finalX == self.destinationX) and (finalY == self.destinationY)):
                    self.carActive = False
                    self.journeyStarted = False
                    self.rideHistory.append(self.currentRider)
                    self.currentRider = False
                    ## Finished
                else:
                    self.journeyStarted = True















