temp = int(input("Enter temperature in °C: "))

if temp < 0:
    print("Freezing Cold!")
elif temp <= 20:
    print("Cold Weather.")
elif temp <= 30:
    print("Normal Temperature.")
else:
    print("Too Hot!")
