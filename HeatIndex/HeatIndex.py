# Heat index calculator
# have fun 
# copyright Grace Cohen 2025
import math
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
