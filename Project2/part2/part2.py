import json
import plotly.express as px
import plotly.graph_objects as go


from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees and celcius symbols.
    
    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and 'degrees celcius.'
    """
    # temp = str()
    
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
 

# Getting forecast data
forecast = Forecast("data/forecast_5days_a.json")


# First figure
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=forecast.dates,
    y=forecast.min_temps,
    name = 'Minimum',
))
fig.add_trace(go.Scatter(
    x=forecast.dates,
    y=forecast.max_temps,
    name='Maximum',
))

fig.update_layout(title_text='Minimum and Maximum Temperatures')
fig.show()

# Second figure
fig2 = go.Figure()

fig2.add_trace(go.Scatter(
    x=forecast.dates,
    y=forecast.min_temps,
    name = 'Minimum', 
))
fig2.add_trace(go.Scatter(
    x=forecast.dates,
    y=forecast.min_real_feel,
    name='Minimum Real Feel',
))
fig2.add_trace(go.Scatter(
    x=forecast.dates,
    y=forecast.min_real_feel_shade,
    name='Minimum Real Feel Shade',
))
fig2.update_layout(title_text='Minimum Temperatures')
fig2.show()
