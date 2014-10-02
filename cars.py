#coding: utf-8
#cost of current car
#OC = original car

OCpay, OCins, OCtax, OCser, OCmot, OCrep, OCtot = (0, 0, 0, 0, 0, 0, 0)

QOCpay = raw_input('Are you still paying for the purchase of your car? (Y/N)')
if "y" in QOCpay:
    OCpay = raw_input('How much do you pay every month? (£) ')

print
OCpet = raw_input('How much petrol does your current car use each week?: £')*4.333
print
OCins = raw_input('Do you pay your insurance monthly? (Y/N)' )
if "y" in OCins:
    OCins = int(raw_input('How much do you pay every month? (£) '))
elif "n" in OCins:
    OCins = (int(int(raw_input('How much do you pay every year? (£) ')))/12)
print "That should be around £",OCins," a month"
print
##OCtax = raw_input('Do you pay tax? (Y/N)')
##if "y" in OCtax:
##    OCtax = (int(int(raw_input('How much do you pay in a year? (£) ')))/12)
##    print "That should be around £",OCtax," a month"
##elif "n" in OCtax:
##    OCtax = int(0)
##print
##print "During the last year"
##OCser = raw_input(' 1. Has your car been in for a service? (Y/N)' )
##if "y" in OCser:
##    OCser = (int(int(raw_input(' How much did it cost? (£)' )))/12)
##    print " That should be around £",OCser," a month"
##elif "n" in OCser:
##    OCser = int(0)
##print
##OCmot = raw_input(' 2. Has your car been in for an MOT? (Y/N)' )
##if "y" in OCmot:
##    OCmot = (int(int(raw_input(	' How much did it cost? (£)' )))/12)
##    print " That should be around £",OCmot," a month"
##elif "n" in OCmot:
##    OCmot = int(0)
##print
##OCrep = raw_input(' 3. Has your car had any repair work? (Y/N)' )
##if "y" in OCrep:
##    OCrep = (int(int(raw_input(' How much did it/they cost? (£)' )))/12)
##    print " That should be around £",OCrep," a month"
##elif "n" in OCrep:
##    OCrep = int(0)
##print
##OCtot = OCpay + OCpet + OCins + OCtax + OCmot + OCser + OCrep
##print "According to my calculations you are currently paying £",OCtot," a month for your current car"
