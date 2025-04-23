import math
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
            print(f"Translational Speed: {spdTran} kts")
            isValid = True
        elif units == "mi":
            spdTran = (dist / 18) / 1.151
            print(f"Translational Speed: {spdTran} kts")
            isValid = True
        else:
            print("Please enter valid units\n")
elif inputOption == 2:
    lat1 = float(input("Enter initial latitude\n"))
    lat1 = math.radians(lat1)
    lon1 = float(input("Enter initial longitude\n"))
    lon1 = math.radians(lon1)
    lat2 = float(input("Enter final latitude\n"))
    lat2 = math.radians(lat2)
    lon2 = float(input("Enter final longitude\n"))
    lon2 = math.radians(lon2)

    delLat = lat2 - lat1
    delLon = lon2 - lon1

    sinLat = math.sin(delLat/2)
    sinLon = math.sin(delLon/2)
    coordDist = 12742 * (math.asin (math.sqrt((sinLat*sinLat) + (math.cos(lat1)) * (math.cos(lat2)) * (sinLon * sinLon))))
    spdTran = (coordDist / 18) / 1.852
    print(f"Translational Speed: {spdTran:.2f} kts")