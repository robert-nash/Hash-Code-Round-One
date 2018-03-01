import ride, car, readFile, router

# --------------------------------------------
# Input File with Rides

inputFile = 'something.txt'

rides = readFile.getRides(inputFile)
parameters = readFile.getParameters(inputFile)

Router = router.Router()

carList = []

for i in range (parameters["vehicles"]):
    carList.append (car.Car(i))


for j in range (parameters["steps"]):

    for current_car in carList:
        if (current_car.carActive):
            current_car.moveCar()

    for current_ride in rides:
        if (not current_ride.assigned()):
            Router.assignCar(current_ride, carList)

for vehicle in carList:
    print (current_car.currentLocationX)
    print (current_car.currentLocationY)
    print ("")

# Create rides in for loop
# Store in List

# Loop through each ride, Loop through available cars
