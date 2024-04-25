import numpy as np
import pandas as pd
import tensorflow as tf


class Predict:
    def __init__(self, parray, tarray):
        self.model = tf.keras.models.load_model("./models/moditmodel")
        self.x = parray
        self.y = tarray

    def model_forecast(self, window_size):
        # def model_forecast(self, steps=100):
        self.data = self.x
        self.window_size = window_size
        self.time_valid = self.y
        self.x_valid = self.x
        self.data = np.array(self.data)
        forecast = []
        if 70 < len(self.data):
            self.splittime = len(self.data) - 70
        else:
            self.splittime = len(self.data)

        # Use the model to predict data points per window size
        for time in range(len(self.data) - self.window_size + 1):  # Changed range limit

            # Append prediction to forecast list
            a = self.model.predict(
                self.data[time : time + self.window_size][np.newaxis]
            )

            forecast.append(a)
        forecast = forecast[
            self.splittime - self.window_size + 1 :
        ]  # No need to subtract window size
        forecast = np.array(forecast)

        forecast = forecast.squeeze()

        # # Slice the points that are aligned with the validation set
        # # print(forecast[0:5])
        # # print(len(forecast[0:4]))

        # # Extend forecast beyond the validation set
        # # forecast = np.array(forecast)

        endtime = self.time_valid[len(self.time_valid) - 1]

        for _ in range(100):
            pval = self.model.predict(forecast[-self.window_size :][np.newaxis])
            pval=pval/2
                                      
            forecast = np.append(
                forecast, pval)
            
            endtime += pd.Timedelta(hours=0.5)
            self.time_valid.append(endtime)
            self.x_valid = np.append(self.x_valid, 0)

        self.results = forecast.squeeze()

        return [
            self.results,
            self.time_valid[self.splittime :],
            self.x_valid[self.splittime :],
        ]
