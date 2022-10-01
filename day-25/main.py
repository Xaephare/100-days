import pandas

# data = pandas.read_csv('weather_data.csv')
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data['temp'].to_list()
# print(temp_list)
#
# temp_average = sum(temp_list) / len(temp_list)
# print(temp_average)
# print(data['temp'].max())
# print(data.condition)
# print(data[data.day == 'Monday'])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == 'Monday']
# monday_fahrenheit = monday.temp * 1.8 + 32
# print(monday_fahrenheit)


squirrel_data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
grey_squirrels_count = len(squirrel_data[squirrel_data['Primary Fur Color'] == "Gray"])
red_squirrels_count = len(squirrel_data[squirrel_data['Primary Fur Color'] == "Cinnamon"])
black_squirrels_count = len(squirrel_data[squirrel_data['Primary Fur Color'] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
