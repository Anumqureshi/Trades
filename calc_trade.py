import pandas as pd
import numpy as np

df = pd.read_csv('input.csv', header=0, engine='python')

# maybe a loop

rows = len(df)-2
print(rows)

i = 0

while i < rows:
    if df.loc[i,'side'] == 'Buy' and df.loc[i+1,'side'] == 'Sell':
        if df.loc[i,'lastQty'] == df.loc[i+1,'lastQty']: # if in side column, a sell comes after a buy and the two quantities are same then put a "trade" in trade column
            df.loc[i, "trade"] = "Trade"
            i += 1
    elif df.loc[i,'side'] == 'Buy' and df.loc[i+1,'side'] == 'Sell' and df.loc[i+2,'side'] == 'Sell':
        if df.loc[i,'lastQty'] == df.loc[i+2,'lastQty'] + df.loc[i+1,'lastQty']: # if there is a buy and then sell + sell, and buy_Qty = Sell_qty1 + SellQty2, it's a trade.
            df.loc[i, "trade"] = "Trade"
            i += 2
    elif df.loc[i,'side'] == 'Sell' and df.loc[i+1,'side'] == 'Buy':
        if df.loc[i,'lastQty'] == df.loc[i+1,'lastQty']:
            df.loc[i,"trade"] = "Trade"
            i += 1

    elif df.loc[i,'side'] == 'Sell' and df.loc[i+1,'side'] == 'Buy' and df.loc[i+2,'side'] == 'Buy':
        if df.loc[i,'lastQty'] == df.loc[i+2,'lastQty'] + df.loc[i+1,'lastQty']:
            df.loc[i, "trade"] = "Trade"
            i += 2

    i += 1


# df =df.fillna("No Trade")
df.to_csv('output.csv')
print(df.head(12))
