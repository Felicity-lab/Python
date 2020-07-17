import json
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

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

    
def get_data(filename):
    with open(filename) as f:
        return json.load(f)


class Historic:

    def __init__(self, filename):
        self.temperatures = []                
        self.min_temps = []
        self.max_temps = []
        self.max_temp = 0                     
        self.min_temp = 1000                    
        self.total_precipitation = 0          
        self.precipitation_readings = 0       
        self.daylight_hours = 0               
        self.max_uv = 0                       
        self.max_uv_time = ""                   
        self.weather_text_dictionary = dict()  
        self.weather_text_categories = []     
        self.weather_text_occurances = []     

        self.historic_data = get_data(filename)


        for reading in self.historic_data:
            # Getting temperature for each reading
            temp = reading["Temperature"]["Metric"]["Value"]
            if (temp > self.max_temp):      # If the temperature for the reading is more than the maximum set the maximum to this temperature
                self.max_temp = temp
            elif (temp < self.min_temp):    # If the temperature for the reading is less than the minimum set the minimum to this temperature
                self.min_temp = temp
            self.temperatures.append(temp)

            uv = reading["UVIndex"]
            if uv > self.max_uv:            # If the uv index for the reading is more than the maximum set the maximum to this uv index
                self.max_uv = uv
                self.max_uv_time = reading["LocalObservationDateTime"]

            # Weather text
            weather_text = reading["WeatherText"]       
            if weather_text in self.weather_text_dictionary:
                self.weather_text_dictionary[weather_text] += 1
            else:
                self.weather_text_dictionary[weather_text] = 1

            # If this reading recorded precipitation add 1 to the number of precipitation readings and add the precipitation to the total
            if reading["HasPrecipitation"]: 
                self.precipitation_readings += 1
                self.total_precipitation += reading["PrecipitationSummary"]["Precipitation"]["Metric"]["Value"]
            
            if reading["IsDayTime"]:
                self.daylight_hours += 1

        # Weather text
        for category in self.weather_text_dictionary:
            self.weather_text_categories.append(category)
            self.weather_text_occurances.append(self.weather_text_dictionary[category])


data = Historic("data/historical_24hours_a.json")


# Box plot (No min/max temperature data for each hours so will just do one box plot for temperature)
df = pd.DataFrame(dict(
    linear=data.temperatures
)).melt(var_name="quartilemethod")
fig = px.box(df, y="value", title="Temperatures")
fig.show()


# Bar chart
fig2 = go.Figure([go.Bar(x=data.weather_text_categories, y=data.weather_text_occurances)])
fig2.update_layout(title_text='Weather Text Categories')
fig2.show()


# Summary
output_string = "----- " + str(len(data.temperatures)) + "Hr Summary -----\n\n"
output_string += "Minimum Temperature: " + format_temperature(data.min_temp) + ".\n"
output_string += "Maximum Temperature: " + format_temperature(data.max_temp) + ".\n"
output_string += "Total Precipitation: " + str(data.total_precipitation) + "mm.\n"
output_string += "Precipitation was recorded for: " + str(data.precipitation_readings) + " hours.\n"
output_string += str(data.daylight_hours) + " hours of daylight.\n"
output_string += "The maximum UV index was: " + str(data.max_uv) + " which occured at " + data.max_uv_time + ".\n"

print(output_string)