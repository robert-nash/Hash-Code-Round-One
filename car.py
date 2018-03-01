class Car:

    carActive = False
    journeyStarted = False
    
    currentLocationX = 0
    currentLocationY = 0

    startX = 0
    startY = 0

    destinationX = 0
    destinationY = 0 

    def startCar (self, startX, startY, destinationX, destinationY):

        self.startX = startX
        self.startY = startY
        self.destinationX = destinationX
        self.destinationY = destinationY
        self.carActive = True

    def moveCar (self):

        if (journeyStarted == False):
            finalX = startX
            finalY = startY
        else:
            finalX = destinationX
            finalY = destinationY 

        if ((currentLocationX != finalX) || (currentLocationY != finalY)):
            if (finalX > currentLocationX):
                self.currentLocationX += 1
            elif (finalX < currentLocationX):
                self.currentLocationX -= 1
            elif (finalY > currentLocationY):
                self.currentLocationY += 1
            elif (finalY < currentLocationY):
                self.currentLocationY -= 1

            if ((currentLocationX == finalX) && (currentLocationY == finalY)):
                if ((finalX == destinationX)&&(finalY == destinationY)):
                    self.carActive = False
                    self.journeyStarted = False
                else:
                    self.journeyStarted = True















