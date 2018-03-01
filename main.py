import ride, car, readFile

# --------------------------------------------
# Input File with Rides

inputFile = 'something.txt'

rides = readFile.getRides(inputFile)
parameters = readFile.getParameters(inputFile)

for ride in rides:
    if (ride.assigned() == False):
        assignCar(ride)
        
# Create rides in for loop
# Store in List

# Loop through each ride, Loop through available cars

assignCar(ride):
    
