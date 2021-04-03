import pandas as pd
import os
import matplotlib.pyplot as plt

def process_file():
    cwd = os.getcwd()
    json = pd.read_json("https://api.covid19api.com/country/singapore/status/confirmed?from=2020-04-01T00:00:00Z&to=2020-05-01T00:00:00Z")
    json['Dateonly'] = pd.to_datetime(json['Date']).apply(lambda x: x.date())
    plt.xticks(rotation=90)
    plt.plot(json['Dateonly'],json['Cases'])
    if os.path.exists(cwd + "\\section4output\Singapore_covid_trend.png"):
        os.remove(cwd + "\\section4output\Singapore_covid_trend.png")
    plt.savefig(cwd + "\\section4output\Singapore_covid_trend.png")

if __name__ == '__main__':
    process_file()