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

for car in carList:
    if (car.carActive):
        car.moveCar()

for current_ride in rides:
    if (not current_ride.assigned()):
        Router.assignCar(current_ride, carList)

# Create rides in for loop
# Store in List

# Loop through each ride, Loop through available cars
