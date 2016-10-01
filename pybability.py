print "PROBABILITY"

events = float(input("Please enter the number of events: "))
outcomes = float(input("Please enter the total number of possible outcomes: "))

def calcpropability(events,outcomes):
	print "Calculating Probability"
	prob = float

	print type(events)
	print type(outcomes)
	print type(prob)

	prob = events / outcomes
	print "Events (" + str(events) + ") / Outcomes (" + str(outcomes) + ")"
	print "="
	print type(prob)


	return prob

print calcpropability(events,outcomes)

