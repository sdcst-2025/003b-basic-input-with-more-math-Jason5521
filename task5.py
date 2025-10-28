#

#A population can be modeled by the following:
#future population = (current population)*(1+r)^(time in years) 
#Have the user enter the current population, the rate of growth as a decimal and the number of DAYS.
#Calculate the expected future population

#Enter the population: 25000000
#Enter the rate of growth in percent: 2.1
#Enter the number of days: 12
#There will be 25017087 people after 12 days
currentPeople = float(input("enter the current population."))
growthRate = float(input("enter the rate of growth."))
Days = float(input("enter the number of days."))

futurePeople = currentPeople * (1 + (growthRate / 100)) ** (Days / 365)
futurePeople = round(futurePeople,0)
print (f"there will be {futurePeople} after {Days} days.")
