#author: Luca Rospocher
from enum import Enum
class State(Enum):
     FREE = 0
     GOING = 1
     OCCUPIED = 2

class Ride:
    def __init__(self):
        self.startIntersectionRow = 0
        self.startIntersectionCol = 0
        self.finishIntersectionRow = 0
        self.finishIntersectionCol = 0
        self.earliest = 0 #step
        self.latest = 0 #step
        self.timeToPerform = 0 # to eval at beginning
        self.done = False
        pass

class Vehicle:
    def __init__(self):
        self.row = 0
        self.col = 0
        self.state = State.FREE
        self.occupiedFor = 0
        self.ridesList = [] #int[]
        pass

vehicles = []
rides = []

countRows = 0
countColumns = 0
countVehicles = 0
countRides = 0
bonus = 0
steps = 0

def main():   
    fileLines = open('b_should_be_easy.in', 'r').readlines()
    firstLine = fileLines[0]
    splittedFirst = firstLine.split(' ')
    
    countRows = int(splittedFirst[0])
    countColumns = int(splittedFirst[1])
    countVehicles = int(splittedFirst[2])
    countRides = int(splittedFirst[3])
    bonus = int(splittedFirst[4])
    steps = int(splittedFirst[5])
    
    for i in range(countVehicles):
        vehicles.append(Vehicle()) #fill with empty
    
    lineCounter = 1
    for i in range(countRides): #read from file rides features
        endPointLine = fileLines[lineCounter]
        lineCounter += 1
        splittedEndPoint = endPointLine.split(' ')
        
        rides.append(Ride()) #fill with empty
        rides[i].startIntersectionRow = int(splittedEndPoint[0])
        rides[i].startIntersectionCol = int(splittedEndPoint[1])
        rides[i].finishIntersectionRow = int(splittedEndPoint[2])
        rides[i].finishIntersectionCol = int(splittedEndPoint[3])
        rides[i].earliest = int(splittedEndPoint[4])
        rides[i].latest = int(splittedEndPoint[5])
        rides[i].timeToPerform = abs(rides[i].startIntersectionRow - rides[i].finishIntersectionRow) + abs(rides[i].startIntersectionCol - rides[i].finishIntersectionCol)
    
    for step in range(steps): # in each step
        for k in range(countRides): # for each ride
            if ((rides[k].latest - rides[k].timeToPerform) >= step and rides[k].done != True):
                distanceBestVehicle = 10000
                indexBestVehicle = -1
                for j in range(countVehicles): # for each vehicle
                    if(vehicles[j].state != State.FREE):
                        vehicles[j].occupiedFor -= 1
                        if(vehicles[j].occupiedFor == 0):
                            vehicles[j].state = State.FREE
                            #vehicles[j].row = rides[vehicles[j].ridesList[-1]].finishIntersectionRow
                            #vehicles[j].col = rides[vehicles[j].ridesList[-1]].finishIntersectionCol
                    elif (distanceBestVehicle > (abs(vehicles[j].row - rides[k].startIntersectionRow) + abs(vehicles[j].col - rides[k].startIntersectionCol))):
                        distanceBestVehicle = (abs(vehicles[j].row - rides[k].startIntersectionRow) + abs(vehicles[j].col - rides[k].startIntersectionCol))
                        indexBestVehicle = j
                vehicles[indexBestVehicle].ridesList.append(k)
                vehicles[indexBestVehicle].state = State.GOING
                vehicles[indexBestVehicle].row = rides[k].finishIntersectionRow
                vehicles[indexBestVehicle].col = rides[k].finishIntersectionCol

                rides[k].done = True
                #delete ride if and after it has been assigned

    #print result to file
    fileOutput = open('b_should_be_easy.out', 'w')
    for b in range(countVehicles):
        fileOutput.write(str(b + 1) + ' ') 
        for t in range(len(vehicles[b].ridesList)):
            fileOutput.write(str(vehicles[b].ridesList[t]) + ' ')
        fileOutput.write('\n') 
        
if  __name__ =='__main__':
    main()