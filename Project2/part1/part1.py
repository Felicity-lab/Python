import json
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees and celcius symbols.
    
    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and 'degrees celcius.'
    """
        
    # print(f"temperature is {temp}{DEGREE_SYBMOL}")
    return f"{temp}{DEGREE_SYBMOL}"

def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.
    
    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year
    """
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime('%A %d %B %Y')


def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius

    Args:
        temp_in_farenheit: integer representing a temperature.
    Returns:
        An integer representing a temperature in degrees celcius.
    """
    temp_in_celcius = (temp_in_farenheit - 32) * 5/9
    mytemp = "%.1f" % temp_in_celcius
    mytemp = float(mytemp)
    return mytemp

    


def calculate_mean(sum_min_temp, num_items):
    """Calculates the mean.
    
    Args:
        total: integer representing the sum of the numbers.
        num_items: integer representing the number of items counted.
    Returns:
        An integer representing the mean of the numbers.
    """
    mean = sum_min_temp/num_items
    mean = "%.1f" % mean
    mean = float(mean)
    return mean
    

def get_data(filename):
    with open(filename) as f:
        return json.load(f)
    
class Forecast:
    def __init__(self, filename):
        # Initialise variables
        self.forecast_dict = dict()
        self.dates = []
        self.min_temps = []
        self.max_temps = []
        self.day_description = []
        self.night_description = []
        self.day_rain_chance = []
        self.night_rain_chance = []
        self.min_real_feel = []
        self.min_real_feel_shade = []
        self.min_temp_index = 0
        self.max_temp_index = 0

        # Getting data from file
        self.data = get_data(filename)
        self.forecast_dict = self.data['DailyForecasts']

        for forcast in self.forecast_dict:
            self.dates.append(convert_date(forcast['Date']))       # Dates
            self.min_temps.append(convert_f_to_c(forcast['Temperature']['Minimum']['Value']))    # Minimum Temperatures
            self.max_temps.append(convert_f_to_c(forcast['Temperature']['Maximum']['Value']))    # Maximum Temperatures
            self.day_description.append(forcast['Day']['LongPhrase'])
            self.night_description.append(forcast['Night']['LongPhrase'])
            self.day_rain_chance.append(forcast['Day']['RainProbability'])
            self.night_rain_chance.append(forcast['Night']['RainProbability'])
            self.min_real_feel.append(convert_f_to_c(forcast['RealFeelTemperature']['Minimum']['Value']))
            self.min_real_feel_shade.append(convert_f_to_c(forcast['RealFeelTemperatureShade']['Minimum']['Value']))
            self.min_index = self.min_temps.index(min(self.min_temps))
            self.max_index = self.max_temps.index(max(self.max_temps))
 
    


def process_weather(forecast_file):
    """Converts raw weather data into meaningful text.

    Args:
        forecast_file: A string representing the file path to a file
            containing raw weather data.
    Returns:
        A string containing the processed and formatted weather data.
    """
    
    # with open(forecast_file ) as json_data:
    #     my_data = json.load(json_data)
 
    forecast = Forecast(forecast_file)

    output_string = str(len(forecast.dates)) + " Day Overview\n"
    output_string += "    The lowest temperature will be " + format_temperature(forecast.min_temps[forecast.min_index])
    output_string += ", and will occur on " + forecast.dates[forecast.min_index] + ".\n"
    output_string += "    The highest temperature will be " + format_temperature(forecast.max_temps[forecast.max_index])
    output_string += ", and will occur on " + forecast.dates[forecast.max_index] + ".\n"
    output_string += "    The average low this week is " + format_temperature(calculate_mean(sum(forecast.min_temps), len(forecast.min_temps))) + ".\n"
    output_string += "    The average high this week is " + format_temperature(calculate_mean(sum(forecast.max_temps), len(forecast.max_temps))) + ".\n"
    
    for index in range(len(forecast.dates)):
        min_temp_celcius = format_temperature(forecast.min_temps[index])
        max_temp_celcius = format_temperature(forecast.max_temps[index])
        output_string += "\n-------- " + forecast.dates[index] + " --------\n"
        output_string += "Minimum Temperature: " + min_temp_celcius + "\n"
        output_string += "Maximum Temperature: " + max_temp_celcius + "\n"
        output_string += "Daytime: " + forecast.day_description[index] + "\n"
        output_string += "    Chance of rain:  " + str(forecast.day_rain_chance[index]) + "%\n"
        output_string += "Nighttime: " + forecast.night_description[index] + "\n"
        output_string += "    Chance of rain:  " + str(forecast.night_rain_chance[index]) + "%\n"

    output_string += "\n"

    return output_string


    
if __name__ == "__main__":
    print(process_weather("data/forecast_5days_a.json"))





