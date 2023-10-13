import datetime, random

def getBirthdays(numberOfBirthdays):
    # returns a list of number of random date objects for birthdays
    birthdays = []
    for i in range(numberOfBirthdays):
        # The year is unimportant for our simulation, as long as all 
        # birthdays have the sameyear 
        
        startOfYear = datetime.date(2001,1,1)
        
        # Get a random day into the year

        randomNumberOfDays = datetime.timedelta(random.randint(0,364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)

    return birthdays

def getMatch(birthdays):
    # returns the date object of a birthday that occurs more than once in the birthdays list.

    if len(birthdays) == len(set(birthdays)):
        return None #all birthdays are unique, so return none

    # compare each birthday to every other birthday

    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a+1:]):
            if birthdayA == birthdayB:
                return birthdayA #return the matching birthday. 

# the birthday paradox shows us that in a group of N people, the chances of two people having the same birthday is surprisingly high.
# we will run Monte Carlo simulation (that is, repeated random simulations)to explore this concept.
# it's not really a paradox, it's just a surprising result.

MONTHS = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')

while True: #keep asking until the users enter a valid amount.
    print("How many birthdays should i generate?Max(100)" )
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break #user has entered a valid amount.

print()

#Generate and display the birthdays:

#Generate and display the birthdays:
print("Here are",numBDays,'birthdays:')
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i!=0:
        #Display a comma for each birthday after the first birthday.
        print(', ', end='')
        monthName = MONTHS[birthday.month - 1]
        datetext = '{} {}'.format(monthName,birthday.day)
        print(datetext,end='')

print()
print()

#Determine if there are two birthdays that match.

match = getMatch(birthdays)

#display the results:

print('In this simulation, ',end='')
# the 'end' argument helps you to specify what to print at the end. 
if match != None:
    monthName = MONTHS[match.month-1]
    datetext = '{} {}'.format(monthName,match.day)
    print('multiple people have a birthday on',datetext)
else:
    print("There are no matching birthdays.")

print()

# Run through 100,000 simulations:
print('Generating',numBDays,'random birthdays 100,000 times....')
input("Press Enter to begin...")

print("Let's run another 100,000 simulations.")
simMatch = 0 #How many simulations had matching birthdays in them.and
for i in range(100_000):
    # Report on the progress every 10,000 simulations:
    if i%10_000 == 0:
        print(i,"simulations run...")
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) != None:
        simMatch += 1
print("100,000 simulations run.")

#display simulation results
probability = round(simMatch/100_000*100,2)
print('Out of 100,000 simulations of',numBDays,'people there was a matching birthday in that group',simMatch,'times.This means that',numBDays,'people have a',probability,'% chance of having a birthday in their group.')

print("That's probably more than you would think.")
