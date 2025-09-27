# Cleaning the data

# import the libraries
import pandas as pd
import numpy as np

# read the data in pandas data frame
data = pd.read_csv("weatherAUS.csv")

# drop (delete) the unncecssary columns in the data
data = data.drop(['Date','Location','MinTemp','MaxTemp','Rainfall','Evaporation','Sunshine','WindGustDir','WindGustSpeed','WindDir9am','WindDir3pm','WindSpeed9am','WindSpeed3pm','Humidity9am','Humidity3pm','Pressure9am','Pressure3pm','Cloud9am','Cloud3pm','Temp9am','Temp3pm','RainToday','RainTomorrow',axis=1])
data = data.replace('NA', 0.0)

data.to_csv("weatherAUS.csv", index=False)