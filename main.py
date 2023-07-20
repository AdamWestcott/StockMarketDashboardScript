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

downloads_path = str(Path.home() / "Downloads")
with open(downloads_path + '/stocks.csv', 'w', encoding="utf-8", newline='') as file:
    writer = csv.writer(file)
    ROW = []
    dataframeRow = 0
    ROW.append("Commodity Type")
    ROW.append("Commodity Value")
    ROW.append("Commodity Date")
    CSV_DATA.append(ROW)
    ROW = []

    alpha_vantage_crude_oil__WTI_response = requests.get("https://www.alphavantage.co/query?function=WTI&interval=daily&apikey="+ApiKeys.alpha_vantage_api_key, headers=alpha_vantage_headers)

    if alpha_vantage_crude_oil__WTI_response.status_code != 200:
        print('Status:', alpha_vantage_crude_oil__WTI_response.status_code, 'Headers:', alpha_vantage_crude_oil__WTI_response.headers)
    alpha_vantage_crude_oil__WTI_response_json = alpha_vantage_crude_oil__WTI_response.json()
    commodity_name = alpha_vantage_crude_oil__WTI_response_json["name"]
    alpha_vantage_crude_oil__WTI_data = alpha_vantage_crude_oil__WTI_response_json["data"]
    alpha_vantage_current_day_data = alpha_vantage_crude_oil__WTI_data[0]
    current_day = alpha_vantage_current_day_data["date"]
    current_value = alpha_vantage_current_day_data["value"]

    print(alpha_vantage_crude_oil__WTI_data[0])
    ROW.append(alpha_vantage_crude_oil__WTI_response_json["name"])
    ROW.append(current_value)
    ROW.append(current_day)
    CSV_DATA.append(ROW)
    ROW = []         
    writer.writerows(CSV_DATA)
