def celcius_to_degrees(celcius):
    farenheit = (celcius * 9/5) + 32
    return farenheit

"""reading = input("Please input celcius: ")
reading = int(reading)

if reading > -273.15:
    print ("%s Celcius = %s farenheit" %(reading, celcius_to_degrees(reading)))

else:
    print("Little bit too chilly that is")"""

temperatures=[10,-20,-289,100]

for items in temperatures:
    if items > -273.15:
        print(celcius_to_degrees(items))
    else:
        print("Little bit too chilly that is")
