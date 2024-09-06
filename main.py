import pandas

# Open csv file in pandas
file = pandas.read_csv("weather_data.csv")

# Dataframe is a table
# A series is a column

# Get data as a dictionary
data_dict = file.to_dict()
# print(data_dict)

# Get series of data
temp_series = file['temp']
temp_series2 = file.temp  # Will get the same result as above
# print(f'{temp_series2} {temp_series}')
temp_list = temp_series.to_list()  # Convert series to list
# print(temp_list)
# print(temp_series.mean())  # You can perform a pandas mean function to average a series
# print(temp_series.max())  # You can perform a pandas max function to get the highest value of series
print(file[file.day == "Monday"])
