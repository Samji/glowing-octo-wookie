#coding: utf-8
#cost of current car
#OC = original car

OCpay, OCins, OCtax, OCser, OCmot, OCrep, OCtot = (0, 0, 0, 0, 0, 0, 0)

QOCpay = raw_input('Are you still paying for the purchase of your car? (Y/N)')
if "y" in QOCpay:
    OCpay = int(raw_input('How much do you pay every month? (£) '))

OCpet = int(int(raw_input('\nHow much petrol does your current car use each week?: £'))*4.333)

QOCins = raw_input('\nDo you pay your insurance monthly? (Y/N)' )
if "y" in QOCins:
    OCins = int(raw_input('How much do you pay every month? (£) '))
elif "n" in QOCins:
    OCins = int(int(raw_input('How much do you pay every year? (£) '))/12)
print "That should be around £",OCins," a month"

QOCtax = raw_input('\nDo you pay tax? (Y/N)')
if "y" in QOCtax:
    OCtax = int(int(raw_input('How much do you pay in a year? (£) '))/12)
    print "That should be around £",OCtax," a month"
    
print "\nDuring the last year"
QOCser = raw_input(' 1. Has your car been in for a service? (Y/N)' )
if "y" in QOCser:
    OCser = int(int(raw_input(' How much did it cost? (£)' ))/12)
    print " That should be around £",OCser," a month"

QOCmot = raw_input('\n 2. Has your car been in for an MOT? (Y/N)' )
if "y" in QOCmot:
    OCmot = int(int(raw_input(	' How much did it cost? (£)' ))/12)
    print " That should be around £",OCmot," a month"
    

QOCrep = raw_input('\n 3. Has your car had any repair work? (Y/N)' )
if "y" in QOCrep:
    OCrep = int(int(raw_input(' How much did it/they cost? (£)' ))/12)
    print " That should be around £",OCrep," a month"

OCtot = OCpay + OCpet + OCins + OCtax + OCmot + OCser + OCrep
print "\nAccording to my calculations you are currently paying £",OCtot," a month for your current car"
