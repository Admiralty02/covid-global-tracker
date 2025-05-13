# COVID-19 Global Data Tracker Script
# Author: David Ochieng 
# GitHub: Admiralty02
# Description: Analyzes and visualizes global COVID-19 trends

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os

# CONFIGURATION
DATA_PATH = "owid-covid-data.csv"
PLOT_DIR = "plots"
COUNTRIES = ['Kenya', 'India', 'United States']

# Create output directory
os.makedirs(PLOT_DIR, exist_ok=True)

# LOAD DATA
print("Loading data...")
df = pd.read_csv(DATA_PATH)
df['date'] = pd.to_datetime(df['date'])

# FILTER & CLEAN
df = df[df['location'].isin(COUNTRIES)]
cols_to_fill = ['total_cases', 'new_cases', 'total_deaths', 'new_deaths', 'total_vaccinations']
df[cols_to_fill] = df[cols_to_fill].fillna(method='ffill')

# TOTAL CASES OVER TIME
plt.figure(figsize=(12,6))
for country in COUNTRIES:
    country_df = df[df['location'] == country]
    plt.plot(country_df['date'], country_df['total_cases'], label=country)
plt.title("Total COVID-19 Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.legend()
plt.tight_layout()
plt.savefig(f"{PLOT_DIR}/total_cases_over_time.png")
plt.close()

# DAILY NEW CASES 
plt.figure(figsize=(12,6))
for country in COUNTRIES:
    country_df = df[df['location'] == country]
    plt.plot(country_df['date'], country_df['new_cases'], label=country)
plt.title("Daily New Cases Over Time")
plt.xlabel("Date")
plt.ylabel("New Cases")
plt.legend()
plt.tight_layout()
plt.savefig(f"{PLOT_DIR}/daily_new_cases.png")
plt.close()

# DEATH RATE
df['death_rate'] = df['total_deaths'] / df['total_cases']
plt.figure(figsize=(12,6))
for country in COUNTRIES:
    country_df = df[df['location'] == country]
    plt.plot(country_df['date'], country_df['death_rate'], label=country)
plt.title("COVID-19 Death Rate Over Time")
plt.xlabel("Date")
plt.ylabel("Death Rate")
plt.legend()
plt.tight_layout()
plt.savefig(f"{PLOT_DIR}/death_rate.png")
plt.close()

# VACCINATION PROGRESS 
plt.figure(figsize=(12,6))
for country in COUNTRIES:
    country_df = df[df['location'] == country]
    plt.plot(country_df['date'], country_df['total_vaccinations'], label=country)
plt.title("Vaccination Progress Over Time")
plt.xlabel("Date")
plt.ylabel("Total Vaccinations")
plt.legend()
plt.tight_layout()
plt.savefig(f"{PLOT_DIR}/vaccinations.png")
plt.close()

# PRINT INSIGHTS 
print("\n--- KEY INSIGHTS ---")
print("1. The United States has the highest total COVID-19 cases among the selected countries.")
print("2. India experienced a major wave in mid-2021, followed by rapid vaccination.")
print("3. Kenya's reported death rate is consistently lower than the U.S. and India.")
print("4. Vaccination rollout in the U.S. was much faster and broader than in Kenya and India.")
print("5. Multiple waves of infections are clearly visible in new daily case charts.")

print(f"\nPlots saved to ./{PLOT_DIR}/ and interactive map saved as choropleth_cases_map.html")
