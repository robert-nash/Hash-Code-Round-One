import math

class Router:
    def assignRide(current_ride, carList):
        personX = current_ride.startX
        personY = current_ride.startY
        endX = current_ride.finishX
        endY = current_ride.finishY
        carDistance = -1
        carID = -1
        for current_car in carList:
            if (!(current_car.carActive)):
                carX = current_car.currentLocationX
                carY = current_car.currentLocationY
                pDistance = math.sqrt ((personX-carX)**2 + (personY-carY)**2)
                if (carDistance == -1):
                    carDistance = pDistance
                    carID = current_car.id
                else:
                    if (pDistance<carDistance):
                        carDistance = pDistance
                        carID = current_car.id

        carList[carID].startCar(personX, personY, endX, endY)
