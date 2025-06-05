# Derecho Composite Parameter Calculator
# Copyright Grace Cohen 2025
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
else:
    print(f"DCP: {DCP:.2f}")
    print("Derecho unlikely")
