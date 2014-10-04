#coding: utf-8
#cost of current car
#OC = original car

OCpay, OCins, OCtax, OCser, OCmot, OCrep, OCtot = (0, 0, 0, 0, 0, 0, 0)
ynValid = 'YN' #the characters required for any branching questions

def checkinput(question, requiredAns):
    '''A function that asks a specific question that requires
        a limited answer
    :param question: the question to be asked
    :param requiredAns: a string of valid answers, anything else is DENIED
    :return: the correct response from the user
    '''
    print question,
    resp = raw_input()
    while resp.lower() not in requiredAns.lower():
        print "Your answer is INVALID!!! Y or N!!!!!!!!!!! try again"
        print question,
        resp = raw_input()
    else:
        return resp.lower()
        

QOCpay = checkinput('\nAre you still paying for the purchase of your car? (Y/N)',ynValid)
if QOCpay == 'y':
    OCpay = int(raw_input('How much do you pay every month? (£) '))

OCpet = int(int(raw_input('\nHow much petrol does your current car use each week?: £ '))*4.333)

QOCins = checkinput('\nDo you pay your insurance monthly? (Y/N)',ynValid)
if QOCins == 'y':
    OCins = int(raw_input('How much do you pay every month? (£) '))
else:
    OCins = int(int(raw_input('How much do you pay every year? (£) '))/12)
print "That should be around £",OCins," a month"

QOCtax = checkinput('\nDo you pay tax? (Y/N)',ynValid)
if QOCtax == 'y':
    OCtax = int(int(raw_input('How much do you pay in a year? (£) '))/12)
    print "That should be around £",OCtax," a month"

print "\nDuring the last year"
QOCser = checkinput(' 1. Has your car been in for a service? (Y/N)',ynValid)
if QOCser == 'y':
    OCser = int(int(raw_input(' How much did it cost? (£)' ))/12)
    print " That should be around £",OCser," a month"

QOCmot = checkinput('\n 2. Has your car been in for an MOT? (Y/N)',ynValid)
if QOCmot == 'y':
    OCmot = int(int(raw_input(	' How much did it cost? (£)' ))/12)
    print " That should be around £",OCmot," a month"

QOCrep = checkinput('\n 3. Has your car had any repair work? (Y/N)',ynValid)
if QOCrep == 'y':
    OCrep = int(int(raw_input(' How much did it/they cost? (£)' ))/12)
    print " That should be around £",OCrep," a month"


OCtot = OCpay + OCpet + OCins + OCtax + OCmot + OCser + OCrep
print "\nAccording to my calculations you are currently paying £",OCtot," a month for your current car"
