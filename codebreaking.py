"""
Playing with game items.
Usage:  codebreaking.py
"""
import sys
def main():
    """Main entry point for the script."""
    print("Starting code break")

    # We think we know
    shark = "1"
    snake = "2"
    seashell = "7"

    # Guessing
    sabre = "8"
    whale = "3"
    mermaid = "4"
    anchor = "5"
    gull = "6"
    lightning = "9"

    # Phillipinnes 12 N / 121 E
    # Latitude: 10-17
    # Longitude: 116 - 129

    latitude = shark + sabre + "." + whale + mermaid + "." + anchor + mermaid + "." + gull
    longitude = shark + snake + mermaid + "." + shark + seashell + "." + shark + sabre + "." + lightning

    print("Guess")
    printlocation(latitude, longitude)

    print("Crunch")
    possibilities = 0
    known = [shark, snake, seashell]
    for saberguess in range(0,7):   # We know this has to be < 8 (the 8 in 180)
        if str(saberguess) not in known:    
            for mermaidguess in range(0,9):
                if str(mermaidguess) not in known and saberguess != mermaidguess:
                    latitude = shark + str(saberguess)
                    longitude = shark + snake + str(mermaidguess)
                    possibilities = possibilities + 1
                    printlocation(latitude,longitude)
    print("Checked " + str(possibilities) + " possibilities")

def printlocation(latitude, longitude):
    print("Latitude: " + latitude)
    print("Longitude: " + longitude)
    print("\n")

if __name__ == '__main__':
    sys.exit(main())