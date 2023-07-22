import csv
import requests
from datetime import time, datetime
from pathlib import Path
import ApiKeys

alpha_vantage_headers = {
    "accept": "application/json",
    "User-Agent": "request"
}

params = {}
ips = []

CSV_DATA = []
#Commodity_List = ["WTI","BRENT","NATURAL_GAS","COPPER","ALUMINUM","WHEAT","CORN","COTTON","SUGAR","COFFEE"]
Commodity_List = ["WTI","BRENT","NATURAL_GAS","COPPER","ALUMINUM"]

downloads_path = str(Path.home() / "Downloads")
with open(downloads_path + '/Commodities.csv', 'w', encoding="utf-8", newline='') as file:
    writer = csv.writer(file)
    ROW = []
    dataframeRow = 0
    ROW.append("Commodity Type")
    ROW.append("Commodity Value")
    ROW.append("Commodity Unit")
    ROW.append("Commodity Date")
    CSV_DATA.append(ROW)
    ROW = []
    for commodity in Commodity_List:
        print(commodity)
        alpha_vantage_commodity_response = requests.get("https://www.alphavantage.co/query?function="+str(commodity)+"&interval=daily&apikey="+ApiKeys.alpha_vantage_api_key, headers=alpha_vantage_headers)

        if alpha_vantage_commodity_response.status_code != 200:
            print('Status:', alpha_vantage_commodity_response.status_code, 'Headers:', alpha_vantage_commodity_response.headers)
        alpha_vantage_commodity_response_json = alpha_vantage_commodity_response.json()
        print(alpha_vantage_commodity_response_json)
        commodity_name = alpha_vantage_commodity_response_json["name"]
        commodity_unit = alpha_vantage_commodity_response_json["unit"]
        alpha_vantage_commodity_data = alpha_vantage_commodity_response_json["data"]

        for day in range(len(alpha_vantage_commodity_data)):
            alpha_vantage_current_day_data = alpha_vantage_commodity_data[day]
            current_day = alpha_vantage_current_day_data["date"]
            current_value = alpha_vantage_current_day_data["value"]
            if current_value == ".":
                current_value = "Unknown"

            ROW.append(commodity_name)
            ROW.append(current_value)
            ROW.append(commodity_unit)
            ROW.append(current_day)
            CSV_DATA.append(ROW)
            ROW = []         
    writer.writerows(CSV_DATA)
