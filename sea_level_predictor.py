import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    data = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10, 5))
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'], color='blue', label='Data')

    # Create first line of best fit
    slope, intercept, _, _, _ = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series(range(1880, 2051))
    plt.plot(years_extended, intercept + slope * years_extended, 'r', label='Fit: All Data')

    # Create second line of best fit from 2000 onwards
    data_2000_onwards = data[data['Year'] >= 2000]
    slope_new, intercept_new, _, _, _ = linregress(data_2000_onwards['Year'], data_2000_onwards['CSIRO Adjusted Sea Level'])
    years_2000_to_2050 = pd.Series(range(2000, 2051))
    plt.plot(years_2000_to_2050, intercept_new + slope_new * years_2000_to_2050, 'green', label='Fit: 2000-2050')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
