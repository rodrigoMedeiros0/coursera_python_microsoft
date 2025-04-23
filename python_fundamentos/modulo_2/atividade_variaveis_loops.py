celsius_temprtures = [0, 10, 25, 30, 32, 100]
fahrenheit_temperatures = []

for celsius in celsius_temprtures:
    fahrenheit = (celsius * 9/5) + 32
    fahrenheit_temperatures.append(fahrenheit)

print("Celsius temperatures:", celsius_temprtures)
print("Fahrenheit temperatures:", fahrenheit_temperatures)