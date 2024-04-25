import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, time
import tensorflow as tf
import numpy as np
import pandas as pd
import math



class MlModel:
    def __init__(self, data, time):
        self.data = data
        self.time = time
        # Define the split time
        self.splittime = 1900

        # Get the train set
        self.time_train = self.time[: self.splittime]
        self.x_train = self.data[: self.splittime]

        # Get the validation set
        self.time_valid = self.time[self.splittime:]
        self.x_valid = self.data[self.splittime :]
        # print('================================================================')
        # print(self.x_valid)
        # print(self.time_valid)
        # print("-------------------------------------------------------")

        # Parameters
        self.window_size = 48
        self.batch_size = 40
        self.shuffle_buffer_size = 1000

    def windowed_dataset(self, series, window_size, batch_size, shuffle_buffer):
        """Generates dataset windows

        Args:
        series (array of float) - contains the values of the time series
        window_size (int) - the number of time steps to include in the feature
        batch_size (int) - the batch size
        shuffle_buffer(int) - buffer size to use for the shuffle method

        Returns:
        dataset (TF Dataset) - TF Dataset containing time windows
        """

        # Generate a TF Dataset from the series values
        dataset = tf.data.Dataset.from_tensor_slices(series)

        # Window the data but only take those with the specified size
        dataset = dataset.window(window_size + 1, shift=1, drop_remainder=True)

        # Flatten the windows by putting its elements in a single batch
        dataset = dataset.flat_map(lambda window: window.batch(window_size + 1))

        # Create tuples with features and labels
        dataset = dataset.map(lambda window: (window[:-1], window[-1]))

        # Shuffle the windows
        dataset = dataset.shuffle(shuffle_buffer)

        # Create batches of windows
        dataset = dataset.batch(batch_size).prefetch(1)
        # print(len(dataset))


        return dataset

    # Generate the dataset windows
    def create_dataseforML(self):
        self.dataset = self.windowed_dataset(
            self.x_train, self.window_size, self.batch_size, self.shuffle_buffer_size
        )

    def buildnetwork(self):

        self.model = tf.keras.models.Sequential(
            [

              tf.keras.layers.Conv1D(filters=50, kernel_size=3,
                                  strides=1,
                                  activation="relu",
                                  padding='causal',
                                  input_shape=[ self.window_size, 1]),
              tf.keras.layers.LSTM(64, return_sequences=True),
              tf.keras.layers.LSTM(64, return_sequences=True),
              tf.keras.layers.LSTM(32, return_sequences=True),
              tf.keras.layers.LSTM(32, return_sequences=True),
              tf.keras.layers.LSTM(32),
              tf.keras.layers.Dense(1),
              tf.keras.layers.Lambda(lambda x: x * 400)
              # =======================================================================/==========
                                
            ]
        )

    def weightinformations(self):
        # Print the initial layer weights
        print("Layer weights: \n {} \n".format(self.l0.get_weights()))

    # Print the model summary
    def model_summary(self):
        self.model.summary()

    # Set the training parameters
    def model_training(self):

        # Set the learning rate
        # learning_rate = 1e-6
        
        # Set the optimizer 
        optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)
        
        # Set the training parameters
        self.model.compile(loss=tf.keras.losses.Huber(),
                      optimizer=optimizer,
                      metrics=["mae"])

        # Train the model
        self.model.fit(self.dataset, epochs=50)

    def model_forecast(self, steps=100):
        self.data = np.array(self.data)
        forecast = []

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
    
        

        for _ in range(steps):
            forecast = np.append(
                forecast, self.model.predict(forecast[-self.window_size :][np.newaxis])
            )
            endtime += pd.Timedelta(hours=0.5)
            self.time_valid.append(endtime)
            self.x_valid = np.append(self.x_valid, 0)

        self.results = forecast.squeeze()
        return [self.results, self.time_valid, self.x_valid]

    # Compute the metrics
    def model_error(self):
        # print(tf.keras.metrics.mean_squared_error(self.x_valid, self.results).numpy())
        print(tf.keras.metrics.mean_absolute_error(self.x_valid, self.results).numpy())


    def save_model(self, filepath="./models/moditmodel"):
        # Save the model to the specified filepath
        self.model.save(filepath)
