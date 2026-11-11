import pandas as pd

df = pd.read_csv("input_1.txt", header=None)
df.rename(columns={0:"depth"}, inplace=True)
df['delta'] = df['depth'].pct_change()
print ("🎄 Part 1: ", (df.loc[1:, 'delta'] > 0).sum())

ulim = len(df) - len(df)%3 + 1
df['sum'] = df.loc[0:ulim, 'depth'].rolling(3, center=True).sum()
df['delta_sum'] = df['sum'].pct_change()
print ("🎄 Part 2: ", (df.loc[0:, 'delta_sum'] > 0).sum())
