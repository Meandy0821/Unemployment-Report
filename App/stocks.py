print("STOCKS REPORT...")

import os
from dotenv import load_dotenv
from pandas import read_csv
load_dotenv()

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")