import pandas as pd
import numpy as np

df = pd.read_csv('out.csv', header=0, engine='python')
df['Diff'] = 1/df['lastPx'] - 1/df['lastPx'].shift(1)
#print(df['Diff'])

if 'Sell' in df['side']:
    df['Profit_excl_fees'] = - df['lastQty']*df['Diff']
    print(df['Profit_excl_fees'])
else:
    df['Profit_excl_fees'] = df['lastQty']*df['Diff']
    print(df['Profit_excl_fees'])

df['Win/Loss_excl_fees']= np.where((df['Profit_excl_fees'])>0, 'W', 'L')

df['Profit_incl_fees'] = df['Profit_excl_fees']-((df['execComm'].shift(1) + df['execComm']) * 0.00000001)

df['Win/Loss_incl_fees']= np.where((df['Profit_incl_fees'])>0, 'W', 'L')

df['Long/Short']= np.where((df['side'])== 'Sell', 'SHORT', 'LONG')
    
df['Market_trade_fess'] = -((df['execComm'].shift(1) + df['execComm']) * 0.00000001)

df['Limit_trade_rebate'] = df['Market_trade_fess']/-3.00

"""
for i in range(0, len(df)):
    df['Capital_market_trading'].loc[i] = df['Capital_market_trading'].loc[i+1] + df['Profit_excl_fees'].loc[i] + df['Market_trade_fess'].loc[i]
"""
#df['Capital_market_trading'] = df['Capital_market_trading'].shift(1) + df['Profit_excl_fees'] + df['Market_trade_fess']
#df['Capital_market_trading'] = df['Win/Loss_excl_fees'] + df['Market_trade_fess'] + 0.022300000

total_entries = df['Win/Loss_excl_fees'].count()
print(total_entries)

df['win_count_excl_fees'] = np.where(df['Win/Loss_excl_fees']=='W', df['Win/Loss_excl_fees'].count(),'')

#df['Cumulative_win_excl_fees'] = df['win_ratio_excl_fees']/100.00

"""
def cnt(x):
     prev_count = 0
     for i in x:
         if i == 'W':
             prev_count+=1
     return prev_count
"""
#df['10trades_Rolling_Window_Win%']=df.where(df['Win/Loss_incl_fees'].eq('W')).groupby(df['Win/Loss_incl_fees']).rolling(10).count()

df.loc[df['Win/Loss_incl_fees']=='W','10trades_Rolling_Window_Win%'] = df.where(df['Win/Loss_incl_fees'].eq('W')).groupby(df['Win/Loss_incl_fees']).rolling(10).count()

df.to_csv('fulloutput.csv')

print(df['10trades_Rolling_Window_Win%'])
