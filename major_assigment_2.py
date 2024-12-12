"""
#Major Assignment 2
# Define 10 Stocks, randomly generate their price (range from 1000 to 10000)
# Write to csv file using python csv module

# Read that csv file using pandas
# Add new column to that data frame which says if we can buy this stock(use whatever you logic you want)
# export to output.csv

# stocks = [
#     {"name":"NHCL","price":randint(100,10000)},
#     {"name":"NHCL","price":randint(100,10000)},
#     {"name":"NHCL","price":randint(100,10000)},
#     {"name":"NHCL","price":randint(100,10000)},
#     ......
#     {"name":"NHCL","price":randint(100,10000)} # 10s

# ]
# csv.DictWrite() -> stocks.csv file save......

# Using pandas read pd.read_csv('stocks.csv')
# df['Can Buy'] = Logic
# df.to_csv('csv_file.csv')

# Optional : Push this code along with output.csv and stocks.csv to github(make your repo public)
# and send me a link
#Highly Encouraged : Uses of lambda or classes would be highly encouraged
"""


#importing the necessary packages, modules, classes
import os 
import csv
from random import randint
import pandas as pd

#list of dictionaries that stores the name and prices of different stocks
stocks = [
    {"Name" : "Apple Inc. (AAPL)", "Price" : randint(100,10000)},
    {"Name" : "Microsoft Corporation", "Price" : randint(100,10000)},
    {"Name" : "Amazon.com Inc.", "Price" : randint(100,10000)},
    {"Name" : "Tesla Inc.", "Price" : randint(100,10000)},
    {"Name" : "Alphabet Inc.", "Price" : randint(100,10000)},
    {"Name" : "Meta Platforms Inc.", "Price" : randint(100,10000)},
    {"Name" : "Johnson & Johnson", "Price" : randint(100,10000)},
    {"Name" : "Berkshire Hathaway Inc.", "Price" : randint(100,10000)},
    {"Name" : "Procter & Gamble Co.", "Price" : randint(100,10000)},
    ]

print(stocks)

#folder where the csv file will be created
folder_path = "D:\Python\BRAODWAY\class_18\class_18_assignments\Major Assignment 2\stocks_file"

#joining the folder path and file path
file_path = os.path.join(folder_path, "stocks_data.csv")

#checking if the folder exists; if not it creates the folder
os.makedirs(folder_path, exist_ok=True)

try:
    with open(file_path, "w+", newline="") as file_data:
        writer = csv.DictWriter(file_data, ["Name", "Price"])

        writer.writeheader()
        writer.writerows(stocks)

        file_data.seek(0)

        reader = csv.DictReader(file_data)

        print(reader)

except FileNotFoundError:
    print(f"The file\"{file_path}\" is not found!!!")



#using pandas to read the csv file
stock_data_frame = pd.read_csv(file_path)
print(f"\n{stock_data_frame}")

#FIXME: ATTENTION PLEASE   !!!!!!!!!!!!!!!!!!!!!!!!
max_budget = 6000
min_budget = 1000
stock_data_frame["Buyable or not?"] = stock_data_frame["Price"].apply(lambda price: "YES" if min_budget <= price <= max_budget else "NO")  

print(f"\n{stock_data_frame}")

#now storing the dataframe into new csv file
stock_data_frame.to_csv("D:\Python\BRAODWAY\class_18\class_18_assignments\Major Assignment 2\stocks_file\stock_data_with_buyability.csv")