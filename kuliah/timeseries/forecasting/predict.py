import pandas as pd
import numpy as np
from fbprophet import Prophet

df = pd.read_csv("testing.csv")
df["y"] = np.log(df["y"])

m = Prophet()
m.fit(df)
future = m.make_future_dataframe(periods=7)
forecast = m.predict(future)
# print forecast[['ds','yhat', 'yhat_lower', 'yhat_upper']]
print np.exp(forecast[['yhat', 'yhat_lower', 'yhat_upper']])