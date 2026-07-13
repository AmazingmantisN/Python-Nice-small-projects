# import csv


# with open("weather_Data.csv", "r") as f:
#   data = csv.reader(f)
#   temps = []
#   for i in data:
#     if i[1] != "temp":
#       temps.append(int(i[1]))
    
    
# print(temps)


import pandas

data = pandas.read_csv("weather_data.csv")


monday = data[data.day == "Monday"]

print((monday.temp * (9/5)) + 32) 