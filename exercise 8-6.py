numlist = list()
while True:
    inp = raw_input('Enter a number: ')
    if inp == 'done' : break 
    if inp == '5' : print 'HIGH 5!' 
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print "The average of your numbers is", average