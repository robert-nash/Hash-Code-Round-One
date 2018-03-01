import ride, car, readFile, router

# --------------------------------------------
# Input File with Rides

inputFile = 'something.txt'

rides = readFile.getRides(inputFile)
parameters = readFile.getParameters(inputFile)

Router = router.Router()

for current_ride in rides:
    if (not current_ride.assigned()):
        Router.assignCar(ride)

# Create rides in for loop
# Store in List

# Loop through each ride, Loop through available cars

