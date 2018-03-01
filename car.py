class Car:

    carActive = False
    
    currentLocationX = 0
    currentLocationY = 0

    destinationX = 0
    destinationY = 0 

    def startCar (self, x, y):
        self.destinationX = x
        self.destinationY = y
        self.carActive = True

    def moveCar (self):

        if (currentLocationX != destinationX):
            if (destinationX > currentLocationX):
                self.currentLocationX += 1
                return
            elif (destinationX < currentLocationX):
                self.currentLocationX -= 1
                return
            elif (destinationY > currentLocationY):
                self.currentLocationY += 1
                return
            elif (destinationY < currentLocationY):
                self.currentLocationY -= 1
                return
            if (destinationX == currentLocationX):
                if (destinationY == currentLocationY):
                    self.carActive = False

