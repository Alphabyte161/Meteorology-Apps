# MeteoWare
#  Copyright Grace Cohen 2025   
import math
print("                 __                  __      __                           ")
print(" /'\\_/`\\        /\\ \\__              /\\ \\  __/\\ \\                          ")
print("/\\      \\     __\\ \\ ,_\\    __    ___\\ \\ \\/\\ \\ \\ \\     __     _ __    __   ")
print("\\ \\ \\__\\ \\  /'__`\\ \\ \\/  /'__`\\ / __`\\ \\ \\ \\ \\ \\ \\  /'__`\\  /\\`'__\\/\'__`\\ ")
print(" \\ \\ \\_/\\ \\/\\  __/\\ \\ \\_/\\  __//\\ \\L\\ \\ \\ \\_/ \\_\\ \\/\\ \\L\\.\\_\\ \\ \\//\\  __/ ")
print("  \\ \\_\\\\ \\_\\ \\____\\\\ \\__\\ \\____\\ \\____/\\ `\\___x___/\\ \\__/.\\_\\\\ \\_\\\\ \\____\\")
print("   \\/_/ \\/_/\\/____/ \\/__/\\/____/\\/___/  '\\/__//__/  \\/__/\\/_/ \\/_/ \\/____/")
print("\n############################################")
print("####     Copyright Grace Cohen 2025     ####")
print("####       Alphabyte161 on Github       ####")
print("############################################")

# Menu Options 
while True:
    print("\n[1] Heat Index Calculator")
    print("[2] DCP Calculator")
    print("[3] 500mb Jet Translational Speed Calculator")
    menuOption = input("\nEnter number of selection (q to quit): ")
    if menuOption == "q":
        break
    elif menuOption == "1":
        T = int(input("Enter temp in F: "))
        inputRH = int(input("Enter RH in percent: "))

        if inputRH < 40 and T < 80:
            heatIndex = T
        else:
            heatIndex = -42.379 + 2.04901523*T + 10.14333127*inputRH - .22475541*T*inputRH - .00683783*T*T - .05481717*inputRH*inputRH + .00122874*T*T*inputRH + .00085282*T*inputRH*inputRH - .00000199*T*T*inputRH*inputRH
            if inputRH < 13 and 80 <= T <= 112:
                heatIndex += ((13 - inputRH) / 4) * math.sqrt((17 - abs(T - 95)) / 17)
            elif inputRH > 85 and 80 <= T <= 87:
                heatIndex += ((inputRH - 85) / 10) * ((87 - T) / 5)
        if heatIndex > 124:
            print("WARNING: EXTREME HEAT DANGER!")
            print(f"Heat index: {heatIndex:.0f}")
        elif heatIndex > 103:
            print("WARNING: HEAT DANGER")
            print(f"Heat index: {heatIndex:.0f}")
        elif heatIndex > 90:
            print("EXTREME CAUTION")
            print(f"Heat index: {heatIndex:.0f}")
        elif heatIndex > 80:
            print("CAUTION")
            print(f"Heat index: {heatIndex:.0f}")
        else:
            print(f"Heat index: {heatIndex:.0f}")
    elif menuOption == "2":
        dcape = int(input("Enter DCAPE: "))
        mucape = int(input("Enter MUCAPE: "))
        shear6km = int(input("Enter 0-6km shear: "))
        mw6km = int(input("Enter 0-6km mean wind: "))
        dcape /= 980
        mucape /= 2000
        shear6km /= 20
        mw6km /= 16
        DCP = dcape*mucape*shear6km*mw6km
        if DCP > 3:
            print(f"DCP: {DCP:.2f}")
            print("Derecho likely")
        elif DCP > 2:
            print(f"DCP: {DCP}")
            print("Derecho possible")
        else:
            print(f"DCP: {DCP:.2f}")
            print("Derecho unlikely")
    elif menuOption == "3":
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
