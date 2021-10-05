import yfinance as yf
import matplotlib.pyplot as plt


#websocket data stream here

df = yf.download('TSLA', start= "2020-11-01")

def MACD(df):
    df["EMA12"] = df.Close.ewm(span=12).mean()
    df["EMA26"] = df.Close.ewm(span=26).mean()
    df['MACD'] = df.EMA12 - df.EMA26
    df['signal'] = df.MACD.ewm(span=9).mean()
    print("indicators added")

MACD(df)

plt.plot(df.signal, label='signal', color='red')
plt.plot(df.MACD, label='MACD', color='green')
plt.legend()
plt.show()

#for i in range(2,len(df)):
 #   if df.MACD.iloc[i] > df.signal.iloc[i] and df.MACD.iloc[i-1] < df.signal.iloc[i-1]:
  #      Buy.append(i)
   # elif df.MACD.iloc[i] < df.signal.iloc[i] and df.MACD.iloc[i-1] > df.signal.iloc[i-1]:
    #    Sell.append(i)