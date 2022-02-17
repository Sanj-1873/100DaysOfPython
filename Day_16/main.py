# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()
#     print(data)

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         try: 
#             temperatures.append(int(row[1]))
#         except:
#             pass

import pandas 

data = pandas.read_csv("weather_data.csv")
data_dict = data.to_dict()
print(data_dict)
#with pandas 
print(data["temp"].mean())
print(data["temp"].max())


# Traditionally 
temp_list = data["temp"].to_list()
sum = 0 
for temp in temp_list:
    sum = temp + sum 

avg = sum / len(temp_list)
print("avg temp is {}".format(avg))