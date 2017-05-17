import random
import time
from elevatorAI import *
DUR = 100000

passengers = []
tripTimes = []

class Passenger:
	def __init__(self): #waitTime, destination, location, inTheElevator
		self.waitTime = 0
		a = random.randint(1,N)
		if random.randint(0,1):
			self.destination, self.location = a, 0
		else:
			self.destination, self.location = 0, a
		self.inTheElevator = False

def oneIn(n):
	return not random.randint(0,n-1)

def tick():
	if not elevator.direction:
		elevator.waiting = TW
	if elevator.waiting:
		elevator.waiting -= 1
	else:
		elevator.floor += elevator.direction


	for i, passenger in enumerate(passengers):
		passenger.waitTime += 1
		if passenger.inTheElevator:
			passenger.location = elevator.floor
			if elevator.waiting and passenger.destination == elevator.floor:
				tripTimes.append(passenger.waitTime)
				del passengers[i]
		elif elevator.waiting and passenger.location == elevator.floor:
			passenger.inTheElevator = True

	if oneIn(M):
		passengers.append(Passenger())

for ticks in range(DUR):
	elevator.direction = elevator.decide(passengers)
	tick()
	#"""
	time.sleep(.1)
	print "\nELEVATOR: " + str(elevator.floor)
	for passenger in passengers:
		print "Passenger at " + str(passenger.location) + " to "  + str(passenger.destination) + ". In the elevator? " + str(passenger.inTheElevator)
	#"""

print "\nTICKS WAITED: " + str(sum(tripTimes))



