def moveDisk(poles, disk, pole):
    # move disk to pole
    if(disk == 0):
        # base case of recursive algorithm
        return 0, poles

    # find the pole the disk is currently on
    diskIsOn = 0
    if disk in poles[1]:
        diskIsOn = 1
    if disk in poles[2]:
        diskIsOn = 2

    # make list of all disks that need to be moved
    # this could be disks that are on top of the disk, or
    #   are smaller and on the pole we are moving to
    disksToMove = []
    for d in poles[diskIsOn] + poles[pole]:
        if(d<disk):
            disksToMove.insert(0,d)
    disksToMove.sort(reverse=True)

    # we want to move the other disks to the 
    #   remaining pole (not pole and not diskIsOn)
    remainingPole = 0
    if(diskIsOn!=1 and pole!=1):
        remainingPole = 1
    if(diskIsOn!=2 and pole!=2):
        remainingPole = 2

    moves = 0
    while(len(disksToMove) > 0):
        # while there are still disks to move
        newMoves, poles = moveDisk(poles, disksToMove[0], remainingPole)
        moves+=newMoves
        disksToMove.pop(0)
    
    # now we can move the disk we wanted to in the beginning
    poles[diskIsOn].remove(disk)
    poles[pole].insert(0, disk)
    moves += 1
    print(poles)

    return moves, poles

def h(poles):
    moves = 0
    for disk in range(largestDisk, 0, -1):
        # move each disk from largest to smallest onto the final pole
        # first find the pole the disk is on
        diskIsOn = 0
        if disk in poles[1]:
            diskIsOn = 1
        if disk in poles[2]:
            diskIsOn = 2

        if(diskIsOn==0 or diskIsOn==1):
            # the disk is not on the correct pole
            # we must first find which disks we need to move
            disksToMove = []
            for d in poles[diskIsOn]+poles[2]:
                if(d<disk):
                    disksToMove.insert(0,d)
            disksToMove.sort(reverse=True)

            # we will move these extra disks to the remaining pole
            remainingPole = 0 if diskIsOn==1 else 1

            while(len(disksToMove)>0):
                # while there are still disks to move
                newMoves, poles = moveDisk(poles, disksToMove[0], remainingPole)
                moves+=newMoves
                disksToMove.pop(0)
  
            # the smaller tower has been moved so we can move 
            #  the disk we are currently working on
            poles[diskIsOn].remove(disk)
            poles[2].insert(0, disk)
            moves +=1
            print(poles)

    return moves

largestDisk = 3
n = [[1,2,3],[],[]]
print(h(n))