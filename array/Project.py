# Find Number of days above Average Temperature
totalDay = int(input("How many day's temperature?"))
total = 0
temp = []

for i in range(totalDay):
    temperature = int(input(f"Day {i+1}'s high temperature: "))
    temp.append(temperature)
    total += temperature

ave = round(total/totalDay,2)
print(f"\nAverage = {ave}" )

above = 0
for i in temp:
    if i > ave:
        above += 1

print(str(above) + "day(s) above average")
