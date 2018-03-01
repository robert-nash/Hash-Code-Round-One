import math

class Router:
    def assignCar(self,current_ride, carList):
        personX = current_ride.startX
        personY = current_ride.startY
        endX = current_ride.finishX
        endY = current_ride.finishY
        carDistance = -1
        carID = -1
        for current_car in carList:
            print('loop' + str(current_car.id))
            if (not current_car.carActive):
                print('car active')
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

        if carID > -1:
            print("car started")
            carList[carID].startCar(personX, personY, endX, endY,carID)
            current_ride.assignCar(carID)
