import csv
import os
import pandas as pd

# cities_csv = os.path.join("..", "Resources", "assets", "cities.csv")
# with open(cities_csv_path, newline="") as csvfile:
#     csv_reader = csv.reader(csvfile, delimiter=",")

# df = pd.read_csv(file, encoding="ISO-8859-1")


cities_csv = "Resources/cities.csv"
cities_df = pd.read_csv(cities_csv)
cities_df.head()

html = cities_df.to_html()
W_data = open("weather_data.html", "w")
W_data.write(html)
W_data.close()

os.getcwd()


