# calculates 500mb jet translational speed, be sure to use 06z and the 00z outputs
# or else this WILL NOT work
# credit to project OMEGA. Please read the paper for more info.
print("\nPlease select an option for calculation by entering the number associated")
print("[1] Distances")
print("[2] Coordinates")
inputOption = int(input())
if inputOption == 1:
    dist =  float(input("Enter jet translational dist\n"))
    isValid = False
    while not isValid:
        units = input("Enter distance units\n")
        if units == "km":
            spdTran = (dist / 18) / 1.852
            print(spdTran)
            isValid = True
        elif units == "mi":
            spdTran = (dist / 18) / 1.151
            print(spdTran)
            isValid = True
        else:
            print("Please enter valid units\n")
elif inputOption == 2:
    print("THIS NEEDS WORK DUM DUM")
