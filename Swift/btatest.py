import btalib
import pandas as pd

df = pd.read_csv ('data/ta.txt', parse_dates=True, index_col='Data')

sma = btalib.sma(df, period=5)