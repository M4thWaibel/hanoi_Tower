#n -> number of disks
#origin -> location of origin of discs
#aux -> Auxiliary place to move the discs
#destination -> Final destination location of discs

def hanoi(n, origin, destination, aux):
    if n == 0:
        return
    hanoi(n-1, origin, aux, destination)
    #Moves disk 'n' from 'source' to 'destination' and prints the towers result
    print(f"Move disc {n} from {origin} to {destination}")
    #Move 'n-1s' from the 'auxiliary' tower to the 'final' tower using the 'origin' tower as an auxiliary
    hanoi(n-1, aux, destination, origin)


n = int(input("Enter the disc number to be uses in the Hanoi Tower: "))
hanoi(n, 'Source', 'auxiliary', 'Destination')