def celcius_to_farenheit(celcius):
    farenheit = (celcius * 9/5) + 32
    return farenheit

file = open("farenheitConversions.txt", "a")

temperatures=[10,-20,-289,100]

for items in temperatures:
    if items > -273.15:
        file.write("%s\n" %(celcius_to_farenheit(items)))

file.close()
