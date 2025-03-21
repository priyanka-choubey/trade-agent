import os
import finnhub
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

# Setup client
FINNHUB_API_KEY = os.environ.get("FINNHUB_API_KEY")
finnhub_client = finnhub.Client(api_key=FINNHUB_API_KEY)

# Stock candles
# res = finnhub_client.stock_candles('AAPL', 'D', 1590988249, 1591852249)
# print(res)

# Aggregate Indicators
# print(finnhub_client.aggregate_indicator('AAPL', 'D'))

#Convert to Pandas Dataframe
print(pd.DataFrame(res))