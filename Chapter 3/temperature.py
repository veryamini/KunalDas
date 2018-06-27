fahrenheit = 0.0
print ("Fahrenheit Celsius")
while fahrenheit <= 250:
    celsius = (fahrenheit - 32.0 ) / 1.8 #Calculated celsius value
    print ("%1.1f  %7.2f" % (fahrenheit, celsius))
    fahrenheit = fahrenheit + 25
