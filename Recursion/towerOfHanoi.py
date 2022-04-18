
def main():
    print("This program will allow the user to provide a number of disks to challenge the computer with to solve the 'Tower of Hanoi'....")
    diskCount = int(input("Provide a positive whole number: "))
    towerPlay(diskCount, "Left", "Right", "Middle")

    
def towerPlay(n, towerStart, towerFinal, towerExtra):
    if n == 1:
        print("Disk " + str(n) + ": " + towerStart + " --> " + towerFinal)
    else:
        towerPlay(n - 1, towerStart, towerExtra, towerFinal)
        print("Disk " + str(n) + ": " + towerStart + " --> " + towerFinal)
        towerPlay(n - 1, towerExtra, towerFinal, towerStart)    

main()


