ip = input(" Enter an IP address ")
segmentCount = 1
lengthOfSegment =0
i='' # this initialsation is done for the test case
# when we enter nothing
for i in ip :
    if i == '.' :
        print(" segment {} has {} characters ".format(segmentCount,lengthOfSegment))
        segmentCount = segmentCount +1
        lengthOfSegment =0
    else :
        lengthOfSegment = lengthOfSegment +1

if i != '.':
    print(" segment {} has {} characters ".format(segmentCount,lengthOfSegment))