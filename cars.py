#coding: utf-8
#cost of current car
#OC = original car

OCpay, OCins, OCtax, OCser, OCmot, OCrep, OCtot = (0, 0, 0, 0, 0, 0, 0)
ynValid = 'YN' #the characters required for any branching questions

def checkinput(question, requiredAns):
    """A function that asks a specific question that requires
        a limited answer
    :param question: the question to be asked
    :param requiredAns: a string of valid answers, anything else is DENIED
    :return: the correct response from the user
    """
    print question,
    resp = raw_input()
    while resp.lower() not in requiredAns.lower():
        print "Your answer is INVALID!!! Y or N!!!!!!!!!!! try again"
        print question,
        resp = raw_input()
    else:
        return resp.lower()

def monthlyOutput(QOCsection):
    """A function to request a monetary amount that is spent in a month
    :param: QOCsection: the subject in question
    """
    if QOCsection == 'y':
        resp = int(raw_input('How much do you pay every month? (£) '))
        return resp

def oneOff(QOCsection):
    """A function to request a monetary amount that was spent in one go
    :param: QOCsection: the subject in question
    """
    if QOCsection == 'y':
        resp = int(int(raw_input(' How much did it cost? (£)' ))/12)
        return resp
    else:
        return (0)

def eitherOutput(QOCsection):
    """A function to request a monetary amount that is spent in a month or a year
    :param: QOCsection: the subject in question
    """
    if QOCsection == 'y':
        resp = int(raw_input('How much do you pay every month? (£) '))
    
    else:
        resp = int(int(raw_input('How much do you pay every year? (£) '))/12)
        print "That should be around £",resp," a month"
        
    return resp

QOCpay = checkinput('\nAre you still paying for the purchase of your car? (Y/N)',ynValid)
OCpay = monthlyOutput(QOCpay)

OCpet = int(int(raw_input('\nHow much petrol does your current car use each week?: £ '))*4.333)

QOCins = checkinput('\nDo you pay your insurance monthly? (Y/N)',ynValid)
OCins = eitherOutput(QOCins)

QOCtax = checkinput('\nDo you pay tax? (Y/N)',ynValid)
if QOCtax == 'y':
    OCtax = oneOff(QOCtax)

print "\nDuring the last year"
QOCser = checkinput(' 1. Has your car been in for a service? (Y/N)',ynValid)
OCser = oneOff(QOCser)

QOCmot = checkinput('\n 2. Has your car been in for an MOT? (Y/N)',ynValid)
OCmot = oneOff(QOCmot)

QOCrep = checkinput('\n 3. Has your car had any repair work? (Y/N)',ynValid)
OCrep = oneOff(QOCrep)

OCtot = OCpay + OCpet + OCins + OCtax + OCmot + OCser + OCrep
print "\nAccording to my calculations you are currently paying £",OCtot," a month for your current car"
