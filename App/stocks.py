


from pandas import read_csv


from app.alpha import API_KEY

def format_usd(my_price):
    return f"${my_price:,.2f}"


def fetch_stocks_data(symbo):
    request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={API_KEY}&datatype=csv"

    df = read_csv(request_url)

    return df


if __name__=="__main__":

    print("STOCKS REPORT...")
    
    symbol = input("Please input a crypto symbol(default")
    print("SYMBOL:", symbol)

    df = fetch_stocks_data(symbol)
    df = read_csv(request_url)
    print(df.columns)
    print(df.head())

    latest = df.iloc[0]

        #print(latest["timestamp"])
        #print(latest["close"])
        print("LATEST:", format_usd(latest["adjusted_close"]), "as of", latest["timestamp"])

        # Challenge B
        #
        # What is the highest high price (formatted as USD)?
        # What is the lowest low price (formatted as USD)?

        print("HIGH:", format_usd(df["high"].max()))
        print("LOW:", format_usd(df["low"].min()))

