import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit (1880–2050)
    res_all = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    years_all = pd.Series(range(1880, 2051))
    sea_level_all = res_all.intercept + res_all.slope * years_all
    plt.plot(years_all, sea_level_all, color="red")

    # Create second line of best fit (2000–2050)
    df_recent = df[df["Year"] >= 2000]
    res_recent = linregress(
        df_recent["Year"],
        df_recent["CSIRO Adjusted Sea Level"]
    )
    years_recent = pd.Series(range(2000, 2051))
    sea_level_recent = res_recent.intercept + res_recent.slope * years_recent
    plt.plot(years_recent, sea_level_recent, color="green")

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
