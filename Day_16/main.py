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
max_temp = data["temp"].max()

#Get data row 
print("row")
day_with_max_temp = data[data.temp == max_temp]
print(day_with_max_temp)
# Traditionally 
temp_list = data["temp"].to_list()
sum = 0 
for temp in temp_list:
    sum = temp + sum 

avg = sum / len(temp_list)
print("avg temp is {}".format(avg))



monday = data[data.day == "Monday" ]
monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)

# Create a dataframe from scratch 

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores" : [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")