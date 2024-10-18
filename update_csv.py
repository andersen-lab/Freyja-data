import pandas as pd

df_barcodes = pd.read_feather('usher_barcodes.feather').set_index('index')
df_barcodes.to_csv('usher_barcodes.csv')