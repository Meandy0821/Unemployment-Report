
import json
from pprint import pprint
from statistics import mean

import requests
from plotly.express import line


from app.alha import API_KEY


API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")

request_url = f"https://www.alphavantage.co/query"


response = requests.get(request_url)

parsed_response = json.loads(response.text)
print(type(parsed_response))
pprint(parsed_response)


# breakpoint()

latest = parsed_response["data"][0]
print(latest)


from statistics import mean

this_year = [d for d in data if "2022-" in d["date"]]

rates_this_year = [float(d["value"]) for d in this_year]
#print(rates_this_year)

print("-------------------------")
print("AVG UNEMPLOYMENT THIS YEAR:", f"{mean(rates_this_year)}%")
print("NO MONTHS:", len(this_year))

from plotly.express import line

dates = [d["date"] for d in data]
rates = [float(d["value"]) for d in data]

fig = line(x=dates, y=rates, title="United States Unemployment Rate over time", labels= {"x": "Month", "y": "Unemployment Rate"})
fig.show()
