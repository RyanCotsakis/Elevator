N = 20 #Number of floors above ground (ground is 0)
TW = 5 #number of ticks that the elevator spends waiting
M = 20 #inverse probability of a new person wanting to use the elevator

class Elevator:
	def __init__(self, initFloor):
		self.floor = initFloor
		self.direction = 0
		self.waiting = 0

	def goTowards(self, level):
		if self.floor < level:
			return 1
		elif self.floor > level:
			return -1
		else: return 0

	def decide(self, passengers):
		#determine highest and lowest floors
		if len(passengers):
			highestWaiter = 0
			highestDest = 0
			lowestWaiter = N
			lowestDest = N
			leaveHere = False
			enterHere = False
			for passenger in passengers:
				if not passenger.inTheElevator:
					if passenger.location > highestWaiter:
						highestWaiter = passenger.location
					if passenger.location < lowestWaiter:
						lowestWaiter = passenger.location
					if passenger.location == self.floor:
						enterHere = True
				else:
					if passenger.destination < lowestDest:
						lowestDest = passenger.destination
					if passenger.destination > highestDest:
						highestDest = passenger.destination
					if passenger.destination == self.floor:
						leaveHere = True

			lowest = min(lowestDest,lowestWaiter)
			highest = max(highestDest,highestWaiter)

			#do something
			if leaveHere:
				return 0
			if self.direction < 0:
				if enterHere:
					return 0
				else:
					return self.goTowards(lowest)
			elif self.direction > 0:
				return self.goTowards(highest)
			else:
				if self.floor == 0:
					return self.goTowards(highest)
				elif self.floor == N:
					return self.goTowards(lowest)

				elif self.floor < N/2:
					return self.goTowards(lowest)
				else:
					return self.goTowards(highest)

		else:
			return self.goTowards(0)

elevator = Elevator(0)

# Returns elevatorDirection. 1 is up, -1 is down, 0 is wait
	